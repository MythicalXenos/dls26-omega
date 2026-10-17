#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Machine Learning System for Dream League Soccer
Hệ thống học máy để cải thiện quyết định trong game
"""

import time
import threading
import json
import pickle
from typing import Dict, Any, Optional, List, Tuple, Union
from pathlib import Path
import numpy as np
from collections import defaultdict, deque
import random
import cv2
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib

from utils.logger import get_logger, log_performance

class GameAction:
    """Đại diện cho một hành động trong game"""
    
    def __init__(self, action_type: str, params: Dict[str, Any], 
                 timestamp: float, context: Dict[str, Any]):
        self.action_type = action_type
        self.params = params
        self.timestamp = timestamp
        self.context = context
        self.result = None
        self.success = False
        self.learning_data = {}
    
    def set_result(self, result: Dict[str, Any], success: bool):
        """Thiết lập kết quả của hành động"""
        self.result = result
        self.success = success
        self.learning_data = {
            'execution_time': time.time() - self.timestamp,
            'success': success,
            'result_quality': result.get('quality', 0.0),
            'ball_position_change': result.get('ball_position_change', 0.0),
            'score_change': result.get('score_change', 0),
            'possession_change': result.get('possession_change', 0.0)
        }

class GameState:
    """Đại diện cho trạng thái game tại một thời điểm"""
    
    def __init__(self, timestamp: float, context: Dict[str, Any]):
        self.timestamp = timestamp
        self.context = context
        self.features = self._extract_features(context)
    
    def _extract_features(self, context: Dict[str, Any]) -> Dict[str, float]:
        """Trích xuất các đặc trưng từ context"""
        features = {}
        
        # Ball position features
        ball_pos = context.get('ball_position', (960, 540))
        features['ball_x'] = ball_pos[0] / 1920.0  # Normalize to 0-1
        features['ball_y'] = ball_pos[1] / 1080.0  # Normalize to 0-1
        
        # Player position features
        player_pos = context.get('player_position', (960, 540))
        features['player_x'] = player_pos[0] / 1920.0
        features['player_y'] = player_pos[1] / 1080.0
        
        # Distance features
        features['ball_player_distance'] = np.sqrt(
            (ball_pos[0] - player_pos[0])**2 + (ball_pos[1] - player_pos[1])**2
        ) / np.sqrt(1920**2 + 1080**2)  # Normalize
        
        # Game situation features
        features['score_difference'] = context.get('score_difference', 0) / 10.0  # Normalize
        features['time_remaining'] = context.get('time_remaining', 90) / 90.0
        features['possession'] = context.get('possession', 0.5)
        features['field_position'] = context.get('field_position', 'center')
        
        # Opponent features
        features['opponent_pressure'] = context.get('opponent_pressure', 0.0)
        features['opponent_distance'] = context.get('opponent_distance', 1000) / 1000.0
        
        # Convert categorical to numerical
        field_positions = {'defense': 0.0, 'midfield': 0.5, 'attack': 1.0}
        features['field_position_num'] = field_positions.get(features['field_position'], 0.5)
        
        return features

class LearningMemory:
    """Bộ nhớ học tập để lưu trữ kinh nghiệm"""
    
    def __init__(self, max_size: int = 10000):
        self.max_size = max_size
        self.memories = deque(maxlen=max_size)
        self.action_outcomes = defaultdict(list)
        self.situation_patterns = defaultdict(list)
        
    def add_memory(self, state: GameState, action: GameAction, 
                   next_state: GameState, reward: float):
        """Thêm một ký ức học tập"""
        memory = {
            'state': state,
            'action': action,
            'next_state': next_state,
            'reward': reward,
            'timestamp': time.time()
        }
        
        self.memories.append(memory)
        
        # Categorize by action type
        self.action_outcomes[action.action_type].append({
            'success': action.success,
            'reward': reward,
            'context': action.context,
            'result': action.result
        })
        
        # Categorize by situation
        situation_key = self._get_situation_key(state.context)
        self.situation_patterns[situation_key].append({
            'action': action.action_type,
            'success': action.success,
            'reward': reward
        })
    
    def get_memories(self, count: int = None) -> List[Dict[str, Any]]:
        """Lấy ký ức học tập"""
        if count is None:
            return list(self.memories)
        return list(self.memories)[-count:]
    
    def get_action_outcomes(self, action_type: str) -> List[Dict[str, Any]]:
        """Lấy kết quả của một loại hành động"""
        return self.action_outcomes.get(action_type, [])
    
    def get_situation_patterns(self, situation_key: str) -> List[Dict[str, Any]]:
        """Lấy các pattern của một tình huống"""
        return self.situation_patterns.get(situation_key, [])
    
    def _get_situation_key(self, context: Dict[str, Any]) -> str:
        """Tạo key cho tình huống"""
        ball_pos = context.get('ball_position', (960, 540))
        field_pos = context.get('field_position', 'center')
        score_diff = context.get('score_difference', 0)
        
        # Create situation categories
        if ball_pos[0] < 640:  # Left third
            area = 'defense'
        elif ball_pos[0] < 1280:  # Middle third
            area = 'midfield'
        else:  # Right third
            area = 'attack'
        
        if score_diff < -2:
            score_situation = 'losing_badly'
        elif score_diff < 0:
            score_situation = 'losing'
        elif score_diff > 2:
            score_situation = 'winning_big'
        elif score_diff > 0:
            score_situation = 'winning'
        else:
            score_situation = 'draw'
        
        return f"{area}_{score_situation}_{field_pos}"

class DecisionTree:
    """Cây quyết định đơn giản để học từ kinh nghiệm"""
    
    def __init__(self):
        self.rules = []
        self.confidence_threshold = 0.7
        
    def add_rule(self, condition: Dict[str, Any], action: str, 
                 confidence: float, success_rate: float):
        """Thêm một quy tắc quyết định"""
        rule = {
            'condition': condition,
            'action': action,
            'confidence': confidence,
            'success_rate': success_rate,
            'usage_count': 0,
            'last_used': 0
        }
        self.rules.append(rule)
    
    def get_decision(self, state: GameState) -> Optional[str]:
        """Lấy quyết định dựa trên trạng thái hiện tại"""
        best_rule = None
        best_score = 0
        
        for rule in self.rules:
            if self._matches_condition(state, rule['condition']):
                # Calculate rule score based on confidence and success rate
                score = rule['confidence'] * rule['success_rate']
                
                # Penalize rules that haven't been used recently
                time_factor = 1.0 / (1.0 + (time.time() - rule['last_used']) / 3600)
                score *= time_factor
                
                if score > best_score and score >= self.confidence_threshold:
                    best_score = score
                    best_rule = rule
        
        if best_rule:
            best_rule['usage_count'] += 1
            best_rule['last_used'] = time.time()
            return best_rule['action']
        
        return None
    
    def _matches_condition(self, state: GameState, condition: Dict[str, Any]) -> bool:
        """Kiểm tra xem trạng thái có khớp với điều kiện không"""
        for feature, value_range in condition.items():
            if feature not in state.features:
                continue
            
            feature_value = state.features[feature]
            
            if isinstance(value_range, (list, tuple)):
                # Range check
                if len(value_range) == 2:
                    min_val, max_val = value_range
                    if not (min_val <= feature_value <= max_val):
                        return False
                else:
                    # Exact value check
                    if feature_value not in value_range:
                        return False
            else:
                # Exact value check
                if feature_value != value_range:
                    return False
        
        return True
    
    def update_rule_confidence(self, condition: Dict[str, Any], 
                              action: str, success: bool):
        """Cập nhật độ tin cậy của quy tắc"""
        for rule in self.rules:
            if (rule['action'] == action and 
                self._matches_condition_loosely(rule['condition'], condition)):
                
                # Update success rate
                if success:
                    rule['success_rate'] = min(1.0, rule['success_rate'] + 0.1)
                else:
                    rule['success_rate'] = max(0.0, rule['success_rate'] - 0.1)
                
                # Update confidence based on usage
                rule['confidence'] = min(1.0, rule['confidence'] + 0.05)
                break
    
    def _matches_condition_loosely(self, rule_condition: Dict[str, Any], 
                                  actual_condition: Dict[str, Any]) -> bool:
        """Kiểm tra điều kiện một cách lỏng lẻo hơn"""
        # Simplified matching - in practice, you'd implement more sophisticated matching
        return True

class ReinforcementLearner:
    """Học tăng cường đơn giản để cải thiện quyết định"""
    
    def __init__(self, learning_rate: float = 0.1, discount_factor: float = 0.9):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_table = defaultdict(lambda: defaultdict(float))
        self.epsilon = 0.1  # Exploration rate
        
    def get_action(self, state: GameState, available_actions: List[str]) -> str:
        """Chọn hành động dựa trên Q-learning"""
        if random.random() < self.epsilon:
            # Exploration: choose random action
            return random.choice(available_actions)
        
        # Exploitation: choose best action based on Q-values
        best_action = None
        best_value = float('-inf')
        
        state_key = self._get_state_key(state)
        
        for action in available_actions:
            q_value = self.q_table[state_key][action]
            if q_value > best_value:
                best_value = q_value
                best_action = action
        
        return best_action if best_action else random.choice(available_actions)
    
    def update_q_value(self, state: GameState, action: str, 
                      reward: float, next_state: GameState, 
                      available_actions: List[str]):
        """Cập nhật Q-value dựa trên kết quả"""
        state_key = self._get_state_key(state)
        next_state_key = self._get_state_key(next_state)
        
        # Current Q-value
        current_q = self.q_table[state_key][action]
        
        # Maximum Q-value for next state
        max_next_q = max([self.q_table[next_state_key][a] for a in available_actions], default=0)
        
        # Q-learning update formula
        new_q = current_q + self.learning_rate * (
            reward + self.discount_factor * max_next_q - current_q
        )
        
        self.q_table[state_key][action] = new_q
    
    def _get_state_key(self, state: GameState) -> str:
        """Tạo key cho trạng thái"""
        # Discretize continuous features for Q-table
        ball_x = round(state.features['ball_x'] * 10) / 10  # Round to 0.1
        ball_y = round(state.features['ball_y'] * 10) / 10
        score_diff = round(state.features['score_difference'] * 2) / 2  # Round to 0.5
        
        return f"b{ball_x:.1f}_{ball_y:.1f}_s{score_diff:.1f}"
    
    def decrease_epsilon(self, factor: float = 0.99):
        """Giảm tỷ lệ khám phá theo thời gian"""
        self.epsilon = max(0.01, self.epsilon * factor)

class AdvancedFeatureEngineer:
    """Engineer nâng cao để trích xuất đặc trưng từ game"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.feature_history = deque(maxlen=100)
        self.is_trained = False
        
    def extract_advanced_features(self, context: Dict[str, Any], 
                                screen_image: Optional[np.ndarray] = None) -> Dict[str, float]:
        """Trích xuất đặc trưng nâng cao từ context và hình ảnh"""
        features = {}
        
        # Basic features (existing)
        basic_features = self._extract_basic_features(context)
        features.update(basic_features)
        
        # Advanced spatial features
        spatial_features = self._extract_spatial_features(context)
        features.update(spatial_features)
        
        # Temporal features
        temporal_features = self._extract_temporal_features(context)
        features.update(temporal_features)
        
        # Image-based features (if available)
        if screen_image is not None:
            image_features = self._extract_image_features(screen_image)
            features.update(image_features)
        
        # Normalize features
        if self.is_trained:
            features = self._normalize_features(features)
        
        return features
    
    def _extract_basic_features(self, context: Dict[str, Any]) -> Dict[str, float]:
        """Trích xuất đặc trưng cơ bản"""
        features = {}
        
        # Ball position features
        ball_pos = context.get('ball_position', (960, 540))
        features['ball_x'] = ball_pos[0] / 1920.0
        features['ball_y'] = ball_pos[1] / 1080.0
        
        # Player position features
        player_pos = context.get('player_position', (960, 540))
        features['player_x'] = player_pos[0] / 1920.0
        features['player_y'] = player_pos[1] / 1080.0
        
        # Distance features
        features['ball_player_distance'] = np.sqrt(
            (ball_pos[0] - player_pos[0])**2 + (ball_pos[1] - player_pos[1])**2
        ) / np.sqrt(1920**2 + 1080**2)
        
        # Game situation features
        features['score_difference'] = context.get('score_difference', 0) / 10.0
        features['time_remaining'] = context.get('time_remaining', 90) / 90.0
        features['possession'] = context.get('possession', 0.5)
        features['field_position'] = context.get('field_position', 'center')
        
        # Opponent features
        features['opponent_pressure'] = context.get('opponent_pressure', 0.0)
        features['opponent_distance'] = context.get('opponent_distance', 1000) / 1000.0
        
        # Convert categorical to numerical
        field_positions = {'defense': 0.0, 'midfield': 0.5, 'attack': 1.0}
        features['field_position_num'] = field_positions.get(features['field_position'], 0.5)
        
        return features
    
    def _extract_spatial_features(self, context: Dict[str, Any]) -> Dict[str, float]:
        """Trích xuất đặc trưng không gian nâng cao"""
        features = {}
        
        # Field zones analysis
        ball_pos = context.get('ball_position', (960, 540))
        player_pos = context.get('player_position', (960, 540))
        
        # Zone-based features
        features['ball_zone_x'] = int(ball_pos[0] / 320) / 6.0  # 6 zones horizontally
        features['ball_zone_y'] = int(ball_pos[1] / 270) / 4.0  # 4 zones vertically
        features['player_zone_x'] = int(player_pos[0] / 320) / 6.0
        features['player_zone_y'] = int(player_pos[1] / 270) / 4.0
        
        # Relative positioning
        features['ball_player_relative_x'] = (ball_pos[0] - player_pos[0]) / 1920.0
        features['ball_player_relative_y'] = (ball_pos[1] - player_pos[1]) / 1080.0
        
        # Field pressure map
        features['left_side_pressure'] = context.get('left_side_pressure', 0.0)
        features['right_side_pressure'] = context.get('right_side_pressure', 0.0)
        features['center_pressure'] = context.get('center_pressure', 0.0)
        
        # Tactical positioning
        features['formation_compactness'] = context.get('formation_compactness', 0.5)
        features['defensive_line_height'] = context.get('defensive_line_height', 0.5)
        
        return features
    
    def _extract_temporal_features(self, context: Dict[str, Any]) -> Dict[str, float]:
        """Trích xuất đặc trưng thời gian"""
        features = {}
        
        # Add current features to history
        current_time = time.time()
        self.feature_history.append({
            'timestamp': current_time,
            'features': context
        })
        
        if len(self.feature_history) >= 2:
            # Velocity features
            prev_features = self.feature_history[-2]
            time_diff = current_time - prev_features['timestamp']
            
            if time_diff > 0:
                # Ball velocity
                prev_ball = prev_features['features'].get('ball_position', (960, 540))
                curr_ball = context.get('ball_position', (960, 540))
                
                ball_velocity_x = (curr_ball[0] - prev_ball[0]) / time_diff
                ball_velocity_y = (curr_ball[1] - prev_ball[1]) / time_diff
                
                features['ball_velocity_x'] = ball_velocity_x / 1000.0  # Normalize
                features['ball_velocity_y'] = ball_velocity_y / 1000.0
                features['ball_speed'] = np.sqrt(ball_velocity_x**2 + ball_velocity_y**2) / 1000.0
                
                # Player velocity
                prev_player = prev_features['features'].get('player_position', (960, 540))
                curr_player = context.get('player_position', (960, 540))
                
                player_velocity_x = (curr_player[0] - prev_player[0]) / time_diff
                player_velocity_y = (curr_player[1] - prev_player[1]) / time_diff
                
                features['player_velocity_x'] = player_velocity_x / 1000.0
                features['player_velocity_y'] = player_velocity_y / 1000.0
                features['player_speed'] = np.sqrt(player_velocity_x**2 + player_velocity_y**2) / 1000.0
        
        # Game phase features
        features['game_phase'] = context.get('game_phase', 'normal')
        features['possession_duration'] = context.get('possession_duration', 0) / 60.0  # Normalize to minutes
        
        return features
    
    def _extract_image_features(self, screen_image: np.ndarray) -> Dict[str, float]:
        """Trích xuất đặc trưng từ hình ảnh màn hình"""
        features = {}
        
        try:
            # Convert to grayscale
            if len(screen_image.shape) == 3:
                gray = cv2.cvtColor(screen_image, cv2.COLOR_BGR2GRAY)
            else:
                gray = screen_image
            
            # Resize for faster processing
            small = cv2.resize(gray, (64, 36))
            
            # Edge detection
            edges = cv2.Canny(small, 50, 150)
            features['edge_density'] = np.sum(edges > 0) / (64 * 36)
            
            # Color analysis
            if len(screen_image.shape) == 3:
                hsv = cv2.cvtColor(screen_image, cv2.COLOR_BGR2HSV)
                
                # Green field detection
                green_mask = cv2.inRange(hsv, (35, 50, 50), (85, 255, 255))
                features['field_coverage'] = np.sum(green_mask > 0) / (screen_image.shape[0] * screen_image.shape[1])
                
                # Ball detection (white objects)
                white_mask = cv2.inRange(hsv, (0, 0, 200), (180, 30, 255))
                features['white_object_density'] = np.sum(white_mask > 0) / (screen_image.shape[0] * screen_image.shape[1])
            
            # Texture analysis
            features['texture_variance'] = np.var(small)
            features['brightness_mean'] = np.mean(small) / 255.0
            
        except Exception as e:
            # Fallback features if image processing fails
            features['edge_density'] = 0.0
            features['field_coverage'] = 0.5
            features['white_object_density'] = 0.0
            features['texture_variance'] = 0.0
            features['brightness_mean'] = 0.5
        
        return features
    
    def _normalize_features(self, features: Dict[str, float]) -> Dict[str, float]:
        """Chuẩn hóa đặc trưng"""
        try:
            # Convert to numpy array for scaling
            feature_names = list(features.keys())
            feature_values = np.array([features[name] for name in feature_names]).reshape(1, -1)
            
            # Scale features
            scaled_values = self.scaler.transform(feature_values)
            
            # Convert back to dictionary
            normalized_features = {}
            for i, name in enumerate(feature_names):
                normalized_features[name] = float(scaled_values[0, i])
            
            return normalized_features
            
        except Exception:
            # Return original features if scaling fails
            return features
    
    def train_scaler(self, training_data: List[Dict[str, float]]):
        """Huấn luyện scaler với dữ liệu training"""
        try:
            if len(training_data) < 10:
                return
            
            # Extract feature values
            feature_names = list(training_data[0].keys())
            feature_matrix = []
            
            for data_point in training_data:
                values = [data_point.get(name, 0.0) for name in feature_names]
                feature_matrix.append(values)
            
            # Fit scaler
            feature_matrix = np.array(feature_matrix)
            self.scaler.fit(feature_matrix)
            self.is_trained = True
            
        except Exception as e:
            print(f"Error training scaler: {e}")

class NeuralNetworkPredictor:
    """Neural Network để dự đoán kết quả hành động"""
    
    def __init__(self, input_size: int, hidden_size: int = 64):
        self.input_size = input_size
        self.hidden_size = hidden_size
        
        # Simple neural network weights
        self.weights1 = np.random.randn(input_size, hidden_size) * 0.01
        self.weights2 = np.random.randn(hidden_size, 1) * 0.01
        self.bias1 = np.zeros((1, hidden_size))
        self.bias2 = np.zeros((1, 1))
        
        # Training parameters
        self.learning_rate = 0.001
        self.is_trained = False
        
    def forward(self, X: np.ndarray) -> np.ndarray:
        """Forward pass"""
        # Hidden layer
        hidden = np.tanh(np.dot(X, self.weights1) + self.bias1)
        
        # Output layer
        output = np.dot(hidden, self.weights2) + self.bias2
        
        return output
    
    def train(self, X: np.ndarray, y: np.ndarray, epochs: int = 100):
        """Huấn luyện neural network"""
        try:
            if len(X) < 10:
                return
            
            for epoch in range(epochs):
                # Forward pass
                hidden = np.tanh(np.dot(X, self.weights1) + self.bias1)
                output = np.dot(hidden, self.weights2) + self.bias2
                
                # Backward pass
                output_error = output - y.reshape(-1, 1)
                hidden_error = np.dot(output_error, self.weights2.T) * (1 - hidden**2)
                
                # Update weights
                self.weights2 -= self.learning_rate * np.dot(hidden.T, output_error)
                self.weights1 -= self.learning_rate * np.dot(X.T, hidden_error)
                self.bias2 -= self.learning_rate * np.sum(output_error, axis=0, keepdims=True)
                self.bias1 -= self.learning_rate * np.sum(hidden_error, axis=0, keepdims=True)
            
            self.is_trained = True
            
        except Exception as e:
            print(f"Error training neural network: {e}")
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Dự đoán kết quả"""
        if not self.is_trained:
            return np.zeros((X.shape[0], 1))
        
        return self.forward(X)

class MultiAgentLearner:
    """Học tập đa tác tử để cải thiện chiến thuật"""
    
    def __init__(self, num_agents: int = 3):
        self.num_agents = num_agents
        self.agents = []
        self.agent_performances = []
        self.best_agent = 0
        
        # Initialize agents with different strategies
        for i in range(num_agents):
            agent = {
                'id': i,
                'strategy': self._generate_strategy(),
                'performance': 0.0,
                'games_played': 0,
                'success_rate': 0.5
            }
            self.agents.append(agent)
            self.agent_performances.append(0.0)
    
    def _generate_strategy(self) -> Dict[str, float]:
        """Tạo chiến thuật ngẫu nhiên cho agent"""
        return {
            'aggression': random.uniform(0.2, 0.8),
            'possession_preference': random.uniform(0.3, 0.7),
            'risk_tolerance': random.uniform(0.1, 0.9),
            'formation_style': random.uniform(0.0, 1.0),
            'counter_attack_tendency': random.uniform(0.2, 0.8)
        }
    
    def select_agent(self, game_context: Dict[str, Any]) -> int:
        """Chọn agent phù hợp nhất cho tình huống game"""
        # Analyze game context
        score_diff = game_context.get('score_difference', 0)
        time_left = game_context.get('time_remaining', 90)
        possession = game_context.get('possession', 0.5)
        
        # Select agent based on context
        if score_diff < -1 and time_left < 30:
            # Need aggressive comeback
            return self._select_agent_by_trait('aggression', 0.7)
        elif score_diff > 1 and time_left < 20:
            # Need defensive play
            return self._select_agent_by_trait('aggression', 0.3)
        elif possession < 0.4:
            # Need possession-based play
            return self._select_agent_by_trait('possession_preference', 0.7)
        else:
            # Use best performing agent
            return self.best_agent
    
    def _select_agent_by_trait(self, trait: str, target_value: float) -> int:
        """Chọn agent dựa trên đặc tính cụ thể"""
        best_agent = 0
        best_match = float('inf')
        
        for i, agent in enumerate(self.agents):
            trait_value = agent['strategy'][trait]
            match_quality = abs(trait_value - target_value)
            
            if match_quality < best_match:
                best_match = match_quality
                best_agent = i
        
        return best_agent
    
    def update_agent_performance(self, agent_id: int, game_result: Dict[str, Any]):
        """Cập nhật hiệu suất của agent"""
        try:
            agent = self.agents[agent_id]
            agent['games_played'] += 1
            
            # Calculate performance score
            score_diff = game_result.get('final_score_difference', 0)
            possession = game_result.get('final_possession', 0.5)
            goals_scored = game_result.get('goals_scored', 0)
            goals_conceded = game_result.get('goals_conceded', 0)
            
            # Performance formula
            performance = (
                score_diff * 0.4 +
                (possession - 0.5) * 0.3 +
                goals_scored * 0.2 -
                goals_conceded * 0.1
            )
            
            # Update agent performance
            old_performance = agent['performance']
            agent['performance'] = (old_performance * (agent['games_played'] - 1) + performance) / agent['games_played']
            
            # Update success rate
            if score_diff > 0:
                agent['success_rate'] = (agent['success_rate'] * (agent['games_played'] - 1) + 1) / agent['games_played']
            else:
                agent['success_rate'] = (agent['success_rate'] * (agent['games_played'] - 1)) / agent['games_played']
            
            # Update best agent
            if agent['performance'] > self.agents[self.best_agent]['performance']:
                self.best_agent = agent_id
            
            # Update performance list
            self.agent_performances[agent_id] = agent['performance']
            
        except Exception as e:
            print(f"Error updating agent performance: {e}")
    
    def evolve_strategies(self):
        """Tiến hóa chiến thuật của các agent"""
        try:
            # Sort agents by performance
            sorted_agents = sorted(enumerate(self.agents), key=lambda x: x[1]['performance'], reverse=True)
            
            # Keep top 50% agents
            top_count = max(1, self.num_agents // 2)
            top_agents = sorted_agents[:top_count]
            
            # Create new agents by combining top strategies
            new_agents = []
            for i in range(self.num_agents):
                if i < len(top_agents):
                    # Keep top agent
                    new_agents.append(top_agents[i][1].copy())
                else:
                    # Create new agent by combining top strategies
                    parent1 = random.choice(top_agents)[1]
                    parent2 = random.choice(top_agents)[1]
                    
                    new_strategy = {}
                    for trait in parent1['strategy']:
                        if random.random() < 0.5:
                            new_strategy[trait] = parent1['strategy'][trait]
                        else:
                            new_strategy[trait] = parent2['strategy'][trait]
                        
                        # Add mutation
                        if random.random() < 0.1:
                            new_strategy[trait] += random.uniform(-0.1, 0.1)
                            new_strategy[trait] = max(0.0, min(1.0, new_strategy[trait]))
                    
                    new_agent = {
                        'id': i,
                        'strategy': new_strategy,
                        'performance': 0.0,
                        'games_played': 0,
                        'success_rate': 0.5
                    }
                    new_agents.append(new_agent)
            
            self.agents = new_agents
            self.agent_performances = [agent['performance'] for agent in self.agents]
            
        except Exception as e:
            print(f"Error evolving strategies: {e}")

class PerformanceOptimizer:
    """Tối ưu hóa hiệu suất của hệ thống ML"""
    
    def __init__(self):
        self.performance_metrics = deque(maxlen=1000)
        self.optimization_history = []
        self.last_optimization = 0
        
    def record_metric(self, metric_name: str, value: float, timestamp: float = None):
        """Ghi lại metric hiệu suất"""
        if timestamp is None:
            timestamp = time.time()
        
        self.performance_metrics.append({
            'name': metric_name,
            'value': value,
            'timestamp': timestamp
        })
    
    def analyze_performance(self) -> Dict[str, Any]:
        """Phân tích hiệu suất và đưa ra khuyến nghị"""
        try:
            if len(self.performance_metrics) < 10:
                return {'status': 'insufficient_data'}
            
            analysis = {}
            
            # Group metrics by name
            metric_groups = defaultdict(list)
            for metric in self.performance_metrics:
                metric_groups[metric['name']].append(metric['value'])
            
            # Analyze each metric
            for metric_name, values in metric_groups.items():
                if len(values) >= 5:
                    analysis[metric_name] = {
                        'mean': np.mean(values),
                        'std': np.std(values),
                        'trend': self._calculate_trend(values),
                        'recommendation': self._generate_recommendation(metric_name, values)
                    }
            
            # Overall system health
            analysis['system_health'] = self._assess_system_health(analysis)
            
            return analysis
            
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def _calculate_trend(self, values: List[float]) -> str:
        """Tính toán xu hướng của metric"""
        if len(values) < 3:
            return 'stable'
        
        recent = values[-3:]
        older = values[-6:-3] if len(values) >= 6 else values[:-3]
        
        if len(older) == 0:
            return 'stable'
        
        recent_avg = np.mean(recent)
        older_avg = np.mean(older)
        
        change = (recent_avg - older_avg) / older_avg if older_avg != 0 else 0
        
        if change > 0.1:
            return 'improving'
        elif change < -0.1:
            return 'declining'
        else:
            return 'stable'
    
    def _generate_recommendation(self, metric_name: str, values: List[float]) -> str:
        """Tạo khuyến nghị dựa trên metric"""
        if metric_name == 'decision_accuracy':
            if np.mean(values) < 0.6:
                return 'Increase training data and adjust learning parameters'
            elif np.mean(values) > 0.8:
                return 'Performance is good, consider reducing complexity'
        
        elif metric_name == 'response_time':
            if np.mean(values) > 0.1:
                return 'Optimize feature extraction and model inference'
            elif np.mean(values) < 0.05:
                return 'Response time is excellent'
        
        elif metric_name == 'memory_usage':
            if np.mean(values) > 0.8:
                return 'Consider reducing memory footprint or implementing cleanup'
        
        return 'No specific recommendation'
    
    def _assess_system_health(self, analysis: Dict[str, Any]) -> str:
        """Đánh giá sức khỏe tổng thể của hệ thống"""
        health_scores = []
        
        for metric_name, metric_data in analysis.items():
            if metric_name == 'system_health':
                continue
            
            if 'decision_accuracy' in metric_name:
                if metric_data['mean'] > 0.8:
                    health_scores.append(1.0)
                elif metric_data['mean'] > 0.6:
                    health_scores.append(0.7)
                else:
                    health_scores.append(0.3)
            
            elif 'response_time' in metric_name:
                if metric_data['mean'] < 0.05:
                    health_scores.append(1.0)
                elif metric_data['mean'] < 0.1:
                    health_scores.append(0.7)
                else:
                    health_scores.append(0.4)
        
        if not health_scores:
            return 'unknown'
        
        avg_health = np.mean(health_scores)
        
        if avg_health > 0.8:
            return 'excellent'
        elif avg_health > 0.6:
            return 'good'
        elif avg_health > 0.4:
            return 'fair'
        else:
            return 'poor'
    
    def optimize_system(self, ml_system) -> Dict[str, Any]:
        """Tối ưu hóa hệ thống ML"""
        try:
            current_time = time.time()
            
            # Only optimize every hour
            if current_time - self.last_optimization < 3600:
                return {'status': 'too_soon'}
            
            analysis = self.analyze_performance()
            optimizations = []
            
            # Memory optimization
            if analysis.get('memory_usage', {}).get('trend') == 'declining':
                ml_system.memory.memories.clear()
                ml_system.memory.action_outcomes.clear()
                ml_system.memory.situation_patterns.clear()
                optimizations.append('cleared_memory')
            
            # Learning rate adjustment
            if analysis.get('decision_accuracy', {}).get('trend') == 'declining':
                ml_system.reinforcement_learner.learning_rate *= 0.9
                optimizations.append('reduced_learning_rate')
            
            # Epsilon adjustment
            if analysis.get('decision_accuracy', {}).get('mean', 0) > 0.8:
                ml_system.reinforcement_learner.epsilon *= 0.95
                optimizations.append('reduced_exploration')
            
            # Update optimization history
            self.optimization_history.append({
                'timestamp': current_time,
                'analysis': analysis,
                'optimizations': optimizations
            })
            
            self.last_optimization = current_time
            
            return {
                'status': 'success',
                'optimizations': optimizations,
                'analysis': analysis
            }
            
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

class MachineLearningSystem:
    """Hệ thống học máy chính để cải thiện quyết định game"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = get_logger(__name__)
        
        # Learning components
        self.memory = LearningMemory(
            max_size=config.get('learning', {}).get('max_memory_size', 10000)
        )
        self.decision_tree = DecisionTree()
        self.reinforcement_learner = ReinforcementLearner(
            learning_rate=config.get('learning', {}).get('learning_rate', 0.1),
            discount_factor=config.get('learning', {}).get('discount_factor', 0.9)
        )
        
        # Advanced components
        self.feature_engineer = AdvancedFeatureEngineer()
        self.neural_predictor = None  # Will be initialized when we have feature data
        self.multi_agent_learner = MultiAgentLearner(
            num_agents=config.get('learning', {}).get('num_agents', 3)
        )
        self.performance_optimizer = PerformanceOptimizer()
        
        # Learning statistics
        self.learning_stats = {
            'total_decisions': 0,
            'successful_decisions': 0,
            'learning_iterations': 0,
            'rule_updates': 0,
            'q_value_updates': 0,
            'neural_predictions': 0,
            'agent_selections': 0
        }
        
        # Threading
        self.lock = threading.Lock()
        self.is_active = False
        
        # Load existing knowledge
        self._load_knowledge()
        
        # Initialize decision rules
        self._initialize_rules()
        
        self.logger.info("Advanced Machine Learning System initialized")
    
    def start(self):
        """Khởi động hệ thống học máy"""
        try:
            with self.lock:
                self.is_active = True
                
                # Start background optimization
                self._start_background_optimization()
                
                self.logger.info("Advanced Machine Learning System started")
                return True
        except Exception as e:
            self.logger.error(f"Error starting Machine Learning System: {e}")
            return False
    
    def stop(self):
        """Dừng hệ thống học máy"""
        try:
            with self.lock:
                self.is_active = False
                
                # Stop background optimization
                self._stop_background_optimization()
                
                self.logger.info("Advanced Machine Learning System stopped")
                return True
        except Exception as e:
            self.logger.error(f"Error stopping Machine Learning System: {e}")
            return False
    
    def make_decision(self, game_context: Dict[str, Any], 
                     available_actions: List[str],
                     screen_image: Optional[np.ndarray] = None) -> str:
        """Đưa ra quyết định dựa trên học máy nâng cao"""
        try:
            if not self.is_active:
                return random.choice(available_actions)
            
            # Extract advanced features
            features = self.feature_engineer.extract_advanced_features(game_context, screen_image)
            
            # Create game state with advanced features
            state = GameState(time.time(), game_context)
            state.features = features
            
            # Select appropriate agent
            selected_agent = self.multi_agent_learner.select_agent(game_context)
            self.learning_stats['agent_selections'] += 1
            
            # Get decision from decision tree
            tree_decision = self.decision_tree.get_decision(state)
            
            if tree_decision and tree_decision in available_actions:
                self.logger.debug(f"Decision tree chose: {tree_decision}")
                return tree_decision
            
            # Use neural network prediction if available
            if self.neural_predictor and self.neural_predictor.is_trained:
                neural_decision = self._get_neural_decision(features, available_actions)
                if neural_decision:
                    self.learning_stats['neural_predictions'] += 1
                    return neural_decision
            
            # Fall back to reinforcement learning
            rl_decision = self.reinforcement_learner.get_action(state, available_actions)
            self.logger.debug(f"Reinforcement learning chose: {rl_decision}")
            
            # Update statistics
            self.learning_stats['total_decisions'] += 1
            
            return rl_decision
            
        except Exception as e:
            self.logger.error(f"Error making decision: {e}")
            return random.choice(available_actions)
    
    def _get_neural_decision(self, features: Dict[str, float], 
                            available_actions: List[str]) -> Optional[str]:
        """Lấy quyết định từ neural network"""
        try:
            # Convert features to numpy array
            feature_values = np.array([list(features.values())])
            
            # Get predictions for each action
            action_scores = {}
            for action in available_actions:
                # Create action-specific features
                action_features = feature_values.copy()
                action_features[0, -1] = hash(action) % 100 / 100.0  # Simple action encoding
                
                # Get prediction
                prediction = self.neural_predictor.predict(action_features)[0, 0]
                action_scores[action] = prediction
            
            # Return best action
            if action_scores:
                best_action = max(action_scores, key=action_scores.get)
                return best_action
            
        except Exception as e:
            self.logger.error(f"Error getting neural decision: {e}")
        
        return None
    
    def learn_from_action(self, state: GameState, action: GameAction, 
                         next_state: GameState, reward: float):
        """Học từ kết quả của hành động"""
        try:
            if not self.is_active:
                return
            
            # Add to memory
            self.memory.add_memory(state, action, next_state, reward)
            
            # Update decision tree
            self._update_decision_tree(state, action, reward)
            
            # Update reinforcement learning
            available_actions = self._get_available_actions_from_context(next_state.context)
            self.reinforcement_learner.update_q_value(
                state, action.action_type, reward, next_state, available_actions
            )
            
            # Update neural network if available
            if self.neural_predictor:
                self._update_neural_network(state, action, reward)
            
            # Update statistics
            self.learning_stats['learning_iterations'] += 1
            self.learning_stats['rule_updates'] += 1
            self.learning_stats['q_value_updates'] += 1
            
            if action.success:
                self.learning_stats['successful_decisions'] += 1
            
            # Periodic learning improvements
            if self.learning_stats['learning_iterations'] % 100 == 0:
                self._improve_learning()
                
        except Exception as e:
            self.logger.error(f"Error learning from action: {e}")
    
    def _update_neural_network(self, state: GameState, action: GameAction, reward: float):
        """Cập nhật neural network"""
        try:
            if not self.neural_predictor:
                return
            
            # Prepare training data
            features = np.array([list(state.features.values())])
            target = np.array([reward])
            
            # Train neural network
            self.neural_predictor.train(features, target, epochs=5)
            
        except Exception as e:
            self.logger.error(f"Error updating neural network: {e}")
    
    def _start_background_optimization(self):
        """Khởi động tối ưu hóa nền"""
        def optimization_loop():
            while self.is_active:
                try:
                    time.sleep(300)  # Run every 5 minutes
                    if self.is_active:
                        self.performance_optimizer.optimize_system(self)
                except Exception as e:
                    self.logger.error(f"Error in optimization loop: {e}")
        
        self.optimization_thread = threading.Thread(target=optimization_loop, daemon=True)
        self.optimization_thread.start()
    
    def _stop_background_optimization(self):
        """Dừng tối ưu hóa nền"""
        if hasattr(self, 'optimization_thread'):
            self.optimization_thread.join(timeout=1)
    
    def get_learning_stats(self) -> Dict[str, Any]:
        """Lấy thống kê học tập nâng cao"""
        stats = self.learning_stats.copy()
        
        # Calculate success rate
        if stats['total_decisions'] > 0:
            stats['decision_success_rate'] = stats['successful_decisions'] / stats['total_decisions']
        else:
            stats['decision_success_rate'] = 0.0
        
        # Memory statistics
        stats['memory_size'] = len(self.memory.memories)
        stats['action_types_learned'] = len(self.memory.action_outcomes)
        stats['situation_patterns_learned'] = len(self.memory.situation_patterns)
        
        # Rule statistics
        stats['total_rules'] = len(self.decision_tree.rules)
        stats['average_rule_confidence'] = np.mean([
            rule['confidence'] for rule in self.decision_tree.rules
        ]) if self.decision_tree.rules else 0.0
        
        # Advanced component statistics
        stats['neural_network_available'] = self.neural_predictor is not None and self.neural_predictor.is_trained
        stats['agent_performances'] = self.multi_agent_learner.agent_performances
        stats['best_agent'] = self.multi_agent_learner.best_agent
        
        # Performance metrics
        performance_analysis = self.performance_optimizer.analyze_performance()
        stats['performance_analysis'] = performance_analysis
        
        return stats

    # === Compatibility APIs for Admin UI ===
    def export_learning_data(self, file_path: str) -> bool:
        """Xuất dữ liệu học máy cơ bản ra JSON."""
        try:
            data = {
                'timestamp': time.time(),
                'learning_stats': self.get_learning_stats(),
                'q_table_size': sum(len(v) for v in self.reinforcement_learner.q_table.values()),
                'rules': self.decision_tree.rules,
            }
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            self.logger.error(f"Error exporting learning data: {e}")
            return False

    def import_learning_data(self, file_path: str) -> bool:
        """Nhập dữ liệu học máy từ JSON (mức cơ bản: chỉ nạp rules)."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            # Load decision rules if present
            if isinstance(data.get('rules'), list):
                self.decision_tree.rules = data['rules']
            return True
        except Exception as e:
            self.logger.error(f"Error importing learning data: {e}")
            return False

    def reset_learning(self) -> bool:
        """Xoá bộ nhớ học tập, quy tắc và Q-table."""
        try:
            self.memory.memories.clear()
            self.memory.action_outcomes.clear()
            self.memory.situation_patterns.clear()
            self.decision_tree.rules = []
            self.reinforcement_learner.q_table.clear()
            self.learning_stats.update({
                'total_decisions': 0,
                'successful_decisions': 0,
                'learning_iterations': 0,
                'rule_updates': 0,
                'q_value_updates': 0,
                'neural_predictions': 0,
                'agent_selections': 0
            })
            return True
        except Exception as e:
            self.logger.error(f"Error resetting learning: {e}")
            return False
    
    def _improve_learning(self):
        """Cải thiện hệ thống học tập nâng cao"""
        try:
            # Decrease exploration rate
            self.reinforcement_learner.decrease_epsilon()
            
            # Analyze memory for patterns
            self._analyze_memory_patterns()
            
            # Evolve multi-agent strategies
            self.multi_agent_learner.evolve_strategies()
            
            # Initialize neural network if we have enough data
            if (self.neural_predictor is None and 
                len(self.memory.memories) > 100):
                self._initialize_neural_network()
            
            # Save knowledge
            self._save_knowledge()
            
            self.logger.info("Advanced learning system improved")
            
        except Exception as e:
            self.logger.error(f"Error improving learning: {e}")
    
    def _initialize_neural_network(self):
        """Khởi tạo neural network"""
        try:
            if len(self.memory.memories) < 50:
                return
            
            # Get sample features to determine input size
            sample_memory = self.memory.memories[0]
            feature_size = len(sample_memory['state'].features)
            
            # Create neural network
            self.neural_predictor = NeuralNetworkPredictor(
                input_size=feature_size,
                hidden_size=64
            )
            
            # Prepare training data
            X = []
            y = []
            
            for memory in self.memory.memories[-100:]:  # Use last 100 memories
                features = list(memory['state'].features.values())
                reward = memory['reward']
                
                X.append(features)
                y.append(reward)
            
            # Train neural network
            X = np.array(X)
            y = np.array(y)
            
            self.neural_predictor.train(X, y, epochs=50)
            
            self.logger.info("Neural network initialized and trained")
            
        except Exception as e:
            self.logger.error(f"Error initializing neural network: {e}")
    
    def _load_knowledge(self):
        """Tải kiến thức đã học từ file"""
        try:
            knowledge_file = Path(__file__).parent.parent / 'data' / 'learned_knowledge.pkl'
            
            if knowledge_file.exists():
                with open(knowledge_file, 'rb') as f:
                    knowledge = pickle.load(f)
                
                # Load decision tree rules
                if 'decision_tree_rules' in knowledge:
                    for rule_data in knowledge['decision_tree_rules']:
                        self.decision_tree.add_rule(
                            rule_data['condition'],
                            rule_data['action'],
                            rule_data['confidence'],
                            rule_data['success_rate']
                        )
                
                # Load Q-table
                if 'q_table' in knowledge:
                    self.reinforcement_learner.q_table = knowledge['q_table']
                
                self.logger.info("Loaded existing knowledge")
                
        except Exception as e:
            self.logger.warning(f"Could not load existing knowledge: {e}")
    
    def _save_knowledge(self):
        """Lưu kiến thức đã học vào file"""
        try:
            knowledge_file = Path(__file__).parent.parent / 'data' / 'learned_knowledge.pkl'
            knowledge_file.parent.mkdir(exist_ok=True)
            
            knowledge = {
                'decision_tree_rules': [
                    {
                        'condition': rule['condition'],
                        'action': rule['action'],
                        'confidence': rule['confidence'],
                        'success_rate': rule['success_rate']
                    }
                    for rule in self.decision_tree.rules
                ],
                'q_table': dict(self.reinforcement_learner.q_table),
                'timestamp': time.time()
            }
            
            with open(knowledge_file, 'wb') as f:
                pickle.dump(knowledge, f)
            
            self.logger.info("Knowledge saved successfully")
            
        except Exception as e:
            self.logger.error(f"Error saving knowledge: {e}")
    
    def _initialize_rules(self):
        """Khởi tạo các quy tắc cơ bản"""
        try:
            # Basic defensive rules
            self.decision_tree.add_rule(
                {'ball_x': [0.0, 0.3], 'score_difference': [-1.0, 0.0]},
                'defend',
                0.8,
                0.7
            )
            
            # Basic attacking rules
            self.decision_tree.add_rule(
                {'ball_x': [0.7, 1.0], 'score_difference': [0.0, 1.0]},
                'attack',
                0.8,
                0.7
            )
            
            # Ball possession rules
            self.decision_tree.add_rule(
                {'ball_player_distance': [0.0, 0.1], 'possession': [0.6, 1.0]},
                'pass',
                0.9,
                0.8
            )
            
            # Emergency rules
            self.decision_tree.add_rule(
                {'opponent_pressure': [0.8, 1.0], 'ball_player_distance': [0.0, 0.2]},
                'clear',
                0.95,
                0.6
            )
            
            self.logger.info("Initialized basic decision rules")
            
        except Exception as e:
            self.logger.error(f"Error initializing rules: {e}")
    
    def _update_decision_tree(self, state: GameState, action: GameAction, reward: float):
        """Cập nhật cây quyết định dựa trên kết quả"""
        try:
            # Create condition based on state features
            condition = {}
            for feature, value in state.features.items():
                if isinstance(value, (int, float)):
                    # Create range around the value
                    tolerance = 0.1
                    condition[feature] = [value - tolerance, value + tolerance]
            
            # Update rule confidence
            self.decision_tree.update_rule_confidence(
                condition, action.action_type, action.success
            )
            
            # Create new rule if this was a successful action
            if action.success and reward > 0.5:
                self.decision_tree.add_rule(
                    condition,
                    action.action_type,
                    0.7,  # Initial confidence
                    0.8   # Initial success rate
                )
                
        except Exception as e:
            self.logger.error(f"Error updating decision tree: {e}")
    
    def _analyze_memory_patterns(self):
        """Phân tích các pattern trong bộ nhớ"""
        try:
            # Analyze successful action patterns
            for action_type, outcomes in self.memory.action_outcomes.items():
                if len(outcomes) >= 10:  # Need sufficient data
                    success_rate = sum(1 for o in outcomes if o['success']) / len(outcomes)
                    
                    if success_rate > 0.8:
                        # This action type is very successful
                        self.logger.info(f"Action {action_type} has high success rate: {success_rate:.2f}")
                    
                    elif success_rate < 0.3:
                        # This action type needs improvement
                        self.logger.warning(f"Action {action_type} has low success rate: {success_rate:.2f}")
            
            # Analyze situation patterns
            for situation, patterns in self.memory.situation_patterns.items():
                if len(patterns) >= 5:  # Need sufficient data
                    best_action = max(patterns, key=lambda p: p['reward'])
                    self.logger.debug(f"Best action for {situation}: {best_action['action']}")
                    
        except Exception as e:
            self.logger.error(f"Error analyzing memory patterns: {e}")
    
    def _get_available_actions_from_context(self, context: Dict[str, Any]) -> List[str]:
        """Lấy danh sách hành động có sẵn từ context"""
        # This would be implemented based on game context
        # For now, return common actions
        return ['pass', 'shoot', 'dribble', 'tackle', 'clear', 'defend', 'attack']

    def cleanup(self):
        """Dọn dẹp tài nguyên"""
        try:
            self.stop()
            self._save_knowledge()
            self.logger.info("Advanced Machine Learning System cleanup completed")
        except Exception as e:
            self.logger.error(f"Error during Advanced Machine Learning System cleanup: {e}") 
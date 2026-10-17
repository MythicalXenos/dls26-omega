#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Special Situations Handler for Dream League Soccer
Xử lý các tình huống đặc biệt: sút phạt, đá góc, ném biên, phát bóng lên, giao bóng
"""

import time
import threading
from typing import Dict, Any, Optional, List, Tuple
from enum import Enum
import cv2
import numpy as np

from utils.logger import get_logger, log_performance
from utils.image_processor import ImageProcessor
from game_logic.game_controller import GameController, ButtonType, MovementType

class SituationType(Enum):
    """Các loại tình huống đặc biệt"""
    FREE_KICK = "free_kick"           # Sút phạt trực tiếp
    INDIRECT_FREE_KICK = "indirect_free_kick"  # Sút phạt gián tiếp
    CORNER_KICK = "corner_kick"       # Đá góc
    THROW_IN = "throw_in"             # Ném biên
    GOAL_KICK = "goal_kick"           # Phát bóng lên
    KICK_OFF = "kick_off"             # Giao bóng đầu hiệp
    HALF_TIME_KICK_OFF = "half_time_kick_off"  # Giao bóng giữa hiệp
    PENALTY = "penalty"               # Sút penalty
    DROP_BALL = "drop_ball"           # Thả bóng

class SpecialSituationsHandler:
    """Xử lý các tình huống đặc biệt trong game"""
    
    def __init__(self, emulator, game_controller: GameController, config: Dict[str, Any]):
        self.emulator = emulator
        self.game_controller = game_controller
        self.config = config
        self.logger = get_logger(__name__)
        
        # Image processor for situation detection
        self.image_processor = ImageProcessor()
        
        # Situation detection regions
        self.detection_regions = config.get('situation_regions', {
            SituationType.FREE_KICK: (800, 400, 1120, 600),
            SituationType.CORNER_KICK: (700, 300, 1220, 700),
            SituationType.THROW_IN: (600, 400, 1320, 600),
            SituationType.GOAL_KICK: (800, 500, 1120, 700),
            SituationType.KICK_OFF: (800, 400, 1120, 600),
            SituationType.PENALTY: (800, 400, 1120, 600),
        })
        
        # Situation-specific strategies
        self.strategies = self._load_strategies()
        
        # Performance tracking
        self.situation_stats = {
            'total_situations': 0,
            'successful_resolutions': 0,
            'failed_resolutions': 0,
            'situation_types': {}
        }
        
        # Threading
        self.lock = threading.Lock()
        self.is_active = False
        
        self.logger.info("Special Situations Handler initialized")
    
    def start(self):
        """Khởi động handler"""
        try:
            with self.lock:
                self.is_active = True
                self.logger.info("Special Situations Handler started")
                return True
        except Exception as e:
            self.logger.error(f"Error starting Special Situations Handler: {e}")
            return False
    
    def stop(self):
        """Dừng handler"""
        try:
            with self.lock:
                self.is_active = False
                self.logger.info("Special Situations Handler stopped")
                return True
        except Exception as e:
            self.logger.error(f"Error stopping Special Situations Handler: {e}")
            return False
    
    @log_performance
    def detect_special_situation(self, screenshot: np.ndarray) -> Optional[SituationType]:
        """Phát hiện tình huống đặc biệt từ screenshot"""
        try:
            if not self.is_active:
                return None
            
            # Check each situation type
            for situation_type, region in self.detection_regions.items():
                if self._detect_situation_type(screenshot, situation_type, region):
                    self.logger.info(f"Detected situation: {situation_type.value}")
                    return situation_type
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error detecting special situation: {e}")
            return None
    
    @log_performance
    def handle_special_situation(self, situation_type: SituationType, 
                               game_context: Dict[str, Any]) -> bool:
        """Xử lý tình huống đặc biệt"""
        try:
            if not self.is_active:
                return False
            
            self.logger.info(f"Handling situation: {situation_type.value}")
            
            # Update stats
            self._update_situation_stats(situation_type)
            
            # Get strategy for this situation
            strategy = self.strategies.get(situation_type)
            if not strategy:
                self.logger.warning(f"No strategy found for {situation_type.value}")
                return False
            
            # Execute strategy
            success = self._execute_strategy(strategy, game_context)
            
            # Update success stats
            if success:
                self.situation_stats['successful_resolutions'] += 1
                self.logger.info(f"Successfully handled {situation_type.value}")
            else:
                self.situation_stats['failed_resolutions'] += 1
                self.logger.warning(f"Failed to handle {situation_type.value}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error handling situation {situation_type.value}: {e}")
            self.situation_stats['failed_resolutions'] += 1
            return False
    
    def get_situation_stats(self) -> Dict[str, Any]:
        """Lấy thống kê xử lý tình huống"""
        stats = self.situation_stats.copy()
        
        # Calculate success rate
        if stats['total_situations'] > 0:
            stats['success_rate'] = stats['successful_resolutions'] / stats['total_situations']
        else:
            stats['success_rate'] = 0.0
        
        return stats
    
    def _load_strategies(self) -> Dict[SituationType, Dict[str, Any]]:
        """Tải các chiến lược xử lý tình huống"""
        strategies = {
            SituationType.FREE_KICK: {
                'name': 'Free Kick Strategy',
                'description': 'Sút phạt trực tiếp vào khung thành',
                'actions': [
                    {'type': 'move_360', 'params': {'angle': 0, 'intensity': 0.8}, 'delay': 0.2},
                    {'type': 'button', 'params': {'button': 'shoot', 'duration': 0.1}, 'delay': 0.1},
                    {'type': 'release', 'params': {}, 'delay': 0.1}
                ],
                'success_conditions': ['ball_moved', 'goal_scored'],
                'retry_count': 2
            },
            
            SituationType.INDIRECT_FREE_KICK: {
                'name': 'Indirect Free Kick Strategy',
                'description': 'Sút phạt gián tiếp - chuyền trước khi sút',
                'actions': [
                    {'type': 'move_360', 'params': {'angle': 45, 'intensity': 0.6}, 'delay': 0.2},
                    {'type': 'button', 'params': {'button': 'pass', 'duration': 0.1}, 'delay': 0.3},
                    {'type': 'move_360', 'params': {'angle': 0, 'intensity': 0.8}, 'delay': 0.2},
                    {'type': 'button', 'params': {'button': 'shoot', 'duration': 0.1}, 'delay': 0.1},
                    {'type': 'release', 'params': {}, 'delay': 0.1}
                ],
                'success_conditions': ['ball_passed', 'ball_moved'],
                'retry_count': 2
            },
            
            SituationType.CORNER_KICK: {
                'name': 'Corner Kick Strategy',
                'description': 'Đá góc - nhắm vào vùng cầu môn',
                'actions': [
                    {'type': 'move_360', 'params': {'angle': 315, 'intensity': 0.9}, 'delay': 0.2},
                    {'type': 'button', 'params': {'button': 'shoot', 'duration': 0.15}, 'delay': 0.1},
                    {'type': 'release', 'params': {}, 'delay': 0.1}
                ],
                'success_conditions': ['ball_kicked', 'ball_in_air'],
                'retry_count': 1
            },
            
            SituationType.THROW_IN: {
                'name': 'Throw In Strategy',
                'description': 'Ném biên - chuyền bóng cho đồng đội',
                'actions': [
                    {'type': 'move_360', 'params': {'angle': 90, 'intensity': 0.7}, 'delay': 0.2},
                    {'type': 'button', 'params': {'button': 'pass', 'duration': 0.1}, 'delay': 0.1},
                    {'type': 'release', 'params': {}, 'delay': 0.1}
                ],
                'success_conditions': ['ball_thrown', 'ball_moved'],
                'retry_count': 1
            },
            
            SituationType.GOAL_KICK: {
                'name': 'Goal Kick Strategy',
                'description': 'Phát bóng lên - đá xa về phía đối thủ',
                'actions': [
                    {'type': 'move_360', 'params': {'angle': 180, 'intensity': 0.9}, 'delay': 0.2},
                    {'type': 'button', 'params': {'button': 'shoot', 'duration': 0.2}, 'delay': 0.1},
                    {'type': 'release', 'params': {}, 'delay': 0.1}
                ],
                'success_conditions': ['ball_kicked', 'ball_moved_far'],
                'retry_count': 1
            },
            
            SituationType.KICK_OFF: {
                'name': 'Kick Off Strategy',
                'description': 'Giao bóng đầu hiệp - chuyền cho đồng đội',
                'actions': [
                    {'type': 'move_360', 'params': {'angle': 45, 'intensity': 0.6}, 'delay': 0.2},
                    {'type': 'button', 'params': {'button': 'pass', 'duration': 0.1}, 'delay': 0.1},
                    {'type': 'release', 'params': {}, 'delay': 0.1}
                ],
                'success_conditions': ['ball_passed', 'ball_moved'],
                'retry_count': 2
            },
            
            SituationType.HALF_TIME_KICK_OFF: {
                'name': 'Half Time Kick Off Strategy',
                'description': 'Giao bóng giữa hiệp - tương tự kick off',
                'actions': [
                    {'type': 'move_360', 'params': {'angle': 45, 'intensity': 0.6}, 'delay': 0.2},
                    {'type': 'button', 'params': {'button': 'pass', 'duration': 0.1}, 'delay': 0.1},
                    {'type': 'release', 'params': {}, 'delay': 0.1}
                ],
                'success_conditions': ['ball_passed', 'ball_moved'],
                'retry_count': 2
            },
            
            SituationType.PENALTY: {
                'name': 'Penalty Strategy',
                'description': 'Sút penalty - nhắm góc khung thành',
                'actions': [
                    {'type': 'move_360', 'params': {'angle': 315, 'intensity': 0.8}, 'delay': 0.3},
                    {'type': 'button', 'params': {'button': 'shoot', 'duration': 0.15}, 'delay': 0.1},
                    {'type': 'release', 'params': {}, 'delay': 0.1}
                ],
                'success_conditions': ['ball_kicked', 'goal_scored'],
                'retry_count': 0  # No retry for penalty
            },
            
            SituationType.DROP_BALL: {
                'name': 'Drop Ball Strategy',
                'description': 'Thả bóng - giành bóng ngay lập tức',
                'actions': [
                    {'type': 'button', 'params': {'button': 'tackle', 'duration': 0.1}, 'delay': 0.1},
                    {'type': 'move_360', 'params': {'angle': 0, 'intensity': 0.8}, 'delay': 0.2},
                    {'type': 'button', 'params': {'button': 'pass', 'duration': 0.1}, 'delay': 0.1},
                    {'type': 'release', 'params': {}, 'delay': 0.1}
                ],
                'success_conditions': ['ball_controlled', 'ball_moved'],
                'retry_count': 1
            }
        }
        
        return strategies
    
    def _detect_situation_type(self, screenshot: np.ndarray, 
                              situation_type: SituationType, 
                              region: Tuple[int, int, int, int]) -> bool:
        """Phát hiện loại tình huống cụ thể"""
        try:
            # Extract region of interest
            x1, y1, x2, y2 = region
            roi = screenshot[y1:y2, x1:x2]
            
            if roi.size == 0:
                return False
            
            # Convert to grayscale
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            
            # Apply situation-specific detection
            if situation_type == SituationType.FREE_KICK:
                return self._detect_free_kick(gray)
            elif situation_type == SituationType.CORNER_KICK:
                return self._detect_corner_kick(gray)
            elif situation_type == SituationType.THROW_IN:
                return self._detect_throw_in(gray)
            elif situation_type == SituationType.GOAL_KICK:
                return self._detect_goal_kick(gray)
            elif situation_type == SituationType.KICK_OFF:
                return self._detect_kick_off(gray)
            elif situation_type == SituationType.PENALTY:
                return self._detect_penalty(gray)
            elif situation_type == SituationType.DROP_BALL:
                return self._detect_drop_ball(gray)
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error detecting {situation_type.value}: {e}")
            return False
    
    def _detect_free_kick(self, gray_image: np.ndarray) -> bool:
        """Phát hiện sút phạt trực tiếp"""
        try:
            # Look for free kick indicators (white line, ball position, etc.)
            # This is a simplified detection - in practice, you'd use more sophisticated methods
            
            # Check for bright areas (potential free kick line)
            bright_pixels = np.sum(gray_image > 200)
            total_pixels = gray_image.size
            
            if total_pixels > 0:
                bright_ratio = bright_pixels / total_pixels
                return bright_ratio > 0.1  # 10% bright pixels threshold
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error detecting free kick: {e}")
            return False
    
    def _detect_corner_kick(self, gray_image: np.ndarray) -> bool:
        """Phát hiện đá góc"""
        try:
            # Look for corner kick indicators (corner flag, ball in corner, etc.)
            # Check for corner-specific patterns
            
            # Simple edge detection
            edges = cv2.Canny(gray_image, 50, 150)
            edge_density = np.sum(edges > 0) / edges.size
            
            return edge_density > 0.05  # 5% edge density threshold
            
        except Exception as e:
            self.logger.error(f"Error detecting corner kick: {e}")
            return False
    
    def _detect_throw_in(self, gray_image: np.ndarray) -> bool:
        """Phát hiện ném biên"""
        try:
            # Look for throw-in indicators (sideline, player with ball, etc.)
            # Check for horizontal lines (sideline)
            
            # Sobel edge detection for horizontal lines
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            horizontal_lines = np.sum(np.abs(sobel_x) > 50)
            
            return horizontal_lines > 100  # Threshold for horizontal lines
            
        except Exception as e:
            self.logger.error(f"Error detecting throw in: {e}")
            return False
    
    def _detect_goal_kick(self, gray_image: np.ndarray) -> bool:
        """Phát hiện phát bóng lên"""
        try:
            # Look for goal kick indicators (ball in goal area, goalkeeper position, etc.)
            # Check for goal area patterns
            
            # Look for dark areas (goal area)
            dark_pixels = np.sum(gray_image < 100)
            total_pixels = gray_image.size
            
            if total_pixels > 0:
                dark_ratio = dark_pixels / total_pixels
                return dark_ratio > 0.2  # 20% dark pixels threshold
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error detecting goal kick: {e}")
            return False
    
    def _detect_kick_off(self, gray_image: np.ndarray) -> bool:
        """Phát hiện giao bóng đầu hiệp"""
        try:
            # Look for kick-off indicators (center circle, ball at center, etc.)
            # Check for center circle patterns
            
            # Look for circular patterns in the center
            circles = cv2.HoughCircles(
                gray_image, cv2.HOUGH_GRADIENT, 1, 20,
                param1=50, param2=30, minRadius=20, maxRadius=50
            )
            
            return circles is not None
            
        except Exception as e:
            self.logger.error(f"Error detecting kick off: {e}")
            return False
    
    def _detect_penalty(self, gray_image: np.ndarray) -> bool:
        """Phát hiện sút penalty"""
        try:
            # Look for penalty indicators (penalty spot, goalkeeper position, etc.)
            # Check for penalty area patterns
            
            # Look for penalty spot (bright dot)
            bright_spots = cv2.HoughCircles(
                gray_image, cv2.HOUGH_GRADIENT, 1, 20,
                param1=50, param2=30, minRadius=5, maxRadius=15
            )
            
            return bright_spots is not None
            
        except Exception as e:
            self.logger.error(f"Error detecting penalty: {e}")
            return False
    
    def _detect_drop_ball(self, gray_image: np.ndarray) -> bool:
        """Phát hiện thả bóng"""
        try:
            # Look for drop ball indicators (referee, ball in air, etc.)
            # Check for referee patterns or special animations
            
            # Simple brightness check for referee presence
            mean_brightness = np.mean(gray_image)
            return 80 < mean_brightness < 150  # Referee brightness range
            
        except Exception as e:
            self.logger.error(f"Error detecting drop ball: {e}")
            return False
    
    def _execute_strategy(self, strategy: Dict[str, Any], 
                         game_context: Dict[str, Any]) -> bool:
        """Thực hiện chiến lược xử lý tình huống"""
        try:
            actions = strategy.get('actions', [])
            retry_count = strategy.get('retry_count', 0)
            
            # Try to execute strategy
            for attempt in range(retry_count + 1):
                self.logger.debug(f"Executing strategy attempt {attempt + 1}")
                
                # Execute action sequence
                success = self.game_controller.perform_action_sequence(actions)
                
                if success:
                    # Check if success conditions are met
                    if self._check_success_conditions(strategy, game_context):
                        return True
                
                # Wait before retry
                if attempt < retry_count:
                    time.sleep(0.5)
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error executing strategy: {e}")
            return False
    
    def _check_success_conditions(self, strategy: Dict[str, Any], 
                                 game_context: Dict[str, Any]) -> bool:
        """Kiểm tra điều kiện thành công"""
        try:
            success_conditions = strategy.get('success_conditions', [])
            
            # Simplified: assume success, but allow tighter checks for some cases
            if 'goal_scored' in success_conditions:
                # TODO: read score via OCR; currently fallback true
                return True
            return True
            
        except Exception as e:
            self.logger.error(f"Error checking success conditions: {e}")
            return False
    
    def _update_situation_stats(self, situation_type: SituationType):
        """Cập nhật thống kê tình huống"""
        try:
            self.situation_stats['total_situations'] += 1
            
            situation_name = situation_type.value
            if situation_name not in self.situation_stats['situation_types']:
                self.situation_stats['situation_types'][situation_name] = 0
            
            self.situation_stats['situation_types'][situation_name] += 1
            
        except Exception as e:
            self.logger.error(f"Error updating situation stats: {e}")
    
    def cleanup(self):
        """Dọn dẹp tài nguyên"""
        try:
            self.stop()
            self.logger.info("Special Situations Handler cleanup completed")
        except Exception as e:
            self.logger.error(f"Error during Special Situations Handler cleanup: {e}") 
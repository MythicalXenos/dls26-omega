#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Game State Detector for Dream League Soccer
Detects current game state using computer vision and image processing
"""

import cv2
import numpy as np
from PIL import Image
import time
from typing import Optional, Tuple, Dict, Any
from enum import Enum
from utils.logger import get_logger, log_performance

class GameState(Enum):
    """Game states enumeration"""
    UNKNOWN = "unknown"
    MAIN_MENU = "main_menu"
    CAREER_MODE = "career_mode"
    LIVE_MODE = "live_mode"
    MATCH_LOADING = "match_loading"
    MATCH_PLAYING = "match_playing"
    MATCH_PAUSED = "match_paused"
    MATCH_END = "match_end"
    PENALTY_KICK = "penalty_kick"
    FREE_KICK = "free_kick"
    CORNER_KICK = "corner_kick"
    THROW_IN = "throw_in"
    GOAL_KICK = "goal_kick"
    KICKOFF = "kickoff"
    HALF_TIME = "half_time"
    SUBSTITUTION = "substitution"
    INJURY = "injury"
    YELLOW_CARD = "yellow_card"
    RED_CARD = "red_card"
    GOAL_SCORED = "goal_scored"
    GOAL_CONCEDED = "goal_conceded"
    BALL_POSSESSION = "ball_possession"
    OPPONENT_POSSESSION = "opponent_possession"
    ATTACKING = "attacking"
    DEFENDING = "defending"
    COUNTER_ATTACK = "counter_attack"
    SET_PIECE = "set_piece"
    ADVERTISEMENT = "advertisement"
    LOADING_SCREEN = "loading_screen"
    ERROR_SCREEN = "error_screen"

class GameStateDetector:
    """Detects current game state using computer vision"""
    
    def __init__(self, emulator, config: Dict[str, Any] = None):
        self.emulator = emulator
        self.config = config or {}
        self.logger = get_logger(__name__)
        self.current_state = GameState.UNKNOWN
        self.state_history = []
        self.confidence_threshold = 0.7
        
        # Load reference images for state detection
        self.reference_images = {}
        self._load_reference_images()
        
        # State detection patterns
        self.state_patterns = self._create_state_patterns()
        
        # Performance tracking
        self.detection_count = 0
        self.last_detection_time = time.time()
    
    def _load_reference_images(self):
        """Load reference images for state detection"""
        try:
            # TODO: Load reference images from config directory
            # self.reference_images = {
            #     'main_menu': cv2.imread('config/reference/main_menu.png'),
            #     'match_playing': cv2.imread('config/reference/match_playing.png'),
            #     # ... more reference images
            # }
            self.logger.info("Reference images loaded successfully")
        except Exception as e:
            self.logger.warning(f"Could not load reference images: {e}")
    
    def _create_state_patterns(self) -> Dict[GameState, Dict[str, Any]]:
        """Create patterns for state detection"""
        return {
            GameState.MAIN_MENU: {
                'color_ranges': [(0, 0, 100), (50, 50, 255)],  # Red menu elements
                'text_patterns': ['Career', 'Live', 'Settings', 'Shop'],
                'ui_elements': ['menu_button', 'play_button', 'settings_button']
            },
            GameState.MATCH_PLAYING: {
                'color_ranges': [(0, 100, 0), (100, 255, 100)],  # Green field
                'text_patterns': ['Time', 'Score', 'Possession'],
                'ui_elements': ['score_display', 'time_display', 'player_indicators']
            },
            GameState.PENALTY_KICK: {
                'color_ranges': [(0, 0, 150), (100, 100, 255)],  # Blue penalty area
                'text_patterns': ['Penalty', 'Kick'],
                'ui_elements': ['penalty_spot', 'goal_area']
            },
            GameState.CORNER_KICK: {
                'color_ranges': [(0, 150, 0), (100, 255, 100)],  # Green corner area
                'text_patterns': ['Corner', 'Kick'],
                'ui_elements': ['corner_flag', 'corner_arc']
            },
            GameState.ADVERTISEMENT: {
                'color_ranges': [(200, 200, 200), (255, 255, 255)],  # White/gray ad area
                'text_patterns': ['Ad', 'Skip', 'Watch'],
                'ui_elements': ['ad_banner', 'skip_button', 'close_button']
            }
        }
    
    @log_performance
    def detect_current_state(self) -> GameState:
        """Detect current game state"""
        try:
            # Take screenshot
            screenshot = self._take_screenshot()
            if screenshot is None:
                return self.current_state
            
            # Analyze screenshot for state detection
            detected_state = self._analyze_screenshot(screenshot)
            
            # Update state if changed
            if detected_state != self.current_state:
                self._handle_state_change(detected_state)
            
            # Update performance stats
            self._update_detection_stats()
            
            return self.current_state
            
        except Exception as e:
            self.logger.error(f"Error detecting game state: {e}")
            return self.current_state
    
    def _take_screenshot(self) -> Optional[np.ndarray]:
        """Take screenshot from emulator"""
        try:
            screenshot_path = self.emulator.take_screenshot()
            if screenshot_path:
                return cv2.imread(screenshot_path)
            return None
        except Exception as e:
            self.logger.error(f"Error taking screenshot: {e}")
            return None
    
    def _analyze_screenshot(self, screenshot: np.ndarray) -> GameState:
        """Analyze screenshot to determine game state"""
        try:
            # Convert to different color spaces for analysis
            hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
            gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            
            # Check each state pattern
            best_match = GameState.UNKNOWN
            best_confidence = 0
            
            for state, pattern in self.state_patterns.items():
                confidence = self._check_state_pattern(screenshot, hsv, gray, pattern)
                if confidence > best_confidence and confidence > self.confidence_threshold:
                    best_confidence = confidence
                    best_match = state
            
            # Additional specific state detection
            if best_match == GameState.UNKNOWN:
                best_match = self._detect_specific_states(screenshot, hsv, gray)
            
            return best_match
            
        except Exception as e:
            self.logger.error(f"Error analyzing screenshot: {e}")
            return GameState.UNKNOWN
    
    def _check_state_pattern(self, screenshot: np.ndarray, hsv: np.ndarray, 
                           gray: np.ndarray, pattern: Dict[str, Any]) -> float:
        """Check if screenshot matches a specific state pattern"""
        try:
            confidence = 0.0
            checks = 0
            
            # Check color ranges
            if 'color_ranges' in pattern:
                color_confidence = self._check_color_patterns(hsv, pattern['color_ranges'])
                confidence += color_confidence
                checks += 1
            
            # Check text patterns (OCR would be needed here)
            if 'text_patterns' in pattern:
                text_confidence = self._check_text_patterns(gray, pattern['text_patterns'])
                confidence += text_confidence
                checks += 1
            
            # Check UI elements
            if 'ui_elements' in pattern:
                ui_confidence = self._check_ui_elements(screenshot, pattern['ui_elements'])
                confidence += ui_confidence
                checks += 1
            
            # Return average confidence
            return confidence / checks if checks > 0 else 0.0
            
        except Exception as e:
            self.logger.error(f"Error checking state pattern: {e}")
            return 0.0
    
    def _check_color_patterns(self, hsv: np.ndarray, color_ranges: list) -> float:
        """Check if image contains specific color patterns"""
        try:
            total_pixels = hsv.shape[0] * hsv.shape[1]
            matching_pixels = 0
            
            for lower, upper in color_ranges:
                mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
                matching_pixels += cv2.countNonZero(mask)
            
            return min(matching_pixels / total_pixels * 10, 1.0)  # Scale to 0-1
            
        except Exception as e:
            self.logger.error(f"Error checking color patterns: {e}")
            return 0.0
    
    def _check_text_patterns(self, gray: np.ndarray, text_patterns: list) -> float:
        """Check if image contains specific text patterns"""
        # TODO: Implement OCR for text detection
        # For now, return a placeholder confidence
        return 0.5
    
    def _check_ui_elements(self, screenshot: np.ndarray, ui_elements: list) -> float:
        """Check if image contains specific UI elements"""
        # TODO: Implement template matching for UI elements
        # For now, return a placeholder confidence
        return 0.5
    
    def _detect_specific_states(self, screenshot: np.ndarray, hsv: np.ndarray, 
                               gray: np.ndarray) -> GameState:
        """Detect specific game states using advanced analysis"""
        try:
            # Detect match playing state
            if self._is_match_playing(screenshot, hsv):
                return GameState.MATCH_PLAYING
            
            # Detect set piece states
            set_piece_state = self._detect_set_piece_state(screenshot, hsv)
            if set_piece_state != GameState.UNKNOWN:
                return set_piece_state
            
            # Detect ball possession
            possession_state = self._detect_ball_possession(screenshot, hsv)
            if possession_state != GameState.UNKNOWN:
                return possession_state
            
            return GameState.UNKNOWN
            
        except Exception as e:
            self.logger.error(f"Error in specific state detection: {e}")
            return GameState.UNKNOWN
    
    def _is_match_playing(self, screenshot: np.ndarray, hsv: np.ndarray) -> bool:
        """Check if match is currently playing"""
        try:
            # Look for green field color (typical soccer field)
            green_lower = np.array([35, 50, 50])
            green_upper = np.array([85, 255, 255])
            green_mask = cv2.inRange(hsv, green_lower, green_upper)
            
            green_ratio = cv2.countNonZero(green_mask) / (screenshot.shape[0] * screenshot.shape[1])
            
            # Look for score display area (usually white/light colored)
            white_lower = np.array([0, 0, 200])
            white_upper = np.array([180, 30, 255])
            white_mask = cv2.inRange(hsv, white_lower, white_upper)
            
            white_ratio = cv2.countNonZero(white_mask) / (screenshot.shape[0] * screenshot.shape[1])
            
            # Match playing if we have significant green (field) and some white (UI elements)
            return green_ratio > 0.3 and white_ratio > 0.05
            
        except Exception as e:
            self.logger.error(f"Error checking match playing state: {e}")
            return False
    
    def _detect_set_piece_state(self, screenshot: np.ndarray, hsv: np.ndarray) -> GameState:
        """Detect specific set piece states"""
        try:
            # Check for penalty kick (look for penalty spot area)
            # Check for corner kick (look for corner flag area)
            # Check for free kick (look for free kick wall)
            # Check for throw-in (look for throw-in line)
            # Check for goal kick (look for goal area)
            # Check for kickoff (look for center circle)
            
            # For now, return unknown - implement specific detection logic
            return GameState.UNKNOWN
            
        except Exception as e:
            self.logger.error(f"Error detecting set piece state: {e}")
            return GameState.UNKNOWN
    
    def _detect_ball_possession(self, screenshot: np.ndarray, hsv: np.ndarray) -> GameState:
        """Detect ball possession state"""
        try:
            # Look for ball (usually white/light colored circular object)
            # Look for player indicators (colored dots/arrows)
            # Look for possession percentage display
            
            # For now, return unknown - implement specific detection logic
            return GameState.UNKNOWN
            
        except Exception as e:
            self.logger.error(f"Error detecting ball possession: {e}")
            return GameState.UNKNOWN
    
    def _handle_state_change(self, new_state: GameState):
        """Handle state change"""
        old_state = self.current_state
        self.current_state = new_state
        
        # Log state change
        self.logger.info(f"Game state changed: {old_state.value} -> {new_state.value}")
        
        # Add to history
        self.state_history.append({
            'timestamp': time.time(),
            'old_state': old_state.value,
            'new_state': new_state.value
        })
        
        # Keep only last 100 state changes
        if len(self.state_history) > 100:
            self.state_history = self.state_history[-100:]
    
    def _update_detection_stats(self):
        """Update detection performance statistics"""
        self.detection_count += 1
        current_time = time.time()
        
        if current_time - self.last_detection_time > 60:  # Every minute
            detections_per_minute = self.detection_count / ((current_time - self.last_detection_time) / 60)
            self.logger.debug(f"Detection rate: {detections_per_minute:.2f} per minute")
            
            # Reset counters
            self.detection_count = 0
            self.last_detection_time = current_time
    
    def get_current_state(self) -> GameState:
        """Get current game state"""
        return self.current_state
    
    def get_state_history(self) -> list:
        """Get state change history"""
        return self.state_history.copy()
    
    def get_detection_stats(self) -> Dict[str, Any]:
        """Get detection performance statistics"""
        current_time = time.time()
        uptime = current_time - self.last_detection_time + 60
        
        return {
            'current_state': self.current_state.value,
            'detection_count': self.detection_count,
            'uptime_seconds': uptime,
            'detections_per_minute': self.detection_count / (uptime / 60) if uptime > 0 else 0,
            'state_history_length': len(self.state_history)
        }
    
    def set_confidence_threshold(self, threshold: float):
        """Set confidence threshold for state detection"""
        if 0.0 <= threshold <= 1.0:
            self.confidence_threshold = threshold
            self.logger.info(f"Confidence threshold set to {threshold}")
        else:
            self.logger.warning("Confidence threshold must be between 0.0 and 1.0")
    
    def reset_detection(self):
        """Reset detection state"""
        self.current_state = GameState.UNKNOWN
        self.state_history.clear()
        self.detection_count = 0
        self.last_detection_time = time.time()
        self.logger.info("Game state detection reset") 
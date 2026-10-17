#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advertisement Handler for Dream League Soccer
Xử lý quảng cáo tự động khi xuất hiện trong game
"""

import time
import threading
from typing import Dict, Any, Optional, List, Tuple
from enum import Enum
import cv2
import numpy as np

from utils.logger import get_logger, log_performance
from utils.image_processor import ImageProcessor

class AdType(Enum):
    """Các loại quảng cáo trong game"""
    REWARD_AD = "reward_ad"           # Quảng cáo thưởng
    INTERSTITIAL_AD = "interstitial_ad"  # Quảng cáo toàn màn hình
    BANNER_AD = "banner_ad"           # Quảng cáo banner
    SKIP_AD = "skip_ad"               # Quảng cáo có thể bỏ qua
    FORCED_AD = "forced_ad"           # Quảng cáo bắt buộc xem

class AdHandler:
    """Xử lý quảng cáo tự động trong game"""
    
    def __init__(self, emulator, config: Dict[str, Any]):
        self.emulator = emulator
        self.config = config
        self.logger = get_logger(__name__)
        
        # Image processor for ad detection
        self.image_processor = ImageProcessor()
        
        # Ad detection configurations
        self.ad_config = config.get('ad_handler', {})
        
        # Ad detection regions and patterns
        self.detection_regions = self.ad_config.get('detection_regions', {
            'reward_ad': (400, 200, 1520, 800),
            'interstitial_ad': (0, 0, 1920, 1080),
            'banner_ad': (0, 900, 1920, 1080),
            'skip_ad': (1600, 50, 1900, 150),
            'forced_ad': (0, 0, 1920, 1080)
        })
        
        # Ad handling strategies
        self.ad_strategies = self._load_ad_strategies()
        
        # Ad statistics
        self.ad_stats = {
            'total_ads_detected': 0,
            'ads_handled': 0,
            'ads_skipped': 0,
            'ads_watched': 0,
            'ad_types': {},
            'rewards_earned': 0,
            'total_time_spent': 0
        }
        
        # Threading
        self.lock = threading.Lock()
        self.is_active = False
        self.current_ad = None
        
        # Ad detection patterns
        self.ad_patterns = self._load_ad_patterns()
        
        self.logger.info("Advertisement Handler initialized")
    
    def start(self):
        """Khởi động handler"""
        try:
            with self.lock:
                self.is_active = True
                self.logger.info("Advertisement Handler started")
                return True
        except Exception as e:
            self.logger.error(f"Error starting Advertisement Handler: {e}")
            return False
    
    def stop(self):
        """Dừng handler"""
        try:
            with self.lock:
                self.is_active = False
                self.current_ad = None
                self.logger.info("Advertisement Handler stopped")
                return True
        except Exception as e:
            self.logger.error(f"Error stopping Advertisement Handler: {e}")
            return False
    
    @log_performance
    def detect_advertisement(self, screenshot: np.ndarray) -> Optional[AdType]:
        """Phát hiện quảng cáo từ screenshot"""
        try:
            if not self.is_active:
                return None
            
            # Check each ad type
            for ad_type, region in self.detection_regions.items():
                if self._detect_ad_type(screenshot, ad_type, region):
                    self.logger.info(f"Detected advertisement: {ad_type}")
                    return AdType(ad_type)
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error detecting advertisement: {e}")
            return None
    
    @log_performance
    def handle_advertisement(self, ad_type: AdType, 
                           game_context: Dict[str, Any]) -> bool:
        """Xử lý quảng cáo đã phát hiện"""
        try:
            if not self.is_active:
                return False
            
            self.logger.info(f"Handling advertisement: {ad_type.value}")
            
            # Update stats
            self._update_ad_stats(ad_type)
            
            # Get strategy for this ad type
            strategy = self.ad_strategies.get(ad_type)
            if not strategy:
                self.logger.warning(f"No strategy found for {ad_type.value}")
                return False
            
            # Set current ad
            with self.lock:
                self.current_ad = ad_type
            
            # Execute ad handling strategy
            success = self._execute_ad_strategy(strategy, game_context)
            
            # Update success stats
            if success:
                self.ad_stats['ads_handled'] += 1
                self.logger.info(f"Successfully handled {ad_type.value}")
            else:
                self.logger.warning(f"Failed to handle {ad_type.value}")
            
            # Clear current ad
            with self.lock:
                self.current_ad = None
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error handling advertisement {ad_type.value}: {e}")
            with self.lock:
                self.current_ad = None
            return False
    
    def is_ad_playing(self) -> bool:
        """Kiểm tra xem có quảng cáo đang chạy không"""
        with self.lock:
            return self.current_ad is not None
    
    def get_current_ad(self) -> Optional[AdType]:
        """Lấy loại quảng cáo hiện tại"""
        with self.lock:
            return self.current_ad
    
    def get_ad_stats(self) -> Dict[str, Any]:
        """Lấy thống kê xử lý quảng cáo"""
        stats = self.ad_stats.copy()
        
        # Calculate success rate
        if stats['total_ads_detected'] > 0:
            stats['handling_success_rate'] = stats['ads_handled'] / stats['total_ads_detected']
        else:
            stats['handling_success_rate'] = 0.0
        
        return stats
    
    def _load_ad_strategies(self) -> Dict[AdType, Dict[str, Any]]:
        """Tải các chiến lược xử lý quảng cáo"""
        strategies = {
            AdType.REWARD_AD: {
                'name': 'Reward Ad Strategy',
                'description': 'Xem quảng cáo để nhận thưởng',
                'actions': [
                    {'type': 'wait', 'params': {'duration': 2.0}, 'description': 'Chờ quảng cáo load'},
                    {'type': 'click', 'params': {'x': 960, 'y': 540}, 'description': 'Click vào quảng cáo'},
                    {'type': 'wait', 'params': {'duration': 30.0}, 'description': 'Chờ quảng cáo kết thúc'},
                    {'type': 'click', 'params': {'x': 960, 'y': 800}, 'description': 'Click nút nhận thưởng'},
                    {'type': 'wait', 'params': {'duration': 1.0}, 'description': 'Chờ xử lý thưởng'}
                ],
                'expected_reward': 'coins_or_diamonds',
                'skip_available': False,
                'timeout': 60
            },
            
            AdType.INTERSTITIAL_AD: {
                'name': 'Interstitial Ad Strategy',
                'description': 'Xử lý quảng cáo toàn màn hình',
                'actions': [
                    {'type': 'wait', 'params': {'duration': 1.0}, 'description': 'Chờ quảng cáo load'},
                    {'type': 'wait', 'params': {'duration': 25.0}, 'description': 'Chờ quảng cáo tự kết thúc'},
                    {'type': 'click', 'params': {'x': 960, 'y': 800}, 'description': 'Click nút đóng nếu cần'}
                ],
                'expected_reward': 'none',
                'skip_available': False,
                'timeout': 45
            },
            
            AdType.BANNER_AD: {
                'name': 'Banner Ad Strategy',
                'description': 'Xử lý quảng cáo banner',
                'actions': [
                    {'type': 'wait', 'params': {'duration': 0.5}, 'description': 'Chờ banner load'},
                    {'type': 'click', 'params': {'x': 960, 'y': 950}, 'description': 'Click vào banner nếu cần'}
                ],
                'expected_reward': 'none',
                'skip_available': True,
                'timeout': 10
            },
            
            AdType.SKIP_AD: {
                'name': 'Skip Ad Strategy',
                'description': 'Bỏ qua quảng cáo có thể bỏ qua',
                'actions': [
                    {'type': 'wait', 'params': {'duration': 1.0}, 'description': 'Chờ nút skip xuất hiện'},
                    {'type': 'click', 'params': {'x': 1750, 'y': 100}, 'description': 'Click nút skip'},
                    {'type': 'wait', 'params': {'duration': 0.5}, 'description': 'Chờ xử lý'}
                ],
                'expected_reward': 'none',
                'skip_available': True,
                'timeout': 15
            },
            
            AdType.FORCED_AD: {
                'name': 'Forced Ad Strategy',
                'description': 'Xử lý quảng cáo bắt buộc',
                'actions': [
                    {'type': 'wait', 'params': {'duration': 1.0}, 'description': 'Chờ quảng cáo load'},
                    {'type': 'wait', 'params': {'duration': 30.0}, 'description': 'Chờ quảng cáo kết thúc'},
                    {'type': 'click', 'params': {'x': 960, 'y': 800}, 'description': 'Click nút tiếp tục'}
                ],
                'expected_reward': 'none',
                'skip_available': False,
                'timeout': 60
            }
        }
        
        return strategies
    
    def _load_ad_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Tải các mẫu nhận dạng quảng cáo"""
        patterns = {
            'reward_ad': {
                'color_patterns': [
                    {'color': (255, 215, 0), 'threshold': 0.1},  # Gold color
                    {'color': (255, 255, 255), 'threshold': 0.2}  # White text
                ],
                'text_patterns': ['REWARD', 'WATCH', 'GET', 'FREE'],
                'button_patterns': ['CLAIM', 'COLLECT', 'GET REWARD']
            },
            
            'interstitial_ad': {
                'color_patterns': [
                    {'color': (0, 0, 0), 'threshold': 0.3},      # Black background
                    {'color': (255, 255, 255), 'threshold': 0.1}  # White elements
                ],
                'text_patterns': ['ADVERTISEMENT', 'AD', 'SPONSORED'],
                'button_patterns': ['CLOSE', 'CONTINUE', 'SKIP']
            },
            
            'banner_ad': {
                'color_patterns': [
                    {'color': (200, 200, 200), 'threshold': 0.15},  # Gray banner
                    {'color': (255, 255, 255), 'threshold': 0.1}    # White text
                ],
                'text_patterns': ['ADVERTISEMENT', 'SPONSORED'],
                'button_patterns': ['CLOSE', 'X']
            },
            
            'skip_ad': {
                'color_patterns': [
                    {'color': (255, 255, 255), 'threshold': 0.05},  # White skip button
                    {'color': (0, 0, 0), 'threshold': 0.1}          # Black text
                ],
                'text_patterns': ['SKIP', 'SKIP AD', 'SKIP IN'],
                'button_patterns': ['SKIP', 'SKIP AD']
            },
            
            'forced_ad': {
                'color_patterns': [
                    {'color': (0, 0, 0), 'threshold': 0.4},        # Black overlay
                    {'color': (255, 255, 255), 'threshold': 0.05}   # White elements
                ],
                'text_patterns': ['ADVERTISEMENT', 'AD', 'SPONSORED'],
                'button_patterns': ['CONTINUE', 'NEXT', 'CLOSE']
            }
        }
        
        return patterns
    
    def _detect_ad_type(self, screenshot: np.ndarray, 
                        ad_type: str, 
                        region: Tuple[int, int, int, int]) -> bool:
        """Phát hiện loại quảng cáo cụ thể"""
        try:
            # Extract region of interest
            x1, y1, x2, y2 = region
            roi = screenshot[y1:y2, x1:x2]
            
            if roi.size == 0:
                return False
            
            # Get patterns for this ad type
            patterns = self.ad_patterns.get(ad_type, {})
            
            # Check color patterns
            if not self._check_color_patterns(roi, patterns.get('color_patterns', [])):
                return False
            
            # Check text patterns (OCR would be used here in practice)
            if not self._check_text_patterns(roi, patterns.get('text_patterns', [])):
                return False
            
            # Check button patterns
            if not self._check_button_patterns(roi, patterns.get('button_patterns', [])):
                return False
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error detecting {ad_type}: {e}")
            return False
    
    def _check_color_patterns(self, image: np.ndarray, 
                             color_patterns: List[Dict[str, Any]]) -> bool:
        """Kiểm tra mẫu màu sắc"""
        try:
            for pattern in color_patterns:
                color = pattern['color']
                threshold = pattern['threshold']
                
                # Convert BGR to RGB for comparison
                target_color = (color[2], color[1], color[0])
                
                # Count pixels matching the color (with tolerance)
                tolerance = 30
                lower_bound = np.array([max(0, c - tolerance) for c in target_color])
                upper_bound = np.array([min(255, c + tolerance) for c in target_color])
                
                mask = cv2.inRange(image, lower_bound, upper_bound)
                matching_pixels = np.sum(mask > 0)
                total_pixels = image.shape[0] * image.shape[1]
                
                if total_pixels > 0:
                    color_ratio = matching_pixels / total_pixels
                    if color_ratio >= threshold:
                        return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error checking color patterns: {e}")
            return False
    
    def _check_text_patterns(self, image: np.ndarray, 
                            text_patterns: List[str]) -> bool:
        """Kiểm tra mẫu văn bản (simplified)"""
        try:
            # In practice, you would use OCR here
            # For now, we'll use a simplified approach based on edge density
            
            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Apply edge detection
            edges = cv2.Canny(gray, 50, 150)
            edge_density = np.sum(edges > 0) / edges.size
            
            # High edge density often indicates text
            return edge_density > 0.08  # 8% edge density threshold
            
        except Exception as e:
            self.logger.error(f"Error checking text patterns: {e}")
            return False
    
    def _check_button_patterns(self, image: np.ndarray, 
                              button_patterns: List[str]) -> bool:
        """Kiểm tra mẫu nút (simplified)"""
        try:
            # In practice, you would use template matching or OCR
            # For now, we'll use a simplified approach based on rectangular shapes
            
            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Find contours (potential buttons)
            _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Look for rectangular contours (potential buttons)
            for contour in contours:
                if len(contour) >= 4:
                    # Approximate contour to polygon
                    epsilon = 0.02 * cv2.arcLength(contour, True)
                    approx = cv2.approxPolyDP(contour, epsilon, True)
                    
                    # Check if it's roughly rectangular
                    if len(approx) == 4:
                        return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error checking button patterns: {e}")
            return False
    
    def _execute_ad_strategy(self, strategy: Dict[str, Any], 
                            game_context: Dict[str, Any]) -> bool:
        """Thực hiện chiến lược xử lý quảng cáo"""
        try:
            actions = strategy.get('actions', [])
            timeout = strategy.get('timeout', 30)
            
            start_time = time.time()
            
            # Execute action sequence
            for action in actions:
                # Check timeout
                if time.time() - start_time > timeout:
                    self.logger.warning(f"Ad handling timeout after {timeout}s")
                    return False
                
                # Execute action
                success = self._execute_ad_action(action)
                if not success:
                    self.logger.warning(f"Failed to execute action: {action}")
                    continue
                
                # Wait for action delay
                delay = action.get('delay', 0.1)
                if delay > 0:
                    time.sleep(delay)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error executing ad strategy: {e}")
            return False
    
    def _execute_ad_action(self, action: Dict[str, Any]) -> bool:
        """Thực hiện một hành động xử lý quảng cáo"""
        try:
            action_type = action.get('type')
            params = action.get('params', {})
            
            if action_type == 'wait':
                duration = params.get('duration', 1.0)
                time.sleep(duration)
                return True
                
            elif action_type == 'click':
                x = params.get('x', 960)
                y = params.get('y', 540)
                return self.emulator.click(x, y)
                
            elif action_type == 'swipe':
                start_x = params.get('start_x', 960)
                start_y = params.get('start_y', 540)
                end_x = params.get('end_x', 960)
                end_y = params.get('end_y', 400)
                return self.emulator.swipe(start_x, start_y, end_x, end_y)
                
            elif action_type == 'key_press':
                key = params.get('key', 'BACK')
                return self.emulator.press_key(key)
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error executing ad action: {e}")
            return False
    
    def _update_ad_stats(self, ad_type: AdType):
        """Cập nhật thống kê quảng cáo"""
        try:
            self.ad_stats['total_ads_detected'] += 1
            
            ad_name = ad_type.value
            if ad_name not in self.ad_stats['ad_types']:
                self.ad_stats['ad_types'][ad_name] = 0
            
            self.ad_stats['ad_types'][ad_name] += 1
            
        except Exception as e:
            self.logger.error(f"Error updating ad stats: {e}")
    
    def cleanup(self):
        """Dọn dẹp tài nguyên"""
        try:
            self.stop()
            self.logger.info("Advertisement Handler cleanup completed")
        except Exception as e:
            self.logger.error(f"Error during Advertisement Handler cleanup: {e}") 

# Compatibility adapter for Admin UI
class AdvertisementHandler:
    """Adapter đơn giản để tương thích với AdminInterface.
    Không thao tác emulator; chỉ cung cấp get_ad_stats().
    """
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self._stats = {
            'total_ads_detected': 0,
            'ads_handled': 0,
            'ads_skipped': 0,
            'ads_watched': 0,
            'ad_types': {},
            'rewards_earned': 0,
            'total_time_spent': 0,
            'handling_success_rate': 0.0
        }
    
    def get_ad_stats(self) -> Dict[str, Any]:
        return self._stats.copy()
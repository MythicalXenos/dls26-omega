#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Game Controller for Dream League Soccer
Điều khiển game với các nút A, B, C và skill, hỗ trợ di chuyển 360 độ
"""

import time
import math
import threading
from typing import Dict, Any, Tuple, Optional, List
from enum import Enum
import cv2
import numpy as np

from utils.logger import get_logger, log_performance
from utils.image_processor import ImageProcessor

class ButtonType(Enum):
    """Các loại nút trong game"""
    A = "pass"           # Chuyền bóng
    B = "shoot"          # Sút bóng
    C = "skill"          # Kỹ năng
    SPRINT = "sprint"    # Chạy nhanh
    TACKLE = "tackle"    # Xoạc bóng
    SWITCH = "switch"    # Đổi cầu thủ

class MovementType(Enum):
    """Các loại di chuyển"""
    IDLE = "idle"
    FORWARD = "forward"
    BACKWARD = "backward"
    LEFT = "left"
    RIGHT = "right"
    FORWARD_LEFT = "forward_left"
    FORWARD_RIGHT = "forward_right"
    BACKWARD_LEFT = "backward_left"
    BACKWARD_RIGHT = "backward_right"

class GameController:
    """Điều khiển game DLS với các nút và di chuyển"""
    
    def __init__(self, emulator, config: Dict[str, Any]):
        self.emulator = emulator
        self.config = config
        self.logger = get_logger(__name__)
        
        # Button positions (relative to screen)
        self.button_positions = config.get('button_positions', {
            ButtonType.A: (1600, 800),      # Pass button
            ButtonType.B: (1750, 800),      # Shoot button
            ButtonType.C: (1450, 800),      # Skill button
            ButtonType.SPRINT: (1500, 700), # Sprint button
            ButtonType.TACKLE: (1300, 800), # Tackle button
            ButtonType.SWITCH: (1400, 700), # Switch player button
        })
        
        # Joystick center position
        self.joystick_center = config.get('joystick_center', (960, 800))
        self.joystick_radius = config.get('joystick_radius', 100)
        
        # Control settings
        self.button_delay = config.get('button_delay', 0.1)
        self.movement_sensitivity = config.get('movement_sensitivity', 1.0)
        self.auto_press_duration = config.get('auto_press_duration', 0.05)
        
        # State tracking
        self.current_movement = MovementType.IDLE
        self.last_button_press = {}
        self.button_cooldowns = {}
        
        # Threading
        self.lock = threading.Lock()
        self.is_active = False
        
        # Image processor for button detection
        self.image_processor = ImageProcessor()
        
        self.logger.info("Game Controller initialized")
    
    def start(self):
        """Khởi động game controller"""
        try:
            with self.lock:
                self.is_active = True
                self.logger.info("Game Controller started")
                return True
        except Exception as e:
            self.logger.error(f"Error starting Game Controller: {e}")
            return False
    
    def stop(self):
        """Dừng game controller"""
        try:
            with self.lock:
                self.is_active = False
                self.logger.info("Game Controller stopped")
                return True
        except Exception as e:
            self.logger.error(f"Error stopping Game Controller: {e}")
            return False
    
    @log_performance
    def press_button(self, button_type: ButtonType, duration: float = None) -> bool:
        """Nhấn nút trong game"""
        try:
            if not self.is_active:
                return False
            
            if duration is None:
                duration = self.auto_press_duration
            
            # Check cooldown
            if self._is_button_on_cooldown(button_type):
                self.logger.debug(f"Button {button_type.value} is on cooldown")
                return False
            
            # Get button position
            position = self.button_positions.get(button_type)
            if not position:
                self.logger.error(f"Unknown button type: {button_type}")
                return False
            
            # Press button
            success = self.emulator.click_at(position[0], position[1], duration)
            
            if success:
                self._update_button_state(button_type)
                self.logger.debug(f"Pressed button {button_type.value} at {position}")
            else:
                self.logger.warning(f"Failed to press button {button_type.value}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error pressing button {button_type.value}: {e}")
            return False
    
    @log_performance
    def move_joystick(self, direction: MovementType, intensity: float = 1.0) -> bool:
        """Di chuyển joystick theo hướng và cường độ"""
        try:
            if not self.is_active:
                return False
            
            # Calculate target position based on direction and intensity
            target_pos = self._calculate_joystick_position(direction, intensity)
            
            # Move joystick
            success = self.emulator.drag_to(
                self.joystick_center[0], self.joystick_center[1],
                target_pos[0], target_pos[1],
                duration=0.1
            )
            
            if success:
                self.current_movement = direction
                self.logger.debug(f"Moved joystick to {direction.value} with intensity {intensity}")
            else:
                self.logger.warning(f"Failed to move joystick to {direction.value}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error moving joystick to {direction.value}: {e}")
            return False
    
    @log_performance
    def move_joystick_360(self, angle: float, intensity: float = 1.0) -> bool:
        """Di chuyển joystick theo góc 360 độ"""
        try:
            if not self.is_active:
                return False
            
            # Convert angle to radians
            angle_rad = math.radians(angle)
            
            # Calculate target position
            dx = math.cos(angle_rad) * self.joystick_radius * intensity
            dy = math.sin(angle_rad) * self.joystick_radius * intensity
            
            target_x = int(self.joystick_center[0] + dx)
            target_y = int(self.joystick_center[1] + dy)
            
            # Move joystick
            success = self.emulator.drag_to(
                self.joystick_center[0], self.joystick_center[1],
                target_x, target_y,
                duration=0.1
            )
            
            if success:
                self.logger.debug(f"Moved joystick to angle {angle}° with intensity {intensity}")
            else:
                self.logger.warning(f"Failed to move joystick to angle {angle}°")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error moving joystick to angle {angle}°: {e}")
            return False
    
    @log_performance
    def release_joystick(self) -> bool:
        """Thả joystick về vị trí trung tâm"""
        try:
            if not self.is_active:
                return False
            
            # Release joystick (return to center)
            success = self.emulator.click_at(
                self.joystick_center[0], self.joystick_center[1],
                duration=0.05
            )
            
            if success:
                self.current_movement = MovementType.IDLE
                self.logger.debug("Released joystick")
            else:
                self.logger.warning("Failed to release joystick")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error releasing joystick: {e}")
            return False
    
    @log_performance
    def perform_action_sequence(self, actions: List[Dict[str, Any]]) -> bool:
        """Thực hiện chuỗi hành động"""
        try:
            if not self.is_active:
                return False
            
            success_count = 0
            total_actions = len(actions)
            
            for action in actions:
                action_type = action.get('type')
                params = action.get('params', {})
                delay = action.get('delay', self.button_delay)
                
                success = False
                
                if action_type == 'button':
                    button = ButtonType(params.get('button'))
                    duration = params.get('duration', self.auto_press_duration)
                    success = self.press_button(button, duration)
                    
                elif action_type == 'move':
                    direction = MovementType(params.get('direction'))
                    intensity = params.get('intensity', 1.0)
                    success = self.move_joystick(direction, intensity)
                    
                elif action_type == 'move_360':
                    angle = params.get('angle', 0)
                    intensity = params.get('intensity', 1.0)
                    success = self.move_joystick_360(angle, intensity)
                    
                elif action_type == 'release':
                    success = self.release_joystick()
                
                if success:
                    success_count += 1
                
                # Wait between actions
                if delay > 0:
                    time.sleep(delay)
            
            success_rate = success_count / total_actions if total_actions > 0 else 0
            self.logger.info(f"Action sequence completed: {success_count}/{total_actions} ({success_rate:.1%})")
            
            return success_rate >= 0.8  # 80% success rate threshold
            
        except Exception as e:
            self.logger.error(f"Error performing action sequence: {e}")
            return False
    
    @log_performance
    def detect_button_state(self, button_type: ButtonType) -> Dict[str, Any]:
        """Phát hiện trạng thái nút (có thể nhấn hay không)"""
        try:
            if not self.is_active:
                return {'detectable': False, 'state': 'unknown'}
            
            # Get button position
            position = self.button_positions.get(button_type)
            if not position:
                return {'detectable': False, 'state': 'unknown'}
            
            # Take screenshot around button area
            button_region = (
                position[0] - 20, position[1] - 20,
                position[0] + 20, position[1] + 20
            )
            
            screenshot = self.emulator.take_screenshot(button_region)
            if screenshot is None:
                return {'detectable': False, 'state': 'unknown'}
            
            # Analyze button state using image processing
            button_state = self._analyze_button_image(screenshot, button_type)
            
            return {
                'detectable': True,
                'state': button_state,
                'position': position,
                'region': button_region
            }
            
        except Exception as e:
            self.logger.error(f"Error detecting button state for {button_type.value}: {e}")
            return {'detectable': False, 'state': 'unknown'}
    
    def get_available_buttons(self) -> List[ButtonType]:
        """Lấy danh sách các nút có thể sử dụng"""
        return list(self.button_positions.keys())
    
    def get_current_movement(self) -> MovementType:
        """Lấy trạng thái di chuyển hiện tại"""
        return self.current_movement
    
    def is_button_available(self, button_type: ButtonType) -> bool:
        """Kiểm tra nút có sẵn sàng không"""
        return not self._is_button_on_cooldown(button_type)
    
    def _calculate_joystick_position(self, direction: MovementType, intensity: float) -> Tuple[int, int]:
        """Tính toán vị trí joystick dựa trên hướng và cường độ"""
        # Normalize intensity
        intensity = max(0.0, min(1.0, intensity))
        
        # Calculate offset based on direction
        if direction == MovementType.FORWARD:
            dx, dy = 0, -self.joystick_radius * intensity
        elif direction == MovementType.BACKWARD:
            dx, dy = 0, self.joystick_radius * intensity
        elif direction == MovementType.LEFT:
            dx, dy = -self.joystick_radius * intensity, 0
        elif direction == MovementType.RIGHT:
            dx, dy = self.joystick_radius * intensity, 0
        elif direction == MovementType.FORWARD_LEFT:
            dx = -self.joystick_radius * intensity * 0.707
            dy = -self.joystick_radius * intensity * 0.707
        elif direction == MovementType.FORWARD_RIGHT:
            dx = self.joystick_radius * intensity * 0.707
            dy = -self.joystick_radius * intensity * 0.707
        elif direction == MovementType.BACKWARD_LEFT:
            dx = -self.joystick_radius * intensity * 0.707
            dy = self.joystick_radius * intensity * 0.707
        elif direction == MovementType.BACKWARD_RIGHT:
            dx = self.joystick_radius * intensity * 0.707
            dy = self.joystick_radius * intensity * 0.707
        else:  # IDLE
            dx, dy = 0, 0
        
        target_x = int(self.joystick_center[0] + dx)
        target_y = int(self.joystick_center[1] + dy)
        
        return target_x, target_y
    
    def _is_button_on_cooldown(self, button_type: ButtonType) -> bool:
        """Kiểm tra nút có đang trong thời gian chờ không"""
        if button_type not in self.button_cooldowns:
            return False
        
        cooldown_time = self.button_cooldowns[button_type]
        return time.time() < cooldown_time
    
    def _update_button_state(self, button_type: ButtonType):
        """Cập nhật trạng thái nút sau khi nhấn"""
        current_time = time.time()
        self.last_button_press[button_type] = current_time
        
        # Set cooldown based on button type
        if button_type in [ButtonType.A, ButtonType.B, ButtonType.C]:
            cooldown_duration = 0.2  # 200ms cooldown for action buttons
        elif button_type == ButtonType.TACKLE:
            cooldown_duration = 0.5  # 500ms cooldown for tackle
        else:
            cooldown_duration = 0.1  # 100ms cooldown for other buttons
        
        self.button_cooldowns[button_type] = current_time + cooldown_duration
    
    def _analyze_button_image(self, image: np.ndarray, button_type: ButtonType) -> str:
        """Phân tích hình ảnh nút để xác định trạng thái"""
        try:
            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Basic image analysis
            # This is a simplified version - in practice, you'd use more sophisticated
            # image processing or ML models to detect button states
            
            # Check if button area is bright (indicating it's active)
            mean_brightness = np.mean(gray)
            
            if mean_brightness > 150:
                return 'active'
            elif mean_brightness > 100:
                return 'available'
            else:
                return 'inactive'
                
        except Exception as e:
            self.logger.error(f"Error analyzing button image: {e}")
            return 'unknown'
    
    def cleanup(self):
        """Dọn dẹp tài nguyên"""
        try:
            self.stop()
            self.logger.info("Game Controller cleanup completed")
        except Exception as e:
            self.logger.error(f"Error during Game Controller cleanup: {e}") 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Action Executor for Dream League Soccer
Executes game actions by sending commands to the emulator
"""

import time
import random
from typing import Dict, Any, Optional, Tuple, List
from enum import Enum
from utils.logger import get_logger, log_performance

class ActionType(Enum):
    """Game action types"""
    MOVE = "move"
    PASS = "pass"
    SHOOT = "shoot"
    TACKLE = "tackle"
    SWITCH_PLAYER = "switch_player"
    SKILL = "skill"
    FORMATION_CHANGE = "formation_change"
    SUBSTITUTION = "substitution"
    WAIT = "wait"
    MENU_NAVIGATION = "menu_navigation"

class ActionExecutor:
    """Executes game actions through emulator control"""
    
    def __init__(self, emulator, config: Dict[str, Any]):
        self.emulator = emulator
        self.config = config
        self.logger = get_logger(__name__)
        
        # Action mappings
        self.action_mappings = self._create_action_mappings()
        
        # Performance tracking
        self.execution_count = 0
        self.successful_executions = 0
        self.last_execution_time = time.time()
        
        # Action timing parameters
        self.action_delays = config.get('action', {}).get('ACTION_DELAYS', {
            'move': 0.1,
            'pass': 0.2,
            'shoot': 0.3,
            'tackle': 0.2,
            'skill': 0.4,
            'menu': 0.5
        })
        
        # Button positions (relative coordinates)
        self.button_positions = config.get('game', {}).get('BUTTON_POSITIONS', {
            'button_a': (0.8, 0.7),  # Right side, bottom area
            'button_b': (0.9, 0.7),  # Right side, bottom area
            'button_c': (0.85, 0.8),  # Right side, bottom area
            'skill_button': (0.75, 0.6),  # Right side, middle area
            'joystick_area': (0.2, 0.7),  # Left side, bottom area
            'formation_button': (0.1, 0.1),  # Top left
            'substitution_button': (0.1, 0.2),  # Top left
            'pause_button': (0.5, 0.05)  # Top center
        })
        
        self.logger.info("Action executor initialized")
    
    def _create_action_mappings(self) -> Dict[str, Dict[str, Any]]:
        """Create mappings between action types and execution methods"""
        return {
            ActionType.MOVE: {
                'method': self._execute_move,
                'description': 'Move player using joystick',
                'requires_focus': True
            },
            ActionType.PASS: {
                'method': self._execute_pass,
                'description': 'Execute pass action',
                'requires_focus': True
            },
            ActionType.SHOOT: {
                'method': self._execute_shoot,
                'description': 'Execute shoot action',
                'requires_focus': True
            },
            ActionType.TACKLE: {
                'method': self._execute_tackle,
                'description': 'Execute tackle action',
                'requires_focus': True
            },
            ActionType.SWITCH_PLAYER: {
                'method': self._execute_switch_player,
                'description': 'Switch to different player',
                'requires_focus': True
            },
            ActionType.SKILL: {
                'method': self._execute_skill,
                'description': 'Execute skill move',
                'requires_focus': True
            },
            ActionType.FORMATION_CHANGE: {
                'method': self._execute_formation_change,
                'description': 'Change team formation',
                'requires_focus': True
            },
            ActionType.SUBSTITUTION: {
                'method': self._execute_substitution,
                'description': 'Make player substitution',
                'requires_focus': True
            },
            ActionType.WAIT: {
                'method': self._execute_wait,
                'description': 'Wait for specified time',
                'requires_focus': False
            },
            ActionType.MENU_NAVIGATION: {
                'method': self._execute_menu_navigation,
                'description': 'Navigate menu system',
                'requires_focus': True
            }
        }
    
    @log_performance
    def execute_action(self, action: ActionType, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute a game action"""
        try:
            self.execution_count += 1
            start_time = time.time()
            
            # Get action mapping
            action_info = self.action_mappings.get(action)
            if not action_info:
                raise ValueError(f"Unknown action type: {action}")
            
            # Check if emulator focus is required
            if action_info['requires_focus']:
                if not self._ensure_emulator_focus():
                    raise RuntimeError("Failed to focus emulator window")
            
            # Execute the action
            result = action_info['method'](context or {})
            
            # Add execution metadata
            execution_time = time.time() - start_time
            result.update({
                'action_type': action.value,
                'execution_time': execution_time,
                'timestamp': start_time,
                'success': result.get('success', False)
            })
            
            # Update success tracking
            if result.get('success', False):
                self.successful_executions += 1
            
            # Log execution
            self.logger.debug(f"Action {action.value} executed in {execution_time:.3f}s, "
                            f"Success: {result.get('success', False)}")
            
            # Update performance stats
            self._update_execution_stats()
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error executing action {action.value}: {e}")
            return {
                'action_type': action.value,
                'success': False,
                'error': str(e),
                'timestamp': time.time()
            }
    
    def _ensure_emulator_focus(self) -> bool:
        """Ensure emulator window is focused"""
        try:
            return self.emulator.focus_window()
        except Exception as e:
            self.logger.error(f"Error focusing emulator: {e}")
            return False
    
    def _execute_move(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute player movement action"""
        try:
            # Get movement parameters from context
            direction = context.get('direction', 'forward')
            intensity = context.get('intensity', 0.7)  # 0.0 to 1.0
            duration = context.get('duration', 0.5)
            
            # Calculate joystick position based on direction
            joystick_pos = self._calculate_joystick_position(direction, intensity)
            
            # Get joystick area coordinates
            joystick_area = self.button_positions['joystick_area']
            
            # Execute joystick movement
            success = self.emulator.drag(
                start_x=joystick_area[0],
                start_y=joystick_area[1],
                end_x=joystick_area[0] + joystick_pos[0] * 0.1,
                end_y=joystick_area[1] + joystick_pos[1] * 0.1,
                duration=duration
            )
            
            # Add delay after movement
            time.sleep(self.action_delays['move'])
            
            return {
                'success': success,
                'direction': direction,
                'intensity': intensity,
                'duration': duration
            }
            
        except Exception as e:
            self.logger.error(f"Error executing move action: {e}")
            return {'success': False, 'error': str(e)}
    
    def _execute_pass(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute pass action"""
        try:
            # Get pass parameters
            pass_type = context.get('pass_type', 'short')  # short, long, through
            target_direction = context.get('target_direction', 'forward')
            
            # Determine which button to use based on pass type
            if pass_type == 'short':
                button = 'button_b'
            elif pass_type == 'long':
                button = 'button_c'
            else:  # through pass
                button = 'button_a'
            
            # Get button position and click
            button_pos = self.button_positions[button]
            success = self.emulator.click(button_pos[0], button_pos[1])
            
            # Add delay after pass
            time.sleep(self.action_delays['pass'])
            
            return {
                'success': success,
                'pass_type': pass_type,
                'target_direction': target_direction,
                'button_used': button
            }
            
        except Exception as e:
            self.logger.error(f"Error executing pass action: {e}")
            return {'success': False, 'error': str(e)}
    
    def _execute_shoot(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute shoot action"""
        try:
            # Get shoot parameters
            power = float(context.get('power', 0.8))  # 0.0 to 1.0
            direction = context.get('direction', 'center')
            
            # Use button A for shooting
            button_pos = self.button_positions['button_a']
            
            # Optional: aim using joystick slightly towards direction before shooting
            try:
                aim_map = {
                    'left': (-0.6, 0.0),
                    'right': (0.6, 0.0),
                    'center': (0.0, 0.0),
                    'high_left': (-0.4, -0.4),
                    'high_right': (0.4, -0.4)
                }
                dx, dy = aim_map.get(direction, (0.0, 0.0))
                joystick_area = self.button_positions['joystick_area']
                self.emulator.drag(
                    start_x=joystick_area[0], start_y=joystick_area[1],
                    end_x=joystick_area[0] + dx * 0.08,
                    end_y=joystick_area[1] + dy * 0.08,
                    duration=0.15
                )
                time.sleep(0.05)
            except Exception:
                pass

            # Click and hold for power (if power control is available)
            if power > 0.7:
                # Long press for power shot
                success = self.emulator.click(button_pos[0], button_pos[1])
                time.sleep(0.2)  # Hold button
            else:
                # Normal shot
                success = self.emulator.click(button_pos[0], button_pos[1])
            
            # Add delay after shoot
            time.sleep(self.action_delays['shoot'])
            
            return {
                'success': success,
                'power': power,
                'direction': direction
            }
            
        except Exception as e:
            self.logger.error(f"Error executing shoot action: {e}")
            return {'success': False, 'error': str(e)}
    
    def _execute_tackle(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute tackle action"""
        try:
            # Get tackle parameters
            tackle_type = context.get('tackle_type', 'normal')  # normal, slide, standing
            
            # Use button C for tackling
            button_pos = self.button_positions['button_c']
            
            # Execute tackle
            success = self.emulator.click(button_pos[0], button_pos[1])
            
            # Add delay after tackle
            time.sleep(self.action_delays['tackle'])
            
            return {
                'success': success,
                'tackle_type': tackle_type
            }
            
        except Exception as e:
            self.logger.error(f"Error executing tackle action: {e}")
            return {'success': False, 'error': str(e)}
    
    def _execute_switch_player(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute player switch action"""
        try:
            # Get switch parameters
            target_player = context.get('target_player', 'nearest')
            
            # Use button C for player switching (may vary by game)
            button_pos = self.button_positions['button_c']
            
            # Execute switch
            success = self.emulator.click(button_pos[0], button_pos[1])
            
            # Add delay after switch
            time.sleep(self.action_delays['tackle'])  # Use tackle delay
            
            return {
                'success': success,
                'target_player': target_player
            }
            
        except Exception as e:
            self.logger.error(f"Error executing player switch: {e}")
            return {'success': False, 'error': str(e)}
    
    def _execute_skill(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute skill move action"""
        try:
            # Get skill parameters
            skill_type = context.get('skill_type', 'basic')
            
            # Use skill button
            button_pos = self.button_positions['skill_button']
            
            # Execute skill
            success = self.emulator.click(button_pos[0], button_pos[1])
            
            # Add delay after skill
            time.sleep(self.action_delays['skill'])
            
            return {
                'success': success,
                'skill_type': skill_type
            }
            
        except Exception as e:
            self.logger.error(f"Error executing skill action: {e}")
            return {'success': False, 'error': str(e)}
    
    def _execute_formation_change(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute formation change action"""
        try:
            # Get formation parameters
            new_formation = context.get('formation', '4-4-2')
            
            # Click formation button
            button_pos = self.button_positions['formation_button']
            success = self.emulator.click(button_pos[0], button_pos[1])
            
            # Add delay after formation change
            time.sleep(self.action_delays['menu'])
            
            return {
                'success': success,
                'formation': new_formation
            }
            
        except Exception as e:
            self.logger.error(f"Error executing formation change: {e}")
            return {'success': False, 'error': str(e)}
    
    def _execute_substitution(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute substitution action"""
        try:
            # Get substitution parameters
            player_out = context.get('player_out', 'tired_player')
            player_in = context.get('player_in', 'fresh_player')
            
            # Click substitution button
            button_pos = self.button_positions['substitution_button']
            success = self.emulator.click(button_pos[0], button_pos[1])
            
            # Add delay after substitution
            time.sleep(self.action_delays['menu'])
            
            return {
                'success': success,
                'player_out': player_out,
                'player_in': player_in
            }
            
        except Exception as e:
            self.logger.error(f"Error executing substitution: {e}")
            return {'success': False, 'error': str(e)}
    
    def _execute_wait(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute wait action"""
        try:
            # Get wait duration
            duration = context.get('duration', 1.0)
            
            # Wait for specified duration
            time.sleep(duration)
            
            return {
                'success': True,
                'duration': duration
            }
            
        except Exception as e:
            self.logger.error(f"Error executing wait action: {e}")
            return {'success': False, 'error': str(e)}
    
    def _execute_menu_navigation(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute menu navigation action"""
        try:
            # Get navigation parameters
            target_menu = context.get('target_menu', 'main')
            action = context.get('action', 'click')
            
            # Determine target position based on menu
            if target_menu == 'main':
                target_pos = (0.5, 0.5)  # Center of screen
            elif target_menu == 'career':
                target_pos = (0.3, 0.4)  # Career mode button
            elif target_menu == 'live':
                target_pos = (0.7, 0.4)  # Live mode button
            else:
                target_pos = (0.5, 0.5)  # Default to center
            
            # Execute navigation
            if action == 'click':
                success = self.emulator.click(target_pos[0], target_pos[1])
            else:
                success = False
            
            # Add delay after menu action
            time.sleep(self.action_delays['menu'])
            
            return {
                'success': success,
                'target_menu': target_menu,
                'action': action
            }
            
        except Exception as e:
            self.logger.error(f"Error executing menu navigation: {e}")
            return {'success': False, 'error': str(e)}
    
    def _calculate_joystick_position(self, direction: str, intensity: float) -> Tuple[float, float]:
        """Calculate joystick position based on direction and intensity"""
        # Normalize intensity to 0.0 - 1.0
        intensity = max(0.0, min(1.0, intensity))
        
        # Direction vectors (x, y) where (0, 0) is center
        direction_vectors = {
            'forward': (0.0, -intensity),      # Up
            'backward': (0.0, intensity),      # Down
            'left': (-intensity, 0.0),         # Left
            'right': (intensity, 0.0),         # Right
            'forward_left': (-intensity * 0.7, -intensity * 0.7),    # Diagonal up-left
            'forward_right': (intensity * 0.7, -intensity * 0.7),    # Diagonal up-right
            'backward_left': (-intensity * 0.7, intensity * 0.7),    # Diagonal down-left
            'backward_right': (intensity * 0.7, intensity * 0.7),    # Diagonal down-right
            'center': (0.0, 0.0)              # Center (no movement)
        }
        
        return direction_vectors.get(direction, (0.0, 0.0))
    
    def _update_execution_stats(self):
        """Update execution performance statistics"""
        current_time = time.time()
        
        if current_time - self.last_execution_time > 60:  # Every minute
            executions_per_minute = self.execution_count / ((current_time - self.last_execution_time) / 60)
            success_rate = self.successful_executions / max(self.execution_count, 1)
            
            self.logger.debug(f"Execution rate: {executions_per_minute:.2f} per minute, "
                            f"Success rate: {success_rate:.2%}")
            
            # Reset counters
            self.execution_count = 0
            self.successful_executions = 0
            self.last_execution_time = current_time
    
    def get_execution_stats(self) -> Dict[str, Any]:
        """Get execution performance statistics"""
        current_time = time.time()
        uptime = current_time - self.last_execution_time + 60
        
        return {
            'total_executions': self.execution_count,
            'successful_executions': self.successful_executions,
            'success_rate': self.successful_executions / max(self.execution_count, 1),
            'uptime_seconds': uptime,
            'executions_per_minute': self.execution_count / (uptime / 60) if uptime > 0 else 0,
            'action_delays': self.action_delays.copy(),
            'button_positions': self.button_positions.copy()
        }
    
    def set_action_delay(self, action_type: str, delay: float):
        """Set delay for specific action type"""
        if action_type in self.action_delays and delay >= 0:
            self.action_delays[action_type] = delay
            self.logger.info(f"Action delay for {action_type} set to {delay}s")
        else:
            self.logger.warning(f"Invalid action type or delay: {action_type}, {delay}")
    
    def set_button_position(self, button_name: str, position: Tuple[float, float]):
        """Set position for specific button"""
        if button_name in self.button_positions:
            self.button_positions[button_name] = position
            self.logger.info(f"Button position for {button_name} set to {position}")
        else:
            self.logger.warning(f"Unknown button: {button_name}")
    
    def reset_execution_stats(self):
        """Reset execution statistics"""
        self.execution_count = 0
        self.successful_executions = 0
        self.last_execution_time = time.time()
        self.logger.info("Action execution statistics reset") 

    def close_advertisement(self):
        """Try to close ad by clicking common close/skip areas."""
        try:
            # Try corners: top-right, top-left, bottom-right
            candidates = [(0.95, 0.08), (0.05, 0.08), (0.95, 0.92)]
            for x, y in candidates:
                self.emulator.click(x, y)
                time.sleep(0.2)
            return True
        except Exception as e:
            self.logger.error(f"Error closing advertisement: {e}")
            return False 
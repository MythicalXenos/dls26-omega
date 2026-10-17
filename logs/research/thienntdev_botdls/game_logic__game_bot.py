#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Game Bot - Logic chơi game tự động cho DLS
"""

import threading
import time
from typing import Dict, Any, Optional, List
from collections import deque

from utils.logger import get_logger, BotLogger, log_performance
from game_logic.game_state_detector import GameStateDetector, GameState
from game_logic.decision_maker import DecisionMaker
from game_logic.action_executor import ActionExecutor
from game_logic.resource_manager import ResourceManager
from game_logic.computer_vision import ComputerVisionSystem
from config.settings import TEAM_CONFIG
from game_logic.game_controller import GameController, MovementType, ButtonType
from game_logic.special_situations import SpecialSituationsHandler, SituationType

class GameBot:
    """Bot tự động chơi game DLS"""
    
    def __init__(self, name: str, emulator, account_info: dict, config: dict, farming_config: dict, data_collector=None):
        self.name = name
        self.emulator = emulator
        self.account_info = account_info
        self.config = config
        self.farming_config = farming_config
        self.data_collector = data_collector
        
        self.logger = get_logger(__name__)
        self.bot_logger = BotLogger(name)
        
        # Bot state
        self.is_running = False
        self.is_paused = False
        self.auto_farming = False
        self.current_state = GameState.UNKNOWN
        
        # Game components
        self.state_detector = GameStateDetector(emulator, config)
        self.decision_maker = DecisionMaker(config)
        self.action_executor = ActionExecutor(emulator, config)
        self.resource_manager = ResourceManager({'resource': {'DEFAULT_TARGETS': {
            'gold': farming_config.get('gold_target', 15000),
            'diamonds': farming_config.get('diamond_target', 400)
        }}})
        
        # Performance tracking
        self.start_time = None
        self.match_count = 0
        self.resources_earned = {'gold': 0, 'diamonds': 0}
        self.last_action_time = None
        self.last_success_action_time = None
        
        # Threading
        self.game_thread = None
        self.lock = threading.Lock()
        
        # Game loop control
        self.game_loop_active = False
        self.state_check_interval = 1.0  # seconds
        
        self.logger.info(f"Game bot initialized: {name}")
        
        # Computer Vision system
        try:
            self.cv_system = ComputerVisionSystem(config)
            self.cv_system.start()
        except Exception:
            self.cv_system = None

        # Controller & special situations
        try:
            self.controller = GameController(self.emulator, config.get('CONTROLS', {}))
            self.controller.start()
        except Exception:
            self.controller = None
        try:
            self.special_handler = SpecialSituationsHandler(self.emulator, self.controller, config)
            self.special_handler.start()
        except Exception:
            self.special_handler = None

        # Attacking direction tracking
        self.attacking_right = True
        self.ball_history = deque(maxlen=30)
    
    def start(self) -> bool:
        """Khởi động bot"""
        try:
            with self.lock:
                if self.is_running:
                    self.logger.warning("Bot is already running")
                    return True
                
                if not self.emulator.is_window_active():
                    self.logger.error("Emulator window not active")
                    return False
                
                self.is_running = True
                self.start_time = time.time()
                self.game_loop_active = True
                
                # Start game loop thread
                self.game_thread = threading.Thread(
                    target=self._game_loop,
                    daemon=True
                )
                self.game_thread.start()
                
                self.bot_logger.log_status("Bot started")
                self.logger.info(f"Bot {self.name} started successfully")
                
                return True
                
        except Exception as e:
            self.logger.error(f"Error starting bot: {e}")
            return False
    
    def stop(self) -> bool:
        """Dừng bot"""
        try:
            with self.lock:
                if not self.is_running:
                    return True
                
                self.is_running = False
                self.game_loop_active = False
                
                # Wait for game thread to finish
                if self.game_thread and self.game_thread.is_alive():
                    self.game_thread.join(timeout=5.0)
                
                self.bot_logger.log_status("Bot stopped")
                self.logger.info(f"Bot {self.name} stopped")
                
                return True
                
        except Exception as e:
            self.logger.error(f"Error stopping bot: {e}")
            return False
    
    def pause(self) -> bool:
        """Tạm dừng bot"""
        try:
            with self.lock:
                if not self.is_running:
                    return False
                
                self.is_paused = True
                self.bot_logger.log_status("Bot paused")
                self.logger.info(f"Bot {self.name} paused")
                
                return True
                
        except Exception as e:
            self.logger.error(f"Error pausing bot: {e}")
            return False
    
    def resume(self) -> bool:
        """Tiếp tục bot"""
        try:
            with self.lock:
                if not self.is_running or not self.is_paused:
                    return False
                
                self.is_paused = False
                self.bot_logger.log_status("Bot resumed")
                self.logger.info(f"Bot {self.name} resumed")
                
                return True
                
        except Exception as e:
            self.logger.error(f"Error resuming bot: {e}")
            return False
    
    def set_auto_farming(self, enabled: bool) -> bool:
        """Bật/tắt chế độ tự động cày tài nguyên"""
        try:
            self.auto_farming = enabled
            self.logger.info(f"Auto farming {'enabled' if enabled else 'disabled'} for {self.name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error setting auto farming: {e}")
            return False
    
    def _game_loop(self):
        """Vòng lặp chính của game"""
        self.logger.info(f"Game loop started for {self.name}")
        
        while self.game_loop_active:
            try:
                if not self.is_running or self.is_paused:
                    time.sleep(1)
                    continue
                
                # Detect current game state
                new_state = self._detect_game_state()
                
                # Handle state change
                if new_state != self.current_state:
                    self._handle_state_change(new_state)
                
                # Execute actions based on current state
                self._execute_state_actions()
                # Check special situations
                self._handle_special_situations()
                
                # Check resource targets if auto farming
                if self.auto_farming:
                    self._check_resource_targets()
                
                # Gửi dữ liệu về collector
                if self.data_collector:
                    record = {
                        'bot_id': self.name,
                        'timestamp': time.time(),
                        'state': self.current_state.value,
                        'resources': self._get_current_resources(),
                        'match_count': self.match_count,
                        'account_info': self.account_info,
                        # Có thể bổ sung thêm action, reward nếu cần
                    }
                    self.data_collector.collect(record)
                
                # Wait before next iteration
                time.sleep(self.state_check_interval)
                
            except Exception as e:
                self.logger.error(f"Error in game loop: {e}")
                time.sleep(5)  # Wait longer on error
        
        self.logger.info(f"Game loop stopped for {self.name}")
    
    def _detect_game_state(self) -> GameState:
        """Phát hiện trạng thái game hiện tại"""
        try:
            state = self.state_detector.detect_current_state()
            return state
            
        except Exception as e:
            self.logger.error(f"Error detecting game state: {e}")
            return GameState.UNKNOWN
    
    def _handle_state_change(self, new_state: GameState):
        """Xử lý khi trạng thái game thay đổi"""
        try:
            old_state = self.current_state
            self.current_state = new_state
            
            if old_state != new_state:
                self.logger.info(f"Game state changed: {old_state.value} -> {new_state.value}")
                self.bot_logger.log_game_action("state_change", f"{old_state.value} -> {new_state.value}")
                
                # Handle specific state transitions
                if new_state == GameState.MATCH_PLAYING:
                    self._on_match_start()
                elif new_state == GameState.MAIN_MENU:
                    self._on_return_to_menu()
                elif new_state == GameState.ADVERTISEMENT:
                    self._on_advertisement()
            
        except Exception as e:
            self.logger.error(f"Error handling state change: {e}")
    
    def _execute_state_actions(self):
        """Thực hiện hành động dựa trên trạng thái hiện tại"""
        try:
            if self.current_state == GameState.UNKNOWN:
                return
            
            # Build game context from CV if available
            game_context = self._build_game_context()
            
            # Get decision for current state
            decision = self.decision_maker.get_decision(self.current_state.value, game_context)
            
            if decision:
                # Execute the decision
                action = decision.get('action')
                context = decision.get('context', {})
                result = self.action_executor.execute_action(action, context)
                
                if result.get('success'):
                    self._update_action_stats()
                    self.bot_logger.log_game_action("action_executed", action.value)
                    # Report success for learning
                    self.decision_maker.report_action_result(action, True, game_context)
                    # Give positive reward and log for param tuning
                    try:
                        reward = self._estimate_action_reward(action.value, game_context, success=True)
                        self.decision_maker.report_action_outcome(action, context, game_context, reward)
                    except Exception:
                        pass
                    self.last_success_action_time = time.time()
                else:
                    self.logger.warning(f"Failed to execute action: {action.value}")
                    self.decision_maker.report_action_result(action, False, game_context)
                    try:
                        reward = self._estimate_action_reward(action.value, game_context, success=False)
                        self.decision_maker.report_action_outcome(action, context, game_context, reward)
                    except Exception:
                        pass
            
        except Exception as e:
            self.logger.error(f"Error executing state actions: {e}")
    
    def _on_match_start(self):
        """Xử lý khi bắt đầu trận đấu"""
        try:
            self.match_count += 1
            self.logger.info(f"Match {self.match_count} started for {self.name}")
            
            # Reset match-specific variables
            self.last_action_time = time.time()
            
        except Exception as e:
            self.logger.error(f"Error handling match start: {e}")
    
    def _on_return_to_menu(self):
        """Xử lý khi quay về menu chính"""
        try:
            self.logger.info(f"Returned to main menu for {self.name}")
            # Update resources heuristically after a match (until OCR is implemented)
            if self.match_count > 0:
                # Award minimal gold per match as heuristic
                new_gold = self.resources_earned.get('gold', 0) + 100
                self.resources_earned['gold'] = new_gold
                # Update resource manager storage for this bot/account
                self.resource_manager.update_current_resources(
                    self.name,
                    {
                        'gold': new_gold,
                        'diamonds': self.resources_earned.get('diamonds', 0)
                    }
                )
            
            # Check if we should continue farming
            if self.auto_farming:
                self._continue_farming()
            
        except Exception as e:
            self.logger.error(f"Error handling return to menu: {e}")
    
    def _on_advertisement(self):
        """Xử lý khi xuất hiện quảng cáo"""
        try:
            self.logger.info(f"Advertisement detected for {self.name}")
            
            # Wait for advertisement to finish
            time.sleep(5)
            
            # Try to close advertisement
            self.action_executor.close_advertisement()
            
        except Exception as e:
            self.logger.error(f"Error handling advertisement: {e}")
    
    def _continue_farming(self):
        """Tiếp tục cày tài nguyên"""
        try:
            # Check current resources
            current_resources = self._get_current_resources()
            
            if not current_resources:
                return
            
            # Check if targets reached
            targets = self.resource_manager.get_targets(self.name)
            if not targets:
                return
            
            gold_reached = current_resources.get('gold', 0) >= targets.get('gold', 0)
            diamonds_reached = current_resources.get('diamonds', 0) >= targets.get('diamonds', 0)
            
            if gold_reached and diamonds_reached:
                self.logger.info(f"Resource targets reached for {self.name}, stopping bot")
                self.stop()
                return
            
            # Continue with next farming action
            next_action_decision = self.decision_maker.get_decision(self.current_state.value, {'ball_possession': 'own'})
            if next_action_decision:
                self.action_executor.execute_action(next_action_decision['action'], next_action_decision.get('context', {}))
            
        except Exception as e:
            self.logger.error(f"Error continuing farming: {e}")
    
    def _check_resource_targets(self):
        """Kiểm tra mục tiêu tài nguyên"""
        try:
            current_resources = self._get_current_resources()
            if not current_resources:
                return
            
            targets = self.resource_manager.get_targets(self.name)
            if not targets:
                return
            
            # Log resource progress
            for resource_type in ['gold', 'diamonds']:
                current = current_resources.get(resource_type, 0)
                target = targets.get(resource_type, 0)
                if target > 0:
                    progress = min(100, (current / target) * 100)
                    self.logger.debug(f"{resource_type} progress: {current}/{target} ({progress:.1f}%)")
            
        except Exception as e:
            self.logger.error(f"Error checking resource targets: {e}")
    
    def _get_current_resources(self) -> Optional[Dict[str, int]]:
        """Lấy tài nguyên hiện tại"""
        try:
            # Use ResourceManager stored values for this bot/account
            current = self.resource_manager.get_current_resources(self.name)
            if not current:
                return {
                    'gold': self.resources_earned.get('gold', 0),
                    'diamonds': self.resources_earned.get('diamonds', 0)
                }
            return current
            
        except Exception as e:
            self.logger.error(f"Error getting current resources: {e}")
            return None
    
    def _update_action_stats(self):
        """Cập nhật thống kê hành động"""
        self.last_action_time = time.time()

    def _estimate_action_reward(self, action_name: str, context: Dict[str, Any], success: bool) -> float:
        """Ước lượng reward nhanh để học tham số mà không cần OCR nặng.
        SHOOT: thưởng cao hơn nếu khoảng cách nhỏ (gần goal) và hành động success.
        PASS: thưởng khi pressure cao và vẫn success.
        MOVE: thưởng vừa phải nếu moving khi pressure thấp (giữ bóng an toàn).
        """
        try:
            base = 1.0 if success else 0.0
            dist = float(context.get('distance_to_goal', 0.5))  # 0 gần, 1 xa
            pressure = float(context.get('opponent_pressure', 0.3))
            if action_name == 'shoot':
                # Closer to goal → bigger reward on success; small negative if fail
                reward = base * (1.2 - dist) - (0.2 if not success else 0.0)
            elif action_name == 'pass':
                reward = base * (0.6 + 0.6 * pressure) - (0.1 if not success else 0.0)
            else:
                reward = base * 0.5
            return max(-0.5, min(1.5, reward))
        except Exception:
            return 0.0
    
    def get_current_state(self) -> str:
        """Lấy trạng thái hiện tại"""
        return self.current_state.value
    
    def get_resource_status(self) -> Dict[str, Any]:
        """Lấy trạng thái tài nguyên"""
        try:
            return {
                'current_resources': self._get_current_resources(),
                'targets': self.resource_manager.get_targets(self.name),
                'auto_farming': self.auto_farming
            }
            
        except Exception as e:
            self.logger.error(f"Error getting resource status: {e}")
            return {}
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Lấy thống kê hiệu suất"""
        try:
            uptime = time.time() - (self.start_time or time.time())
            return {
                'match_count': self.match_count,
                'uptime_seconds': uptime,
                'last_action_time': self.last_action_time,
            }
        except Exception as e:
            self.logger.error(f"Error getting performance stats: {e}")
            return {} 

    # === Added public APIs used by manager/UI ===
    def get_status(self) -> Dict[str, Any]:
        try:
            return {
                'name': self.name,
                'is_running': self.is_running,
                'is_paused': self.is_paused,
                'current_state': self.current_state.value,
                'auto_farming': self.auto_farming,
            }
        except Exception:
            return {}

    def get_stats(self) -> Dict[str, Any]:
        try:
            resources = self._get_current_resources() or {}
            return {
                'gold_farmed': resources.get('gold', 0),
                'diamonds_farmed': resources.get('diamonds', 0),
                'matches_played': self.match_count,
                'wins': 0,
                'losses': 0,
            }
        except Exception:
            return {}

    def update_farming_targets(self, gold_target: int, diamond_target: int):
        try:
            self.resource_manager.set_resource_targets(self.name, gold_target, diamond_target)
        except Exception:
            pass

    def update_game_mode_settings(self, game_modes: Dict[str, Any]):
        # Stub for compatibility
        return True

    def is_healthy(self) -> bool:
        try:
            thread_ok = not self.game_thread or self.game_thread.is_alive()
            emulator_ok = True
            try:
                emulator_ok = self.emulator.is_responsive()
            except Exception:
                pass
            return thread_ok and emulator_ok
        except Exception:
            return False

    def cleanup(self):
        try:
            self.stop()
            if self.cv_system:
                self.cv_system.cleanup()
        except Exception:
            pass

    # === Internal helpers ===
    def _build_game_context(self) -> Dict[str, Any]:
        context = {
            'ball_possession': 'unknown',
            'field_position': 'center',
            'score_difference': 0,
            'time_remaining': 90,
            'player_energy': 100,
        }
        try:
            if not self.cv_system:
                return context
            # Fast capture (no disk IO)
            frame = None
            if hasattr(self.emulator, 'capture_frame'):
                frame = self.emulator.capture_frame()
            if frame is None:
                # Fallback to slow path
                screenshot_path = self.emulator.take_screenshot()
                if not screenshot_path:
                    return context
                import cv2
                frame = cv2.imread(screenshot_path)
            if frame is None:
                return context
            analysis = self.cv_system.process_frame(frame) or {}
            # Sample jersey colors at match start (first frames)
            if self.match_count >= 1 and len(self.ball_history) < 5:
                self._maybe_sample_jerseys(frame)
            # Field position from ball x
            ball_pos = None
            game_situation = analysis.get('game_situation', {})
            if 'ball_position' in game_situation and game_situation['ball_position']:
                ball_pos = game_situation['ball_position']
            elif analysis.get('ball_detections'):
                best_ball = max(analysis['ball_detections'], key=lambda d: d.get('confidence', 0))
                x, y = best_ball.get('bbox', (960, 540, 0, 0))[:2]
                ball_pos = (x, y)
            if ball_pos:
                if ball_pos[0] < 640:
                    context['field_position'] = 'own_half'
                elif ball_pos[0] > 1280:
                    context['field_position'] = 'opponent_half'
                else:
                    context['field_position'] = 'center'
                context['ball_position'] = ball_pos
                # Update attacking direction estimation
                self._update_attacking_direction(ball_pos)
                context['attacking_right'] = self.attacking_right
            # Possession heuristic: unknown without team ID; keep contested
            # Use possession from analysis if available
            poss = analysis.get('possession') or {}
            if poss.get('label') == 'own' and poss.get('confidence', 0.0) >= 0.5:
                context['ball_possession'] = 'own'
                self.last_possession_label = 'own'
            elif poss.get('label') == 'opponent' and poss.get('confidence', 0.0) >= 0.5:
                context['ball_possession'] = 'opponent'
                self.last_possession_label = 'opponent'
            else:
                context['ball_possession'] = getattr(self, 'last_possession_label', 'contested') if getattr(self, 'last_possession_label', 'unknown') != 'unknown' else 'contested'

            # HUD-based flags
            try:
                hud = analysis.get('hud') or {}
                filled = hud.get('filled') or []
                hollow = hud.get('hollow') or []
                context['hud_filled_present'] = len(filled) > 0
                context['hud_hollow_near_ball'] = False
                if hollow and ball_pos:
                    bx, by = ball_pos
                    # Image width heuristic
                    w = frame.shape[1]
                    thr = max(24, int(0.08 * w))
                    # Choose nearest hollow
                    def center(bb):
                        x, y, w0, h0 = bb
                        return (x + w0 / 2, y + h0 / 2)
                    nearest_d = 1e9
                    for hdet in hollow:
                        cx, cy = center(hdet['bbox'])
                        d = ((cx - bx) ** 2 + (cy - by) ** 2) ** 0.5
                        if d < nearest_d:
                            nearest_d = d
                    if nearest_d <= thr:
                        context['hud_hollow_near_ball'] = True
            except Exception:
                context['hud_filled_present'] = False
                context['hud_hollow_near_ball'] = False
            # Opponent pressure heuristic based on player density near ball
            try:
                player_detections = analysis.get('player_detections') or []
                field_info = analysis.get('field_info') or {}
                if ball_pos and player_detections:
                    bx, by = ball_pos
                    close_players = 0
                    for det in player_detections:
                        x, y, w, h = det.get('bbox', (0, 0, 0, 0))
                        cx = x + w/2
                        cy = y + h/2
                        dist = ((cx - bx)**2 + (cy - by)**2) ** 0.5
                        if dist < 200:  # pixels
                            close_players += 1
                    # Normalize rough pressure: 0..1 for 0..5 players near
                    context['opponent_pressure'] = min(1.0, close_players / 5.0)
                else:
                    context['opponent_pressure'] = 0.3
            except Exception:
                context['opponent_pressure'] = 0.3
            # Distance to goal heuristic using attacking_right or goal detection
            try:
                if ball_pos:
                    width = frame.shape[1]
                    goal_info = analysis.get('goal_info') or {}
                    left_score = goal_info.get('left_goal_score', 0.0)
                    right_score = goal_info.get('right_goal_score', 0.0)
                    # If goals are clearly detected, set attacking toward opposite goal of own half
                    if left_score > 0.5 or right_score > 0.5:
                        # Heuristic: if ball ở nửa trái nhiều và thấy khung thành trái rõ → ta đang thủ bên trái → tấn công phải
                        self.attacking_right = right_score <= left_score
                    if self.attacking_right:
                        distance = max(1, width - ball_pos[0])
                    else:
                        distance = max(1, ball_pos[0])
                    context['distance_to_goal'] = min(1.0, distance / width)
            except Exception:
                pass
            return context
        except Exception:
            return context

    def _maybe_sample_jerseys(self, frame):
        try:
            regions = TEAM_CONFIG.get('jersey_sample_regions', {})
            if not regions:
                return
            h, w = frame.shape[:2]
            abs_regions = {}
            for k, (x1, y1, x2, y2) in regions.items():
                abs_regions[k] = (int(x1 * w), int(y1 * h), int(x2 * w), int(y2 * h))
            if hasattr(self.cv_system, 'detector'):
                self.cv_system.detector.sample_team_colors(frame, abs_regions)
        except Exception:
            pass

    def _handle_special_situations(self):
        if not self.special_handler or not self.emulator:
            return
        try:
            frame = None
            if hasattr(self.emulator, 'capture_frame'):
                frame = self.emulator.capture_frame()
            if frame is None:
                return
            sit = self.special_handler.detect_special_situation(frame)
            if sit:
                # Pause regular flow and execute strategy via controller
                ctx = {'attacking_right': self.attacking_right}
                self.logger.info(f"Special situation detected: {sit.value}")
                self.special_handler.handle_special_situation(sit, ctx)
        except Exception as e:
            self.logger.error(f"Error handling special situations: {e}")

    def _update_attacking_direction(self, ball_pos: Any) -> None:
        try:
            # Record ball history
            now = time.time()
            self.ball_history.append((now, ball_pos))
            # Only attempt direction update if we recently executed a successful action
            if not self.last_success_action_time or now - self.last_success_action_time > 5.0:
                return
            # Need enough history
            if len(self.ball_history) < 5:
                return
            # Compute dx trend over last positions
            recent = list(self.ball_history)[-10:]
            dxs = []
            for i in range(1, len(recent)):
                (_, (x_prev, _)) = recent[i-1]
                (_, (x_cur, _)) = recent[i]
                dxs.append(x_cur - x_prev)
            if not dxs:
                return
            avg_dx = sum(dxs) / len(dxs)
            # Threshold in pixels per sample
            if avg_dx > 2.0:
                self.attacking_right = True
            elif avg_dx < -2.0:
                self.attacking_right = False
        except Exception:
            pass
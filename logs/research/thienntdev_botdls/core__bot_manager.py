#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bot Manager for DLS Auto Bot
Manages multiple bot instances and coordinates their activities
"""

import time
import threading
from typing import Dict, List, Optional, Any
from pathlib import Path
import json

from config.settings import FARMING_CONFIG, GAME_MODES, BOT_CONFIG
from emulator.emulator_controller import get_emulator_controller
from game_logic.game_bot import GameBot
from utils.logger import get_logger, BotLogger
from core.central_data_collector import CentralDataCollector

logger = get_logger(__name__)

class BotManager:
    """Manages multiple bot instances and coordinates their activities"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.bots: Dict[str, GameBot] = {}
        self.emulator_controller = get_emulator_controller()
        self.max_bots = 5
        self.is_running = False
        self.auto_restart = True
        self.global_stats = {
            'total_gold_farmed': 0,
            'total_diamonds_farmed': 0,
            'total_matches_played': 0,
            'total_wins': 0,
            'total_losses': 0,
            'start_time': time.time()
        }
        
        # Bot configuration
        self.bot_config = BOT_CONFIG.copy()
        self.farming_config = FARMING_CONFIG.copy()
        self.game_modes = GAME_MODES.copy()
        
        # Performance monitoring
        self.performance_monitor = None
        self.monitoring_enabled = True
        
        # Database for storing bot data
        self.db_path = Path(__file__).parent.parent / 'data' / 'bots.db'
        self.db_path.parent.mkdir(exist_ok=True)
        
        self.data_collector = CentralDataCollector()
        
        logger.info("Bot Manager initialized")
    
    def create_bot(self, name: str, emulator_name: str, account_info: Dict[str, Any],
                   emulator_type: Optional[str] = None,
                   emulator_params: Optional[Dict[str, Any]] = None) -> Optional[GameBot]:
        """Create a new bot instance"""
        try:
            if len(self.bots) >= self.max_bots:
                logger.warning(f"Maximum bots ({self.max_bots}) reached")
                return None
            
            if name in self.bots:
                logger.warning(f"Bot {name} already exists")
                return None
            
            # Ensure emulator instance exists
            emulator = self.emulator_controller.get_instance(emulator_name)
            if not emulator:
                use_mock = self.config.get('DEV_CONFIG', {}).get('mock_emulator', False)
                emu_type = emulator_type if emulator_type else ('mock' if use_mock else 'ldplayer')
                instance_id = 0
                # If adb_port provided, try to derive instance_id from base in config
                if emulator_params and 'adb_port' in emulator_params:
                    try:
                        base_port = self.config.get('EMULATOR_CONFIG', {}).get(emu_type, {}).get('adb_port', 0)
                        if base_port:
                            instance_id = max(0, int(emulator_params['adb_port']) - int(base_port))
                    except Exception:
                        instance_id = 0
                emulator = self.emulator_controller.create_instance(emulator_name, emu_type, instance_id)
                if not emulator:
                    logger.error(f"Failed to create emulator instance: {emulator_name}")
                    return None
                # Override emulator parameters if provided
                if emulator_params:
                    if 'input_mode' in emulator_params:
                        emulator.input_mode = emulator_params['input_mode']
                    if 'adb_port' in emulator_params and emulator_params['adb_port']:
                        emulator.adb_port = int(emulator_params['adb_port'])
                    # Mark attach_only if provided via EMULATOR_CONFIG
                    try:
                        emulator.config['attach_only'] = bool(emulator_params.get('attach_only', False))
                    except Exception:
                        pass
                # Try to start/attach emulator (mock will succeed instantly)
                self.emulator_controller.start_instance(emulator_name)
            
            # Create bot instance
            bot = GameBot(
                name=name,
                emulator=emulator,
                account_info=account_info,
                config=self.bot_config,
                farming_config=self.farming_config,
                data_collector=self.data_collector
            )
            
            self.bots[name] = bot
            logger.info(f"Created bot: {name} for emulator: {emulator_name}")
            
            # Save bot configuration
            self._save_bot_config(name, account_info)
            
            return bot
            
        except Exception as e:
            logger.error(f"Error creating bot {name}: {e}")
            return None
    
    def start_bot(self, name: str) -> bool:
        """Start a specific bot"""
        try:
            if name not in self.bots:
                # Attempt to auto-create with default emulator of same name
                emulator_name = name
                account_info = {'account_id': name}
                bot = self.create_bot(name, emulator_name, account_info)
                if not bot:
                    logger.error(f"Bot {name} not found and could not be created")
                    return False
            
            bot = self.bots[name]
            success = bot.start()
            
            if success:
                logger.info(f"Bot {name} started successfully")
            else:
                logger.error(f"Failed to start bot {name}")
            
            return success
            
        except Exception as e:
            logger.error(f"Error starting bot {name}: {e}")
            return False
    
    def stop_bot(self, name: str) -> bool:
        """Stop a specific bot"""
        try:
            if name not in self.bots:
                logger.error(f"Bot {name} not found")
                return False
            
            bot = self.bots[name]
            success = bot.stop()
            
            if success:
                logger.info(f"Bot {name} stopped successfully")
            else:
                logger.error(f"Failed to stop bot {name}")
            
            return success
            
        except Exception as e:
            logger.error(f"Error stopping bot {name}: {e}")
            return False
    
    def restart_bot(self, name: str) -> bool:
        """Restart a specific bot"""
        try:
            if name not in self.bots:
                logger.error(f"Bot {name} not found")
                return False
            
            logger.info(f"Restarting bot {name}")
            if self.stop_bot(name):
                time.sleep(5)
                return self.start_bot(name)
            
            return False
            
        except Exception as e:
            logger.error(f"Error restarting bot {name}: {e}")
            return False
    
    def start_all_bots(self) -> Dict[str, bool]:
        """Start all bots"""
        results = {}
        for name in self.bots:
            results[name] = self.start_bot(name)
            time.sleep(2)  # Delay between starts
        return results
    
    def stop_all_bots(self) -> Dict[str, bool]:
        """Stop all bots"""
        results = {}
        for name in self.bots:
            results[name] = self.stop_bot(name)
        return results
    
    def restart_all_bots(self) -> Dict[str, bool]:
        """Restart all bots"""
        results = {}
        for name in self.bots:
            results[name] = self.restart_bot(name)
            time.sleep(5)
        return results
    
    def remove_bot(self, name: str) -> bool:
        """Remove a bot instance"""
        try:
            if name not in self.bots:
                return False
            
            bot = self.bots[name]
            bot.stop()
            del self.bots[name]
            
            # Remove bot configuration
            self._remove_bot_config(name)
            
            logger.info(f"Removed bot: {name}")
            return True
            
        except Exception as e:
            logger.error(f"Error removing bot {name}: {e}")
            return False
    
    def get_bot(self, name: str) -> Optional[GameBot]:
        """Get a specific bot instance"""
        return self.bots.get(name)
    
    def get_all_bots(self) -> Dict[str, GameBot]:
        """Get all bot instances"""
        return self.bots.copy()
    
    def get_running_bots(self) -> Dict[str, GameBot]:
        """Get all running bots"""
        return {name: bot for name, bot in self.bots.items() if bot.is_running}
    
    def get_bot_status(self, name: str) -> Optional[Dict[str, Any]]:
        """Get status of a specific bot"""
        if name in self.bots:
            return self.bots[name].get_status()
        return None
    
    def get_all_bot_status(self) -> Dict[str, Dict[str, Any]]:
        """Get status of all bots"""
        return {name: bot.get_status() for name, bot in self.bots.items()}
    
    def get_global_stats(self) -> Dict[str, Any]:
        """Get global statistics from all bots"""
        try:
            stats = self.global_stats.copy()
            
            # Aggregate stats from all bots
            for bot in self.bots.values():
                bot_stats = bot.get_stats()
                if bot_stats:
                    stats['total_gold_farmed'] += bot_stats.get('gold_farmed', 0)
                    stats['total_diamonds_farmed'] += bot_stats.get('diamonds_farmed', 0)
                    stats['total_matches_played'] += bot_stats.get('matches_played', 0)
                    stats['total_wins'] += bot_stats.get('wins', 0)
                    stats['total_losses'] += bot_stats.get('losses', 0)
            
            # Calculate additional metrics
            uptime = time.time() - stats['start_time']
            stats['uptime_hours'] = uptime / 3600
            stats['bots_running'] = len(self.get_running_bots())
            stats['total_bots'] = len(self.bots)
            
            if stats['total_matches_played'] > 0:
                stats['win_rate'] = stats['total_wins'] / stats['total_matches_played']
            else:
                stats['win_rate'] = 0.0
            
            return stats
            
        except Exception as e:
            logger.error(f"Error getting global stats: {e}")
            return self.global_stats.copy()

    # === Added APIs used by UI ===
    def get_game_stats(self) -> Dict[str, Any]:
        try:
            stats = self.get_global_stats()
            return stats
        except Exception as e:
            logger.error(f"Error getting game stats: {e}")
            return {}

    def start_resource_farming(self, emulator_id: str, targets: Dict[str, int]) -> bool:
        try:
            if emulator_id not in self.bots:
                # Try to start/create the bot
                if not self.start_bot(emulator_id):
                    return False
            bot = self.bots[emulator_id]
            bot.update_farming_targets(targets.get('gold_target', 0), targets.get('diamond_target', 0))
            bot.set_auto_farming(True)
            return True
        except Exception as e:
            logger.error(f"Error starting resource farming for {emulator_id}: {e}")
            return False

    def stop_resource_farming(self, emulator_id: str) -> bool:
        try:
            if emulator_id in self.bots:
                self.bots[emulator_id].set_auto_farming(False)
                return True
            return False
        except Exception as e:
            logger.error(f"Error stopping resource farming for {emulator_id}: {e}")
            return False
    
    def update_farming_targets(self, gold_target: int, diamond_target: int):
        """Update farming targets for all bots"""
        try:
            self.farming_config['gold_target'] = gold_target
            self.farming_config['diamond_target'] = diamond_target
            
            # Update all bots
            for bot in self.bots.values():
                bot.update_farming_targets(gold_target, diamond_target)
            
            logger.info(f"Updated farming targets: Gold={gold_target}, Diamonds={diamond_target}")
            
        except Exception as e:
            logger.error(f"Error updating farming targets: {e}")

    def update_bot_targets(self, name: str, gold_target: int, diamond_target: int) -> bool:
        """Update farming targets for a specific bot/emulator"""
        try:
            if name not in self.bots:
                logger.error(f"Bot {name} not found")
                return False
            bot = self.bots[name]
            bot.update_farming_targets(gold_target, diamond_target)
            logger.info(f"Updated targets for {name}: Gold={gold_target}, Diamonds={diamond_target}")
            return True
        except Exception as e:
            logger.error(f"Error updating targets for {name}: {e}")
            return False

    def shutdown_emulator(self, name: str) -> bool:
        """Stop bot and shutdown/remove emulator instance for given name."""
        try:
            # Stop bot if exists
            if name in self.bots:
                try:
                    self.stop_bot(name)
                except Exception:
                    pass
            # Stop and remove emulator instance
            inst = self.emulator_controller.get_instance(name)
            if inst:
                try:
                    self.emulator_controller.stop_instance(name)
                except Exception:
                    pass
                try:
                    self.emulator_controller.remove_instance(name)
                except Exception:
                    pass
            # Remove bot object and config
            if name in self.bots:
                try:
                    del self.bots[name]
                except Exception:
                    pass
                try:
                    self._remove_bot_config(name)
                except Exception:
                    pass
            logger.info(f"Shutdown emulator and bot for {name}")
            return True
        except Exception as e:
            logger.error(f"Error shutting down emulator {name}: {e}")
            return False

    def update_emulator_params(self, name: str, input_mode: Optional[str] = None, adb_port: Optional[int] = None) -> bool:
        """Cập nhật tham số emulator (input_mode/adb_port) cho một bot/instance đang có."""
        try:
            inst = self.emulator_controller.get_instance(name)
            if not inst:
                logger.error(f"Emulator instance {name} not found")
                return False
            if input_mode in ('mouse', 'adb'):
                inst.input_mode = input_mode
            if adb_port:
                try:
                    inst.adb_port = int(adb_port)
                except Exception:
                    pass
            logger.info(f"Updated emulator params for {name}: input_mode={inst.input_mode}, adb_port={inst.adb_port}")
            return True
        except Exception as e:
            logger.error(f"Error updating emulator params for {name}: {e}")
            return False
    
    def update_game_mode_settings(self, mode_settings: Dict[str, Any]):
        """Update game mode settings"""
        try:
            for mode, settings in mode_settings.items():
                if mode in self.game_modes:
                    self.game_modes[mode].update(settings)
            
            # Update all bots
            for bot in self.bots.values():
                bot.update_game_mode_settings(self.game_modes)
            
            logger.info("Updated game mode settings")
            
        except Exception as e:
            logger.error(f"Error updating game mode settings: {e}")
    
    def start_monitoring(self):
        """Start performance monitoring"""
        if not self.monitoring_enabled:
            return
        
        try:
            from utils.performance_monitor import PerformanceMonitor
            self.performance_monitor = PerformanceMonitor()
            self.performance_monitor.start()
            logger.info("Started performance monitoring")
            
        except Exception as e:
            logger.error(f"Error starting performance monitoring: {e}")
    
    def stop_monitoring(self):
        """Stop performance monitoring"""
        if self.performance_monitor:
            self.performance_monitor.stop()
            self.performance_monitor = None
            logger.info("Stopped performance monitoring")
    
    def health_check(self):
        """Perform health check on all bots"""
        for name, bot in self.bots.items():
            try:
                if bot.is_running and not bot.is_healthy():
                    logger.warning(f"Bot {name} is not healthy, restarting...")
                    if self.auto_restart:
                        self.restart_bot(name)
                        
            except Exception as e:
                logger.error(f"Error during health check for bot {name}: {e}")
    
    def start_health_monitoring(self):
        """Start background health monitoring"""
        def monitor():
            while self.is_running:
                self.health_check()
                time.sleep(60)  # Check every minute
        
        monitor_thread = threading.Thread(target=monitor, daemon=True)
        monitor_thread.start()
        logger.info("Started bot health monitoring")
    
    def save_state(self):
        """Save current bot manager state"""
        try:
            state = {
                'bots': {},
                'global_stats': self.global_stats,
                'farming_config': self.farming_config,
                'game_modes': self.game_modes,
                'timestamp': time.time()
            }
            
            for name, bot in self.bots.items():
                state['bots'][name] = {
                    'name': name,
                    'emulator_name': bot.emulator.name,
                    'account_info': bot.account_info,
                    'status': bot.get_status()
                }
            
            state_file = Path(__file__).parent.parent / 'data' / 'bot_manager_state.json'
            state_file.parent.mkdir(exist_ok=True)
            
            with open(state_file, 'w', encoding='utf-8') as f:
                json.dump(state, f, indent=2, ensure_ascii=False)
            
            logger.info("Bot manager state saved")
            
        except Exception as e:
            logger.error(f"Error saving bot manager state: {e}")
    
    def load_state(self):
        """Load bot manager state from file"""
        try:
            state_file = Path(__file__).parent.parent / 'data' / 'bot_manager_state.json'
            
            if not state_file.exists():
                logger.info("No saved state found, starting fresh")
                return
            
            with open(state_file, 'r', encoding='utf-8') as f:
                state = json.load(f)
            
            # Restore global stats
            if 'global_stats' in state:
                self.global_stats.update(state['global_stats'])
            
            # Restore configuration
            if 'farming_config' in state:
                self.farming_config.update(state['farming_config'])
            
            if 'game_modes' in state:
                self.game_modes.update(state['game_modes'])
            
            # Restore bots (they will need to be recreated)
            logger.info("Bot manager state loaded")
            
        except Exception as e:
            logger.error(f"Error loading bot manager state: {e}")
    
    def _save_bot_config(self, name: str, account_info: Dict[str, Any]):
        """Save bot configuration to database"""
        try:
            config_file = Path(__file__).parent.parent / 'data' / f'bot_{name}_config.json'
            config_file.parent.mkdir(exist_ok=True)
            
            config = {
                'name': name,
                'account_info': account_info,
                'created_at': time.time(),
                'last_updated': time.time()
            }
            
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            logger.error(f"Error saving bot config for {name}: {e}")
    
    def _remove_bot_config(self, name: str):
        """Remove bot configuration file"""
        try:
            config_file = Path(__file__).parent.parent / 'data' / f'bot_{name}_config.json'
            if config_file.exists():
                config_file.unlink()
                
        except Exception as e:
            logger.error(f"Error removing bot config for {name}: {e}")
    
    def start(self):
        """Start the bot manager"""
        try:
            if self.is_running:
                logger.warning("Bot manager is already running")
                return False
            
            self.is_running = True
            
            # Start monitoring
            self.start_monitoring()
            self.start_health_monitoring()
            
            # Start all bots
            self.start_all_bots()
            
            logger.info("Bot manager started successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error starting bot manager: {e}")
            self.is_running = False
            return False
    
    def stop(self):
        """Stop the bot manager"""
        try:
            if not self.is_running:
                logger.warning("Bot manager is not running")
                return False
            
            self.is_running = False
            
            # Stop all bots
            self.stop_all_bots()
            
            # Stop monitoring
            self.stop_monitoring()
            
            # Save state
            self.save_state()
            
            logger.info("Bot manager stopped successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error stopping bot manager: {e}")
            return False
    
    def cleanup(self):
        """Cleanup bot manager resources"""
        logger.info("Cleaning up bot manager")
        
        # Stop all bots
        for bot in self.bots.values():
            try:
                bot.cleanup()
            except Exception as e:
                logger.error(f"Error cleaning up bot {bot.name}: {e}")
        
        # Clear bots
        self.bots.clear()
        
        # Stop monitoring
        self.stop_monitoring()
        
        # Save final state
        self.save_state()
        
        logger.info("Bot manager cleanup completed")

    def get_central_data(self) -> list:
        """Return centrally collected data records"""
        try:
            return self.data_collector.get_all()
        except Exception:
            return []

    def clear_central_data(self):
        """Xóa dữ liệu tập trung"""
        self.data_collector.clear()

# Global bot manager instance (lazy)
_bot_manager = None

def get_bot_manager(config: Dict[str, Any] = None) -> BotManager:
    """Get/create a global bot manager instance lazily."""
    global _bot_manager
    if _bot_manager is None:
        if config is None:
            try:
                from config.settings import load_config as _load_cfg
                config = _load_cfg()
            except Exception:
                config = {}
        _bot_manager = BotManager(config)
    return _bot_manager
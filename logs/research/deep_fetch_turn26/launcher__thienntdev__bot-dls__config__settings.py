#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration settings for DLS Auto Bot
"""

import os
from pathlib import Path
from typing import Dict, List, Tuple, Any
import json
import logging

# Base paths
BASE_DIR = Path(__file__).parent.parent
LOGS_DIR = BASE_DIR / 'logs'
SCREENSHOTS_DIR = BASE_DIR / 'screenshots'
MODELS_DIR = BASE_DIR / 'models'

# Create necessary directories
LOGS_DIR.mkdir(exist_ok=True)
SCREENSHOTS_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)

# Emulator settings
EMULATOR_CONFIG = {
    'bluestacks': {
        'executable': r'C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe',
        'adb_port': 5555,
        'window_title': 'BlueStacks',
        'resolution': (1920, 1080),
        'input_mode': 'mouse',  # 'mouse' or 'adb'
        'attach_only': False
    },
    'nox': {
        'executable': r'C:\\Program Files (x86)\\Nox\\bin\\Nox.exe',
        'adb_port': 62001,
        'window_title': 'NoxPlayer',
        'resolution': (1920, 1080),
        'input_mode': 'mouse',
        'attach_only': False
    },
    'ldplayer': {
        'executable': r'C:\\LDPlayer\\LDPlayer9\\dnplayer.exe',
        'adb_port': 5555,
        'window_title': 'LDPlayer',
        'resolution': (1920, 1080),
        'input_mode': 'mouse',
        'attach_only': False
    },
    'gameloop': {
        'executable': r'C:\\Program Files\\GameLoop\\GameLoop.exe',   # chỉnh đúng path
        'adb_port': 5555,                                          # chỉnh đúng port của instance
        'window_title': 'GameLoop',                                 # hoặc tiêu đề thật của cửa sổ
        'resolution': (1280, 720),
        'input_mode': 'adb',                                        # dùng ADB thay chuột
        'attach_only': True
    }
    }

# Game settings
GAME_CONFIG = {
    'package_name': 'com.firsttouchgames.dls7',
    'main_activity': 'com.firsttouchgames.dls7.MainActivity',
    'game_resolution': (1920, 1080),
    'fps': 30,
    'action_delay': 0.1,  # Delay between actions
    'screenshot_interval': 0.5  # Screenshot every 0.5 seconds
}

# Team mapping (for possession labelling)
TEAM_CONFIG = {
    'own_team': 'team_a',  # 'team_a' or 'team_b'
    # Vùng mẫu màu áo (tọa độ tương đối 0..1): (x1, y1, x2, y2)
    # Mặc định lấy gần vòng tròn giữa sân khi giao bóng
    'jersey_sample_regions': {
        'own_player': (0.45, 0.48, 0.50, 0.55),
        'opponent_player': (0.50, 0.48, 0.55, 0.55),
        'own_goalkeeper': (0.05, 0.80, 0.10, 0.95),
        'opponent_goalkeeper': (0.90, 0.05, 0.95, 0.20)
    }
}

# Bot behavior settings
BOT_CONFIG = {
    'learning_enabled': True,
    'decision_threshold': 0.7,  # Confidence threshold for actions
    'max_retry_attempts': 3,
    'adaptive_learning_rate': 0.1,
    'memory_size': 1000,  # Number of game situations to remember
    'performance_threshold': 0.6  # Minimum performance to continue learning
}

# Resource farming settings
FARMING_CONFIG = {
    'gold_target': 15000,
    'diamond_target': 400,
    'auto_restart': True,
    'restart_delay': 300,  # 5 minutes between restarts
    'max_daily_playtime': 14400,  # 4 hours in seconds
    'break_interval': 1800,  # 30 minutes break every 4 hours
}

# Game modes
GAME_MODES = {
    'career': {
        'enabled': True,
        'priority': 1,
        'auto_restart': True
    },
    'live': {
        'enabled': True,
        'priority': 2,
        'auto_restart': True
    },
    'tournament': {
        'enabled': False,
        'priority': 3,
        'auto_restart': False
    }
}

# Control mappings
CONTROLS = {
    'move_joystick': (960, 800),  # Center of movement joystick
    'pass_button': (1600, 800),   # Pass button (A)
    'shoot_button': (1750, 800),  # Shoot button (B)
    'skill_button': (1450, 800),  # Skill button (C)
    'switch_player': (1400, 700), # Switch player button
    'tackle_button': (1300, 800), # Tackle button
    'sprint_button': (1500, 700), # Sprint button
}

# Screen regions for detection
SCREEN_REGIONS = {
    'game_field': (200, 100, 1720, 900),
    'score_display': (800, 50, 1120, 100),
    'time_display': (900, 20, 1020, 50),
    'possession_indicator': (50, 400, 150, 500),
    'ball_position': (800, 400, 1120, 600),
    'ad_popup': (400, 300, 1520, 700),
    'menu_button': (50, 50, 150, 100),
    'continue_button': (800, 700, 1120, 800),
}

# AI/ML settings
AI_CONFIG = {
    'model_type': 'cnn_lstm',  # CNN + LSTM for image + sequence processing
    'input_shape': (224, 224, 3),  # Standard image input size
    'sequence_length': 10,  # Number of frames to consider for decisions
    'learning_rate': 0.001,
    'batch_size': 32,
    'epochs': 100,
    'validation_split': 0.2,
    'early_stopping_patience': 10,
    'model_save_path': str(MODELS_DIR / 'dls_bot_model.h5')
}

# Logging settings
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file_rotation': True,
    'max_file_size': 10 * 1024 * 1024,  # 10MB
    'backup_count': 5
}

# Performance monitoring
PERFORMANCE_CONFIG = {
    'enable_monitoring': True,
    'metrics_interval': 60,  # Collect metrics every minute
    'memory_threshold': 0.8,  # Alert if memory usage > 80%
    'cpu_threshold': 0.9,     # Alert if CPU usage > 90%
    'disk_threshold': 0.9     # Alert if disk usage > 90%
}

# Database settings
DATABASE_CONFIG = {
    'type': 'sqlite',
    'path': str(BASE_DIR / 'data' / 'dls_bot.db'),
    'backup_enabled': True,
    'backup_interval': 86400,  # Daily backup
    'max_backups': 7
}

# Notification settings
NOTIFICATION_CONFIG = {
    'enabled': True,
    'discord_webhook': None,
    'telegram_bot_token': None,
    'telegram_chat_id': None,
    'email_enabled': False,
    'smtp_server': None,
    'smtp_port': 587,
    'smtp_username': None,
    'smtp_password': None,
    'notification_email': None
}

# Development settings
DEV_CONFIG = {
    'debug_mode': False,
    'test_mode': False,
    'mock_emulator': False,
    'save_screenshots': True,
    'save_replays': False,
    'performance_profiling': False
}

# Load environment variables
def load_env_config():
    """Load configuration from environment variables"""
    import os
    
    # Override with environment variables if they exist
    if os.getenv('DLS_BOT_DEBUG'):
        DEV_CONFIG['debug_mode'] = os.getenv('DLS_BOT_DEBUG').lower() == 'true'
    
    if os.getenv('DLS_BOT_LOG_LEVEL'):
        LOGGING_CONFIG['level'] = os.getenv('DLS_BOT_LOG_LEVEL')
    
    if os.getenv('DLS_BOT_GOLD_TARGET'):
        FARMING_CONFIG['gold_target'] = int(os.getenv('DLS_BOT_GOLD_TARGET'))
    
    if os.getenv('DLS_BOT_DIAMOND_TARGET'):
        FARMING_CONFIG['diamond_target'] = int(os.getenv('DLS_BOT_DIAMOND_TARGET'))

# Initialize configuration
load_env_config()

# Hàm load_config gom toàn bộ cấu hình thành dict
def load_config() -> dict:
    """Load full config as dict"""
    return {
        "EMULATOR_CONFIG": EMULATOR_CONFIG,
        "GAME_CONFIG": GAME_CONFIG,
        "TEAM_CONFIG": TEAM_CONFIG,
        "BOT_CONFIG": BOT_CONFIG,
        "FARMING_CONFIG": FARMING_CONFIG,
        "GAME_MODES": GAME_MODES,
        "CONTROLS": CONTROLS,
        "SCREEN_REGIONS": SCREEN_REGIONS,
        "AI_CONFIG": AI_CONFIG,
        "LOGGING_CONFIG": LOGGING_CONFIG,
        "PERFORMANCE_CONFIG": PERFORMANCE_CONFIG,
        "DATABASE_CONFIG": DATABASE_CONFIG,
        "NOTIFICATION_CONFIG": NOTIFICATION_CONFIG,
        "DEV_CONFIG": DEV_CONFIG,
    }

def save_config(config: dict):
    """Dummy save_config (chưa cần thiết nếu chỉ load config từ file)"""
    pass
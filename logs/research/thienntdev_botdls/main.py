#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dream League Soccer Bot - Main Entry Point
Bot tự động chơi game Dream League Soccer với khả năng học máy
"""

import sys
import os
import time
import signal
from pathlib import Path
from typing import Dict, Any
import argparse

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from config.settings import load_config, save_config
from ui.admin_interface import AdminInterface
from utils.logger import get_logger, setup_logging
from utils.performance_monitor import PerformanceMonitor
from core.bot_manager import BotManager

# Initialize logging early to ensure logger is available in all paths
setup_logging()
logger = get_logger(__name__)

def signal_handler(signum, frame):
    """Xử lý signal để thoát an toàn"""
    logger = get_logger(__name__)
    logger.info(f"Received signal {signum}, shutting down gracefully...")
    sys.exit(0)

def setup_signal_handlers():
    """Thiết lập signal handlers"""
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Windows specific signals
    if hasattr(signal, 'SIGBREAK'):
        signal.signal(signal.SIGBREAK, signal_handler)

def check_dependencies():
    """Kiểm tra dependencies cần thiết"""
    logger = get_logger(__name__)
    
    try:
        import cv2
        import numpy as np
        import tkinter as tk
        import threading
        
        logger.info("All required dependencies are available")
        return True
        
    except ImportError as e:
        logger.error(f"Missing required dependency: {e}")
        logger.error("Please install required packages: pip install -r requirements.txt")
        return False

def create_directories():
    """Tạo các thư mục cần thiết"""
    logger = get_logger(__name__)
    
    try:
        directories = [
            'logs',
            'data',
            'assets',
            'assets/ad_templates',
            'config',
            'exports'
        ]
        
        for directory in directories:
            dir_path = project_root / directory
            dir_path.mkdir(exist_ok=True)
            logger.debug(f"Directory created/verified: {dir_path}")
        
        logger.info("All required directories created/verified")
        
    except Exception as e:
        logger.error(f"Error creating directories: {e}")
        return False
    
    return True

def initialize_system(config: Dict[str, Any]):
    """Khởi tạo hệ thống"""
    logger = get_logger(__name__)
    
    try:
        # Create directories
        if not create_directories():
            logger.error("Failed to create required directories")
            return False
        
        # Initialize performance monitor with PERFORMANCE_CONFIG
        performance_monitor = PerformanceMonitor(config.get('PERFORMANCE_CONFIG', {}))
        performance_monitor.start_monitoring()
        
        logger.info("System initialized successfully")
        return True
        
    except Exception as e:
        logger.error(f"Error initializing system: {e}")
        return False

def parse_args():
    parser = argparse.ArgumentParser(description="Dream League Soccer Bot")
    parser.add_argument("--ui", action="store_true", help="Mở giao diện quản lý (Tkinter)")
    parser.add_argument("--bots", type=int, default=4, help="Số lượng cửa sổ/giả lập cần chạy (mặc định: 4)")
    return parser.parse_args()

def main():
    """Hàm chính"""
    bot_manager = None
    try:
        logger.info("=" * 60)
        logger.info("Dream League Soccer Bot - Starting...")
        logger.info("=" * 60)
        
        args = parse_args()

        # Setup signal handlers
        setup_signal_handlers()
        
        # Check dependencies
        if not check_dependencies():
            logger.error("Dependency check failed. Exiting.")
            sys.exit(1)
        
        # Load configuration
        config = load_config()
        if not config:
            logger.error("Failed to load configuration. Exiting.")
            sys.exit(1)
        
        # If --ui flag is passed, start Admin UI and exit
        if args.ui:
            logger.info("Starting Admin Interface (UI) mode...")
            ui = AdminInterface(config)
            ui.start()
            return

        # Optionally enable mock emulator for quick smoke test
        dev_cfg = config.get('DEV_CONFIG', {})
        if 'mock_emulator' in dev_cfg and dev_cfg['mock_emulator']:
            logger.info("DEV: Mock emulator mode enabled")
        
        logger.info("Configuration loaded successfully")
        
        # Initialize system
        if not initialize_system(config):
            logger.error("System initialization failed. Exiting.")
            sys.exit(1)
        
        # Khởi tạo BotManager
        bot_manager = BotManager(config)
        # Danh sách tên emulator (giả sử đã cấu hình sẵn 4 emulator)
        emulator_count = max(1, int(args.bots))
        emulator_names = [f"emulator_{i+1}" for i in range(emulator_count)]
        # Tạo 4 bot, mỗi bot gắn với 1 emulator
        for i, emulator_name in enumerate(emulator_names):
            bot_name = f"bot_{i+1}"
            account_info = {'account_id': f"acc_{i+1}"}
            bot_manager.create_bot(bot_name, emulator_name, account_info)
        # Khởi động tất cả bot
        bot_manager.start_all_bots()
        # (Có thể thêm vòng lặp chính để giám sát hoặc xuất dữ liệu tập trung)
        while True:
            time.sleep(60)
            if bot_manager:
                central_data = bot_manager.get_central_data()
                print(f"[CentralData] Collected {len(central_data)} records so far.")
    except KeyboardInterrupt:
        print("Received keyboard interrupt, shutting down...")
        if bot_manager:
            bot_manager.stop_all_bots()
    except Exception as e:
        print(f"Unexpected error in main: {e}")
        if bot_manager:
            bot_manager.stop_all_bots()
    finally:
        get_logger(__name__).info("Dream League Soccer Bot - Shutdown complete")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Central Data Collector for Multi-Bot AI Training
Gom dữ liệu từ nhiều bot về một nơi để phục vụ training/học hỏi
"""

import threading
import time
from typing import Dict, Any, List
from pathlib import Path
import json

from utils.logger import get_logger

class CentralDataCollector:
    """Gom dữ liệu từ nhiều bot về một nơi"""
    def __init__(self, save_path: str = None):
        self.logger = get_logger(__name__)
        self.data: List[Dict[str, Any]] = []
        self.lock = threading.Lock()
        self.save_path = save_path or str(Path(__file__).parent.parent / 'data' / 'central_data.json')
        self.save_interval = 60  # seconds
        self._start_auto_save()

    def collect(self, record: Dict[str, Any]):
        """Nhận dữ liệu từ một bot"""
        with self.lock:
            self.data.append(record)
        self.logger.debug(f"Collected data from bot: {record.get('bot_id', 'unknown')}")

    def get_all(self) -> List[Dict[str, Any]]:
        with self.lock:
            return list(self.data)

    def clear(self):
        with self.lock:
            self.data.clear()
        self.logger.info("Central data cleared")

    def save(self):
        with self.lock:
            try:
                Path(self.save_path).parent.mkdir(exist_ok=True)
                with open(self.save_path, 'w', encoding='utf-8') as f:
                    json.dump(self.data, f, indent=2, ensure_ascii=False)
                self.logger.info(f"Central data saved to {self.save_path}")
            except Exception as e:
                self.logger.error(f"Error saving central data: {e}")

    def load(self):
        try:
            if Path(self.save_path).exists():
                with open(self.save_path, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
                self.logger.info(f"Central data loaded from {self.save_path}")
        except Exception as e:
            self.logger.error(f"Error loading central data: {e}")

    def _start_auto_save(self):
        def auto_save_loop():
            while True:
                time.sleep(self.save_interval)
                self.save()
        t = threading.Thread(target=auto_save_loop, daemon=True)
        t.start() 
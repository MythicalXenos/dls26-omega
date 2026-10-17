#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Input Scheduler - xếp hàng thao tác chuột/drag để tránh tranh focus khi nhiều bot
"""

import threading
import time
from queue import Queue, Empty
from typing import Callable

from utils.logger import get_logger


class InputScheduler:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.queue: "Queue[Callable[[], None]]" = Queue()
        self.thread = threading.Thread(target=self._worker, daemon=True)
        self.running = False

    def start(self):
        if self.running:
            return
        self.running = True
        self.thread.start()
        self.logger.info("InputScheduler started")

    def stop(self):
        self.running = False
        try:
            self.queue.put_nowait(lambda: None)
        except Exception:
            pass

    def schedule(self, fn: Callable[[], None]):
        try:
            self.queue.put_nowait(fn)
        except Exception as e:
            self.logger.error(f"Failed to schedule input: {e}")

    def _worker(self):
        while self.running:
            try:
                fn = self.queue.get(timeout=0.2)
            except Empty:
                continue
            try:
                fn()
            except Exception as e:
                self.logger.error(f"Error executing input task: {e}")
            finally:
                # short spacing to avoid focus contention
                time.sleep(0.03)


_scheduler = InputScheduler()


def get_input_scheduler() -> InputScheduler:
    _scheduler.start()
    return _scheduler



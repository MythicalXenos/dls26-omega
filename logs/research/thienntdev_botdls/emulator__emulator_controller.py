#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Emulator Controller for DLS Auto Bot
Manages multiple emulator instances and their connections
"""

import subprocess
import time
import psutil
import os
import win32gui
import win32con
import win32api
import win32process
from typing import Dict, List, Optional, Tuple
from pathlib import Path
import logging

from config.settings import EMULATOR_CONFIG
from utils.logger import get_logger

logger = get_logger(__name__)

class EmulatorInstance:
    """Represents a single emulator instance"""
    
    def __init__(self, name: str, emulator_type: str, instance_id: int = 0):
        self.name = name
        self.emulator_type = emulator_type
        self.instance_id = instance_id
        self.process = None
        self.window_handle = None
        self.adb_port = None
        self.is_running = False
        self.is_connected = False
        self.last_activity = time.time()
        self.status = "stopped"
        
        # Get configuration for this emulator type
        self.config = EMULATOR_CONFIG.get(emulator_type, {})
        if self.config:
            self.adb_port = self.config.get('adb_port', 5555) + instance_id
            self.executable = self.config.get('executable', '')
            self.window_title = self.config.get('window_title', '')
            self.resolution = self.config.get('resolution', (1920, 1080))
            self.input_mode = self.config.get('input_mode', 'mouse')
        else:
            self.executable = ''
            self.window_title = ''
            self.resolution = (1920, 1080)
            self.input_mode = 'mouse'
        
        # Mock mode only if explicitly requested via type
        self.mock_mode = (self.emulator_type.lower() == 'mock')

    def start(self) -> bool:
        """Start the emulator instance"""
        try:
            if self.mock_mode:
                logger.warning(f"{self.name}: starting in MOCK mode (executable not found or emulator_type=mock)")
                self.is_running = True
                self.status = "running"
                # Try to find any matching window, but allow operations without it
                self._find_window()
                return True
            
            # If config set to attach_only, skip launching and just attach
            if self.config.get('attach_only'):
                if self._find_window():
                    self.is_running = True
                    self.status = "running"
                    return True
                else:
                    logger.error(f"{self.name}: attach_only is True but window not found")
                    return False

            if not self.executable or not Path(self.executable).exists():
                logger.error(f"Emulator executable not found: {self.executable}")
                return False
            
            # Start emulator process
            cmd = [self.executable]
            if self.instance_id > 0:
                cmd.extend(['--instance', str(self.instance_id)])
            
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            
            logger.info(f"Started {self.name} (PID: {self.process.pid})")
            self.is_running = True
            self.status = "starting"
            
            # Wait for emulator to fully start
            time.sleep(30)  # Give emulator time to boot
            
            # Find and connect to window
            if self._find_window():
                self.status = "running"
                return True
            else:
                logger.error(f"Could not find window for {self.name}")
                self.stop()
                return False
                
        except Exception as e:
            logger.error(f"Error starting {self.name}: {e}")
            self.status = "error"
            return False
    
    def stop(self) -> bool:
        """Stop the emulator instance"""
        try:
            if self.process and self.process.poll() is None:
                self.process.terminate()
                time.sleep(5)
                
                if self.process.poll() is None:
                    self.process.kill()
                
                logger.info(f"Stopped {self.name}")
            
            self.is_running = False
            self.is_connected = False
            self.status = "stopped"
            self.window_handle = None
            return True
            
        except Exception as e:
            logger.error(f"Error stopping {self.name}: {e}")
            return False
    
    def restart(self) -> bool:
        """Restart the emulator instance"""
        logger.info(f"Restarting {self.name}")
        if self.stop():
            time.sleep(5)
            return self.start()
        return False
    
    def _find_window(self) -> bool:
        """Find the emulator window"""
        def enum_windows_callback(hwnd, windows):
            if win32gui.IsWindowVisible(hwnd):
                window_text = win32gui.GetWindowText(hwnd)
                if self.window_title.lower() in window_text.lower():
                    windows.append(hwnd)
            return True
        
        if self.mock_mode:
            # In mock mode, skip strict window requirement
            return True
        
        windows = []
        win32gui.EnumWindows(enum_windows_callback, windows)
        
        if windows:
            self.window_handle = windows[0]
            return True
        return False
    
    def focus_window(self) -> bool:
        """Bring emulator window to front"""
        try:
            if self.mock_mode:
                return True
            if self.window_handle:
                win32gui.ShowWindow(self.window_handle, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(self.window_handle)
                return True
        except Exception as e:
            logger.error(f"Error focusing window for {self.name}: {e}")
        return False

    def is_window_active(self) -> bool:
        """Check if emulator window is active (foreground)"""
        try:
            if self.mock_mode:
                return True
            if not self.window_handle:
                return False
            return win32gui.GetForegroundWindow() == self.window_handle
        except Exception:
            return False

    def get_window_rect(self) -> Optional[Tuple[int, int, int, int]]:
        """Get emulator window rectangle"""
        try:
            if self.mock_mode or not self.window_handle:
                # Fall back to primary screen area
                width = win32api.GetSystemMetrics(0)
                height = win32api.GetSystemMetrics(1)
                return (0, 0, width, height)
            if self.window_handle:
                return win32gui.GetWindowRect(self.window_handle)
        except Exception as e:
            logger.error(f"Error getting window rect for {self.name}: {e}")
        return None

    def click(self, x: float, y: float) -> bool:
        """Click within the emulator window. Accepts normalized (0..1) or absolute coords."""
        try:
            from core.input_scheduler import get_input_scheduler
            rect = self.get_window_rect()
            if not rect:
                return False
            left, top, right, bottom = rect
            width = right - left
            height = bottom - top
            cx = x if x > 1 else left + int(x * width)
            cy = y if y > 1 else top + int(y * height)

            if self.input_mode == 'adb' and self.adb_port:
                def _do():
                    os.system(f"adb -s 127.0.0.1:{self.adb_port} shell input tap {cx} {cy}")
                get_input_scheduler().schedule(_do)
            else:
                import pyautogui
                def _do():
                    pyautogui.moveTo(cx, cy)
                    pyautogui.click()
                get_input_scheduler().schedule(_do)
            self.last_activity = time.time()
            return True
        except Exception as e:
            logger.error(f"Error clicking in {self.name}: {e}")
            return False

    def drag(self, start_x: float, start_y: float, end_x: float, end_y: float, duration: float = 0.2) -> bool:
        """Drag within the emulator window using normalized or absolute coords."""
        try:
            from core.input_scheduler import get_input_scheduler
            rect = self.get_window_rect()
            if not rect:
                return False
            left, top, right, bottom = rect
            width = right - left
            height = bottom - top
            sx = start_x if start_x > 1 else left + int(start_x * width)
            sy = start_y if start_y > 1 else top + int(start_y * height)
            ex = end_x if end_x > 1 else left + int(end_x * width)
            ey = end_y if end_y > 1 else top + int(end_y * height)

            if self.input_mode == 'adb' and self.adb_port:
                duration_ms = max(1, int(duration * 1000))
                def _do():
                    os.system(f"adb -s 127.0.0.1:{self.adb_port} shell input swipe {sx} {sy} {ex} {ey} {duration_ms}")
                get_input_scheduler().schedule(_do)
            else:
                import pyautogui
                def _do():
                    pyautogui.moveTo(sx, sy)
                    pyautogui.dragTo(ex, ey, duration=duration)
                get_input_scheduler().schedule(_do)
            self.last_activity = time.time()
            return True
        except Exception as e:
            logger.error(f"Error dragging in {self.name}: {e}")
            return False

    def take_screenshot(self) -> Optional[str]:
        """Take a screenshot of the emulator window, return file path."""
        try:
            from datetime import datetime
            from pathlib import Path
            import pyautogui
            
            rect = self.get_window_rect()
            if not rect:
                return None
            left, top, right, bottom = rect
            width = right - left
            height = bottom - top
            img = pyautogui.screenshot(region=(left, top, width, height))
            screenshots_dir = Path(__file__).parent.parent / 'screenshots'
            screenshots_dir.mkdir(exist_ok=True)
            fname = screenshots_dir / f"{self.name}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.png"
            img.save(str(fname))
            return str(fname)
        except Exception as e:
            logger.error(f"Error taking screenshot in {self.name}: {e}")
            return None

    def capture_frame(self):
        """Capture a frame as a NumPy BGR image array for fast processing (no disk IO)."""
        try:
            import pyautogui
            import numpy as np
            import cv2
            rect = self.get_window_rect()
            if not rect:
                return None
            left, top, right, bottom = rect
            width = right - left
            height = bottom - top
            img = pyautogui.screenshot(region=(left, top, width, height))
            img = np.array(img)  # RGB
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            return img
        except Exception as e:
            logger.error(f"Error capturing frame in {self.name}: {e}")
            return None

    # Absolute-coordinate helpers (pixels)
    def click_at(self, x: int, y: int, duration: float = 0.05) -> bool:
        try:
            from core.input_scheduler import get_input_scheduler
            if self.input_mode == 'adb' and self.adb_port:
                def _do():
                    os.system(f"adb -s 127.0.0.1:{self.adb_port} shell input tap {int(x)} {int(y)}")
                get_input_scheduler().schedule(_do)
                return True
            else:
                import pyautogui
                def _do():
                    pyautogui.moveTo(int(x), int(y))
                    pyautogui.mouseDown(); time.sleep(max(0.01, duration)); pyautogui.mouseUp()
                get_input_scheduler().schedule(_do)
                return True
        except Exception as e:
            logger.error(f"Error click_at in {self.name}: {e}")
            return False

    def drag_to(self, sx: int, sy: int, ex: int, ey: int, duration: float = 0.2) -> bool:
        try:
            from core.input_scheduler import get_input_scheduler
            if self.input_mode == 'adb' and self.adb_port:
                dur_ms = max(1, int(duration * 1000))
                def _do():
                    os.system(f"adb -s 127.0.0.1:{self.adb_port} shell input swipe {int(sx)} {int(sy)} {int(ex)} {int(ey)} {dur_ms}")
                get_input_scheduler().schedule(_do)
                return True
            else:
                import pyautogui
                def _do():
                    pyautogui.moveTo(int(sx), int(sy))
                    pyautogui.dragTo(int(ex), int(ey), duration=duration)
                get_input_scheduler().schedule(_do)
                return True
        except Exception as e:
            logger.error(f"Error drag_to in {self.name}: {e}")
            return False
    
    def is_responsive(self) -> bool:
        """Check if emulator is responsive"""
        try:
            if self.mock_mode:
                return True
            if self.process and self.process.poll() is None:
                # Check if window responds to messages
                if self.window_handle:
                    return win32gui.IsWindow(self.window_handle)
            return False
        except:
            return False
    
    def get_status_info(self) -> Dict:
        """Get current status information"""
        return {
            'name': self.name,
            'type': self.emulator_type,
            'instance_id': self.instance_id,
            'status': self.status,
            'is_running': self.is_running,
            'is_connected': self.is_connected,
            'pid': self.process.pid if self.process else None,
            'adb_port': self.adb_port,
            'last_activity': self.last_activity,
            'memory_usage': self._get_memory_usage(),
            'cpu_usage': self._get_cpu_usage()
        }
    
    def _get_memory_usage(self) -> float:
        """Get memory usage in MB"""
        try:
            if self.process:
                process = psutil.Process(self.process.pid)
                return process.memory_info().rss / 1024 / 1024
        except:
            pass
        return 0.0
    
    def _get_cpu_usage(self) -> float:
        """Get CPU usage percentage"""
        try:
            if self.process:
                process = psutil.Process(self.process.pid)
                return process.cpu_percent()
        except:
            pass
        return 0.0

class EmulatorController:
    """Manages multiple emulator instances"""
    
    def __init__(self):
        self.instances: Dict[str, EmulatorInstance] = {}
        self.max_instances = 5
        self.auto_restart = True
        self.health_check_interval = 60  # seconds
        
    def create_instance(self, name: str, emulator_type: str, instance_id: int = 0) -> Optional[EmulatorInstance]:
        """Create a new emulator instance"""
        if len(self.instances) >= self.max_instances:
            logger.warning(f"Maximum instances ({self.max_instances}) reached")
            return None
        
        if name in self.instances:
            logger.warning(f"Instance {name} already exists")
            return None
        
        instance = EmulatorInstance(name, emulator_type, instance_id)
        self.instances[name] = instance
        logger.info(f"Created emulator instance: {name}")
        return instance
    
    def start_instance(self, name: str) -> bool:
        """Start a specific emulator instance"""
        if name not in self.instances:
            logger.error(f"Instance {name} not found")
            return False
        
        instance = self.instances[name]
        return instance.start()
    
    def stop_instance(self, name: str) -> bool:
        """Stop a specific emulator instance"""
        if name not in self.instances:
            logger.error(f"Instance {name} not found")
            return False
        
        instance = self.instances[name]
        return instance.stop()
    
    def restart_instance(self, name: str) -> bool:
        """Restart a specific emulator instance"""
        if name not in self.instances:
            logger.error(f"Instance {name} not found")
            return False
        
        instance = self.instances[name]
        return instance.restart()
    
    def start_all(self) -> Dict[str, bool]:
        """Start all emulator instances"""
        results = {}
        for name, instance in self.instances.items():
            results[name] = instance.start()
            time.sleep(10)  # Delay between starts to avoid resource conflicts
        return results
    
    def stop_all(self) -> Dict[str, bool]:
        """Stop all emulator instances"""
        results = {}
        for name, instance in self.instances.items():
            results[name] = instance.stop()
        return results
    
    def restart_all(self) -> Dict[str, bool]:
        """Restart all emulator instances"""
        results = {}
        for name, instance in self.instances.items():
            results[name] = instance.restart()
            time.sleep(10)
        return results
    
    def remove_instance(self, name: str) -> bool:
        """Remove an emulator instance"""
        if name not in self.instances:
            return False
        
        instance = self.instances[name]
        instance.stop()
        del self.instances[name]
        logger.info(f"Removed emulator instance: {name}")
        return True
    
    def get_instance(self, name: str) -> Optional[EmulatorInstance]:
        """Get a specific emulator instance"""
        return self.instances.get(name)
    
    def get_all_instances(self) -> Dict[str, EmulatorInstance]:
        """Get all emulator instances"""
        return self.instances.copy()
    
    def get_running_instances(self) -> Dict[str, EmulatorInstance]:
        """Get all running emulator instances"""
        return {name: instance for name, instance in self.instances.items() 
                if instance.is_running}
    
    def get_instance_status(self, name: str) -> Optional[Dict]:
        """Get status of a specific instance"""
        if name in self.instances:
            return self.instances[name].get_status_info()
        return None
    
    def get_all_status(self) -> Dict[str, Dict]:
        """Get status of all instances"""
        return {name: instance.get_status_info() 
                for name, instance in self.instances.items()}
    
    def health_check(self):
        """Perform health check on all instances"""
        for name, instance in self.instances.items():
            if instance.is_running and not instance.is_responsive():
                logger.warning(f"Instance {name} is not responsive, restarting...")
                if self.auto_restart:
                    instance.restart()
    
    def start_health_monitoring(self):
        """Start background health monitoring"""
        import threading
        
        def monitor():
            while True:
                self.health_check()
                time.sleep(self.health_check_interval)
        
        monitor_thread = threading.Thread(target=monitor, daemon=True)
        monitor_thread.start()
        logger.info("Started emulator health monitoring")
    
    def cleanup(self):
        """Cleanup all instances"""
        logger.info("Cleaning up emulator controller")
        self.stop_all()
        self.instances.clear()

# Global emulator controller instance
emulator_controller = EmulatorController()

def get_emulator_controller() -> EmulatorController:
    """Get the global emulator controller instance"""
    return emulator_controller 
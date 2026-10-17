#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Resource Manager - Quản lý tài nguyên và mục tiêu cày
"""

import json
import time
from typing import Dict, Any, Optional, List
from pathlib import Path

from utils.logger import get_logger, BotLogger

class ResourceManager:
    """Quản lý tài nguyên và mục tiêu cày cho các account"""
    
    def __init__(self, config: dict):
        self.config = config
        self.logger = get_logger(__name__)
        
        # Resource targets for each account
        self.resource_targets: Dict[str, Dict[str, int]] = {}
        
        # Current resource status
        self.current_resources: Dict[str, Dict[str, int]] = {}
        
        # Farming history
        self.farming_history: Dict[str, List[Dict[str, Any]]] = {}
        
        # Load or create default targets
        self._load_resource_targets()
        
        self.logger.info("Resource Manager initialized")
    
    def _load_resource_targets(self):
        """Tải mục tiêu tài nguyên từ file hoặc tạo mặc định"""
        try:
            config_file = Path(__file__).parent.parent / 'config' / 'resource_targets.json'
            
            if config_file.exists():
                with open(config_file, 'r', encoding='utf-8') as f:
                    self.resource_targets = json.load(f)
                self.logger.info("Resource targets loaded from file")
            else:
                # Create default targets
                self._create_default_targets()
                self._save_resource_targets()
                self.logger.info("Default resource targets created")
                
        except Exception as e:
            self.logger.error(f"Error loading resource targets: {e}")
            self._create_default_targets()
    
    def _create_default_targets(self):
        """Tạo mục tiêu tài nguyên mặc định"""
        default_targets = self.config.get('resource', {}).get('DEFAULT_TARGETS', {})
        
        self.resource_targets = {
            'default': {
                'gold': default_targets.get('gold', 15000),
                'diamonds': default_targets.get('diamonds', 400)
            }
        }
    
    def _save_resource_targets(self):
        """Lưu mục tiêu tài nguyên vào file"""
        try:
            config_file = Path(__file__).parent.parent / 'config' / 'resource_targets.json'
            config_file.parent.mkdir(exist_ok=True)
            
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(self.resource_targets, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Error saving resource targets: {e}")
    
    def set_resource_targets(self, account_name: str, gold: int, diamonds: int) -> bool:
        """Thiết lập mục tiêu tài nguyên cho account"""
        try:
            self.resource_targets[account_name] = {
                'gold': max(0, gold),
                'diamonds': max(0, diamonds)
            }
            
            self._save_resource_targets()
            self.logger.info(f"Set targets for {account_name}: Gold={gold}, Diamonds={diamonds}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error setting resource targets: {e}")
            return False
    
    def get_targets(self, account_name: str) -> Optional[Dict[str, int]]:
        """Lấy mục tiêu tài nguyên cho account"""
        try:
            # Return specific account targets if available
            if account_name in self.resource_targets:
                return self.resource_targets[account_name].copy()
            
            # Return default targets if no specific ones
            return self.resource_targets.get('default', {}).copy()
            
        except Exception as e:
            self.logger.error(f"Error getting targets for {account_name}: {e}")
            return None
    
    def update_current_resources(self, account_name: str, resources: Dict[str, int]) -> bool:
        """Cập nhật tài nguyên hiện tại cho account"""
        try:
            if account_name not in self.current_resources:
                self.current_resources[account_name] = {}
            
            old_resources = self.current_resources[account_name].copy()
            
            # Update resources
            for resource_type, new_value in resources.items():
                old_value = old_resources.get(resource_type, 0)
                self.current_resources[account_name][resource_type] = new_value
                
                # Log resource changes
                if new_value != old_value:
                    self._log_resource_change(account_name, resource_type, old_value, new_value)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error updating resources for {account_name}: {e}")
            return False
    
    def _log_resource_change(self, account_name: str, resource_type: str, old_value: int, new_value: int):
        """Ghi log thay đổi tài nguyên"""
        try:
            change = new_value - old_value
            change_str = f"+{change}" if change > 0 else str(change)
            
            self.logger.info(f"Resource update for {account_name}: {resource_type} {old_value} -> {new_value} ({change_str})")
            
            # Add to farming history
            if account_name not in self.farming_history:
                self.farming_history[account_name] = []
            
            history_entry = {
                'timestamp': time.time(),
                'resource_type': resource_type,
                'old_value': old_value,
                'new_value': new_value,
                'change': change
            }
            
            self.farming_history[account_name].append(history_entry)
            
            # Keep only last 100 entries
            if len(self.farming_history[account_name]) > 100:
                self.farming_history[account_name] = self.farming_history[account_name][-100:]
                
        except Exception as e:
            self.logger.error(f"Error logging resource change: {e}")
    
    def get_current_resources(self, account_name: str) -> Optional[Dict[str, int]]:
        """Lấy tài nguyên hiện tại cho account"""
        try:
            return self.current_resources.get(account_name, {}).copy()
            
        except Exception as e:
            self.logger.error(f"Error getting current resources for {account_name}: {e}")
            return None
    
    def check_targets_reached(self, account_name: str) -> Dict[str, bool]:
        """Kiểm tra xem account đã đạt mục tiêu chưa"""
        try:
            targets = self.get_targets(account_name)
            current = self.get_current_resources(account_name)
            
            if not targets or not current:
                return {}
            
            results = {}
            for resource_type in ['gold', 'diamonds']:
                target_value = targets.get(resource_type, 0)
                current_value = current.get(resource_type, 0)
                
                if target_value > 0:
                    results[resource_type] = current_value >= target_value
                else:
                    results[resource_type] = True  # No target set
            
            return results
            
        except Exception as e:
            self.logger.error(f"Error checking targets for {account_name}: {e}")
            return {}
    
    def get_farming_progress(self, account_name: str) -> Dict[str, float]:
        """Lấy tiến độ cày tài nguyên cho account"""
        try:
            targets = self.get_targets(account_name)
            current = self.get_current_resources(account_name)
            
            if not targets or not current:
                return {}
            
            progress = {}
            for resource_type in ['gold', 'diamonds']:
                target_value = targets.get(resource_type, 0)
                current_value = current.get(resource_type, 0)
                
                if target_value > 0:
                    progress[resource_type] = min(100.0, (current_value / target_value) * 100)
                else:
                    progress[resource_type] = 100.0  # No target set
            
            return progress
            
        except Exception as e:
            self.logger.error(f"Error getting farming progress for {account_name}: {e}")
            return {}
    
    def get_farming_stats(self, account_name: str) -> Dict[str, Any]:
        """Lấy thống kê cày tài nguyên cho account"""
        try:
            current = self.get_current_resources(account_name)
            targets = self.get_targets(account_name)
            progress = self.get_farming_progress(account_name)
            targets_reached = self.check_targets_reached(account_name)
            
            # Calculate farming efficiency
            history = self.farming_history.get(account_name, [])
            total_earned = {'gold': 0, 'diamonds': 0}
            
            for entry in history:
                if entry['change'] > 0:
                    resource_type = entry['resource_type']
                    total_earned[resource_type] += entry['change']
            
            return {
                'current_resources': current,
                'targets': targets,
                'progress': progress,
                'targets_reached': targets_reached,
                'total_earned': total_earned,
                'history_count': len(history)
            }
            
        except Exception as e:
            self.logger.error(f"Error getting farming stats for {account_name}: {e}")
            return {}
    
    def update_all_accounts(self):
        """Cập nhật tất cả các account (được gọi định kỳ)"""
        try:
            # This method would typically scan all active accounts
            # and update their resource status
            pass
            
        except Exception as e:
            self.logger.error(f"Error updating all accounts: {e}")
    
    def get_all_accounts_status(self) -> Dict[str, Dict[str, Any]]:
        """Lấy trạng thái của tất cả các account"""
        try:
            status = {}
            
            for account_name in self.resource_targets:
                if account_name != 'default':
                    status[account_name] = self.get_farming_stats(account_name)
            
            return status
            
        except Exception as e:
            self.logger.error(f"Error getting all accounts status: {e}")
            return {}
    
    def reset_account_progress(self, account_name: str) -> bool:
        """Reset tiến độ cày tài nguyên cho account"""
        try:
            if account_name in self.current_resources:
                del self.current_resources[account_name]
            
            if account_name in self.farming_history:
                del self.farming_history[account_name]
            
            self.logger.info(f"Reset progress for account: {account_name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error resetting progress for {account_name}: {e}")
            return False
    
    def export_farming_data(self, file_path: str) -> bool:
        """Xuất dữ liệu cày tài nguyên ra file"""
        try:
            export_data = {
                'export_timestamp': time.time(),
                'resource_targets': self.resource_targets,
                'current_resources': self.current_resources,
                'farming_history': self.farming_history
            }
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Farming data exported to: {file_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error exporting farming data: {e}")
            return False
    
    def import_farming_data(self, file_path: str) -> bool:
        """Nhập dữ liệu cày tài nguyên từ file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                import_data = json.load(f)
            
            # Validate import data
            required_keys = ['resource_targets', 'current_resources', 'farming_history']
            if not all(key in import_data for key in required_keys):
                raise ValueError("Invalid import data format")
            
            # Import data
            self.resource_targets = import_data['resource_targets']
            self.current_resources = import_data['current_resources']
            self.farming_history = import_data['farming_history']
            
            # Save to file
            self._save_resource_targets()
            
            self.logger.info(f"Farming data imported from: {file_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error importing farming data: {e}")
            return False 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Natural Language Processing System for Dream League Soccer Bot
Hệ thống xử lý ngôn ngữ tự nhiên để hiểu lệnh và giao tiếp
"""

import re
import json
import time
from typing import Dict, Any, List, Tuple, Optional, Union
from pathlib import Path
from collections import defaultdict, deque
import threading

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
NLTK_AVAILABLE = True

import spacy
SPACY_AVAILABLE = True

from utils.logger import get_logger, log_performance

class VietnameseLanguageProcessor:
    """Xử lý ngôn ngữ tiếng Việt"""
    
    def __init__(self):
        self.logger = get_logger(__name__)
        
        # Vietnamese stop words
        self.vietnamese_stop_words = {
            'là', 'của', 'và', 'với', 'trong', 'ngoài', 'trên', 'dưới', 'trước', 'sau',
            'bên', 'cạnh', 'giữa', 'xung', 'quanh', 'theo', 'cùng', 'về', 'từ', 'đến',
            'cho', 'vì', 'do', 'bởi', 'tại', 'ở', 'tại', 'nơi', 'chỗ', 'đây', 'đó',
            'kia', 'này', 'ấy', 'nọ', 'kìa', 'đâu', 'nào', 'sao', 'thế', 'nào',
            'có', 'không', 'chưa', 'đã', 'sẽ', 'đang', 'vừa', 'mới', 'còn', 'hết',
            'rồi', 'xong', 'thôi', 'đủ', 'thiếu', 'dư', 'thừa', 'vậy', 'thế', 'như',
            'nhưng', 'mà', 'hoặc', 'hay', 'nếu', 'thì', 'nếu', 'không', 'thì', 'cũng',
            'cả', 'tất', 'cả', 'mỗi', 'mọi', 'bất', 'kỳ', 'một', 'hai', 'ba', 'bốn',
            'năm', 'sáu', 'bảy', 'tám', 'chín', 'mười', 'trăm', 'nghìn', 'triệu', 'tỷ'
        }
        
        # Vietnamese game-specific vocabulary
        self.game_vocabulary = {
            'actions': {
                'tiếng_việt': {
                    'pass': ['chuyền', 'chuyền bóng', 'truyền', 'truyền bóng'],
                    'shoot': ['sút', 'sút bóng', 'đá', 'đá bóng'],
                    'dribble': ['dẫn', 'dẫn bóng', 'lái', 'lái bóng'],
                    'tackle': ['tắc', 'tắc bóng', 'cướp', 'cướp bóng'],
                    'clear': ['phá', 'phá bóng', 'đá ra', 'đá đi'],
                    'defend': ['phòng thủ', 'phòng ngự', 'bảo vệ'],
                    'attack': ['tấn công', 'tấn công', 'tiến công']
                },
                'tiếng_anh': {
                    'pass': ['pass', 'passing', 'pass the ball'],
                    'shoot': ['shoot', 'shooting', 'shoot the ball'],
                    'dribble': ['dribble', 'dribbling', 'dribble the ball'],
                    'tackle': ['tackle', 'tackling', 'steal the ball'],
                    'clear': ['clear', 'clearing', 'kick away'],
                    'defend': ['defend', 'defending', 'defense'],
                    'attack': ['attack', 'attacking', 'offense']
                }
            },
            'positions': {
                'tiếng_việt': {
                    'defense': ['phòng thủ', 'hậu vệ', 'phòng ngự'],
                    'midfield': ['giữa sân', 'tiền vệ', 'trung tâm'],
                    'attack': ['tấn công', 'tiền đạo', 'tiền vệ cánh']
                },
                'tiếng_anh': {
                    'defense': ['defense', 'defender', 'back'],
                    'midfield': ['midfield', 'midfielder', 'center'],
                    'attack': ['attack', 'forward', 'striker']
                }
            },
            'tactics': {
                'tiếng_việt': {
                    'possession': ['kiểm soát bóng', 'giữ bóng', 'sở hữu bóng'],
                    'counter_attack': ['phản công', 'tấn công nhanh', 'phản công nhanh'],
                    'high_press': ['ép cao', 'áp sát cao', 'gây áp lực cao'],
                    'low_block': ['chặn thấp', 'phòng thủ thấp', 'chặn gần khung thành']
                },
                'tiếng_anh': {
                    'possession': ['possession', 'keep the ball', 'ball control'],
                    'counter_attack': ['counter attack', 'fast break', 'quick attack'],
                    'high_press': ['high press', 'high pressure', 'pressing high'],
                    'low_block': ['low block', 'deep defense', 'defensive block']
                }
            }
        }
        
        # Initialize NLTK if available
        if NLTK_AVAILABLE:
            try:
                nltk.download('punkt', quiet=True)
                nltk.download('stopwords', quiet=True)
                nltk.download('wordnet', quiet=True)
                self.lemmatizer = WordNetLemmatizer()
                self.stemmer = PorterStemmer()
            except Exception as e:
                self.logger.warning(f"Could not initialize NLTK: {e}")
        
        self.logger.info("Vietnamese Language Processor initialized")
    
    def preprocess_text(self, text: str, language: str = 'auto') -> str:
        """Tiền xử lý văn bản"""
        try:
            # Detect language if auto
            if language == 'auto':
                language = self._detect_language(text)
            
            # Convert to lowercase
            text = text.lower()
            
            # Remove special characters but keep Vietnamese diacritics
            if language == 'tiếng_việt':
                text = re.sub(r'[^\w\sàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ\s]', ' ', text)
            else:
                text = re.sub(r'[^\w\s]', ' ', text)
            
            # Remove extra whitespace
            text = re.sub(r'\s+', ' ', text).strip()
            
            return text
            
        except Exception as e:
            self.logger.error(f"Error preprocessing text: {e}")
            return text
    
    def _detect_language(self, text: str) -> str:
        """Tự động phát hiện ngôn ngữ"""
        try:
            # Simple heuristic based on Vietnamese characters
            vietnamese_chars = 'àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ'
            
            vietnamese_count = sum(1 for char in text if char in vietnamese_chars)
            total_chars = len([char for char in text if char.isalpha()])
            
            if total_chars > 0 and vietnamese_count / total_chars > 0.1:
                return 'tiếng_việt'
            else:
                return 'tiếng_anh'
                
        except Exception as e:
            self.logger.error(f"Error detecting language: {e}")
            return 'tiếng_anh'
    
    def tokenize_text(self, text: str, language: str = 'auto') -> List[str]:
        """Tokenize văn bản"""
        try:
            # Detect language if auto
            if language == 'auto':
                language = self._detect_language(text)
            
            # Preprocess text
            processed_text = self.preprocess_text(text, language)
            
            if NLTK_AVAILABLE:
                # Use NLTK tokenization
                tokens = word_tokenize(processed_text)
            else:
                # Simple tokenization
                tokens = processed_text.split()
            
            # Remove stop words
            if language == 'tiếng_việt':
                tokens = [token for token in tokens if token not in self.vietnamese_stop_words]
            else:
                # English stop words
                if NLTK_AVAILABLE:
                    english_stop_words = set(stopwords.words('english'))
                    tokens = [token for token in tokens if token not in english_stop_words]
            
            return tokens
            
        except Exception as e:
            self.logger.error(f"Error tokenizing text: {e}")
            return text.split()
    
    def extract_game_commands(self, text: str) -> List[Dict[str, Any]]:
        """Trích xuất lệnh game từ văn bản"""
        try:
            commands = []
            
            # Tokenize text
            tokens = self.tokenize_text(text)
            
            # Check for action commands
            for action, keywords in self.game_vocabulary['actions']['tiếng_việt'].items():
                for keyword in keywords:
                    if keyword in text.lower():
                        commands.append({
                            'type': 'action',
                            'action': action,
                            'confidence': 0.9,
                            'source': 'vietnamese_keyword',
                            'keyword': keyword
                        })
                        break
            
            # Check for position commands
            for position, keywords in self.game_vocabulary['positions']['tiếng_việt'].items():
                for keyword in keywords:
                    if keyword in text.lower():
                        commands.append({
                            'type': 'position',
                            'position': position,
                            'confidence': 0.8,
                            'source': 'vietnamese_keyword',
                            'keyword': keyword
                        })
                        break
            
            # Check for tactic commands
            for tactic, keywords in self.game_vocabulary['tactics']['tiếng_việt'].items():
                for keyword in keywords:
                    if keyword in text.lower():
                        commands.append({
                            'type': 'tactic',
                            'tactic': tactic,
                            'confidence': 0.85,
                            'source': 'vietnamese_keyword',
                            'keyword': keyword
                        })
                        break
            
            # Check for English commands as well
            for action, keywords in self.game_vocabulary['actions']['tiếng_anh'].items():
                for keyword in keywords:
                    if keyword in text.lower():
                        commands.append({
                            'type': 'action',
                            'action': action,
                            'confidence': 0.85,
                            'source': 'english_keyword',
                            'keyword': keyword
                        })
                        break
            
            return commands
            
        except Exception as e:
            self.logger.error(f"Error extracting game commands: {e}")
            return []
    
    def understand_intent(self, text: str) -> Dict[str, Any]:
        """Hiểu ý định của người dùng"""
        try:
            intent = {
                'text': text,
                'language': self._detect_language(text),
                'commands': self.extract_game_commands(text),
                'confidence': 0.0,
                'intent_type': 'unknown'
            }
            
            # Analyze intent based on commands
            if intent['commands']:
                # Calculate overall confidence
                confidences = [cmd['confidence'] for cmd in intent['commands']]
                intent['confidence'] = sum(confidences) / len(confidences)
                
                # Determine intent type
                command_types = [cmd['type'] for cmd in intent['commands']]
                if 'action' in command_types:
                    intent['intent_type'] = 'action_request'
                elif 'position' in command_types:
                    intent['intent_type'] = 'position_request'
                elif 'tactic' in command_types:
                    intent['intent_type'] = 'tactic_request'
                
                # Check for urgency indicators
                urgency_words = ['ngay', 'lập tức', 'nhanh', 'gấp', 'urgent', 'now', 'quick']
                if any(word in text.lower() for word in urgency_words):
                    intent['urgency'] = 'high'
                else:
                    intent['urgency'] = 'normal'
            
            return intent
            
        except Exception as e:
            self.logger.error(f"Error understanding intent: {e}")
            return {'text': text, 'error': str(e)}

class CommandInterpreter:
    """Thông dịch viên lệnh game"""
    
    def __init__(self):
        self.logger = get_logger(__name__)
        
        # Language processor
        self.language_processor = VietnameseLanguageProcessor()
        
        # Command patterns
        self.command_patterns = {
            'simple_action': r'(chuyền|sút|dẫn|tắc|phá|phòng thủ|tấn công)',
            'action_with_target': r'(chuyền|sút|dẫn|tắc|phá)\s+(cho|tới|về)\s+(\w+)',
            'position_change': r'(di chuyển|chuyển|đi)\s+(tới|về|ra)\s+(phòng thủ|giữa sân|tấn công)',
            'tactic_change': r'(thay đổi|đổi|chuyển)\s+(chiến thuật|tactics)\s+(thành|sang)\s+(\w+)',
            'formation_change': r'(thay đổi|đổi|chuyển)\s+(đội hình|formation)\s+(thành|sang)\s+(\w+)'
        }
        
        # Command history
        self.command_history = deque(maxlen=1000)
        
        # Response templates
        self.response_templates = {
            'tiếng_việt': {
                'action_confirmed': 'Đã thực hiện lệnh {action}',
                'position_changed': 'Đã di chuyển về vị trí {position}',
                'tactic_changed': 'Đã thay đổi chiến thuật thành {tactic}',
                'command_not_understood': 'Không hiểu lệnh, vui lòng thử lại',
                'action_in_progress': 'Đang thực hiện lệnh {action}...'
            },
            'tiếng_anh': {
                'action_confirmed': 'Command {action} executed',
                'position_changed': 'Moved to {position} position',
                'tactic_changed': 'Changed tactic to {tactic}',
                'command_not_understood': 'Command not understood, please try again',
                'action_in_progress': 'Executing command {action}...'
            }
        }
        
        self.logger.info("Command Interpreter initialized")
    
    def interpret_command(self, text: str) -> Dict[str, Any]:
        """Thông dịch lệnh từ văn bản"""
        try:
            # Understand intent
            intent = self.language_processor.understand_intent(text)
            
            # Parse command structure
            command_structure = self._parse_command_structure(text, intent)
            
            # Create command object
            command = {
                'original_text': text,
                'intent': intent,
                'structure': command_structure,
                'timestamp': time.time(),
                'status': 'pending'
            }
            
            # Store in history
            self.command_history.append(command)
            
            return command
            
        except Exception as e:
            self.logger.error(f"Error interpreting command: {e}")
            return {'error': str(e), 'original_text': text}
    
    def _parse_command_structure(self, text: str, intent: Dict[str, Any]) -> Dict[str, Any]:
        """Phân tích cấu trúc lệnh"""
        try:
            structure = {
                'type': 'unknown',
                'action': None,
                'target': None,
                'position': None,
                'tactic': None,
                'parameters': {}
            }
            
            # Check for simple action
            if intent['commands']:
                for cmd in intent['commands']:
                    if cmd['type'] == 'action':
                        structure['type'] = 'action'
                        structure['action'] = cmd['action']
                        break
                    elif cmd['type'] == 'position':
                        structure['type'] = 'position'
                        structure['position'] = cmd['position']
                        break
                    elif cmd['type'] == 'tactic':
                        structure['type'] = 'tactic'
                        structure['tactic'] = cmd['tactic']
                        break
            
            # Check for complex patterns
            for pattern_name, pattern in self.command_patterns.items():
                matches = re.findall(pattern, text, re.IGNORECASE)
                if matches:
                    if pattern_name == 'action_with_target':
                        structure['type'] = 'action_with_target'
                        structure['action'] = matches[0][0]
                        structure['target'] = matches[0][2]
                    elif pattern_name == 'position_change':
                        structure['type'] = 'position_change'
                        structure['position'] = matches[0][2]
                    elif pattern_name == 'tactic_change':
                        structure['type'] = 'tactic_change'
                        structure['tactic'] = matches[0][3]
                    elif pattern_name == 'formation_change':
                        structure['type'] = 'formation_change'
                        structure['parameters']['formation'] = matches[0][3]
            
            return structure
            
        except Exception as e:
            self.logger.error(f"Error parsing command structure: {e}")
            return {'type': 'unknown'}
    
    def generate_response(self, command: Dict[str, Any], language: str = 'auto') -> str:
        """Tạo phản hồi cho lệnh"""
        try:
            if language == 'auto':
                language = command['intent']['language']
            
            # Select response template
            if language == 'tiếng_việt':
                templates = self.response_templates['tiếng_việt']
            else:
                templates = self.response_templates['tiếng_anh']
            
            # Generate response based on command type
            structure = command['structure']
            
            if structure['type'] == 'action':
                return templates['action_confirmed'].format(action=structure['action'])
            elif structure['type'] == 'position':
                return templates['position_changed'].format(position=structure['position'])
            elif structure['type'] == 'tactic':
                return templates['tactic_changed'].format(tactic=structure['tactic'])
            elif structure['type'] == 'action_with_target':
                return templates['action_confirmed'].format(action=structure['action'])
            else:
                return templates['command_not_understood']
                
        except Exception as e:
            self.logger.error(f"Error generating response: {e}")
            return "Error generating response"
    
    def get_command_history(self) -> List[Dict[str, Any]]:
        """Lấy lịch sử lệnh"""
        return list(self.command_history)
    
    def get_command_statistics(self) -> Dict[str, Any]:
        """Lấy thống kê lệnh"""
        try:
            if not self.command_history:
                return {}
            
            stats = {
                'total_commands': len(self.command_history),
                'successful_commands': 0,
                'failed_commands': 0,
                'command_types': defaultdict(int),
                'languages': defaultdict(int),
                'intent_types': defaultdict(int)
            }
            
            for command in self.command_history:
                # Count by status
                if command.get('status') == 'completed':
                    stats['successful_commands'] += 1
                elif command.get('status') == 'failed':
                    stats['failed_commands'] += 1
                
                # Count by command type
                structure = command.get('structure', {})
                stats['command_types'][structure.get('type', 'unknown')] += 1
                
                # Count by language
                intent = command.get('intent', {})
                stats['languages'][intent.get('language', 'unknown')] += 1
                
                # Count by intent type
                stats['intent_types'][intent.get('intent_type', 'unknown')] += 1
            
            return stats
            
        except Exception as e:
            self.logger.error(f"Error getting command statistics: {e}")
            return {}

class NaturalLanguageSystem:
    """Hệ thống Natural Language Processing chính"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = get_logger(__name__)
        
        # Components
        self.language_processor = VietnameseLanguageProcessor()
        self.command_interpreter = CommandInterpreter()
        
        # Performance tracking
        self.processing_times = deque(maxlen=1000)
        self.accuracy_metrics = deque(maxlen=1000)
        
        # Threading
        self.lock = threading.Lock()
        self.is_active = False
        
        self.logger.info("Natural Language Processing System initialized")
    
    def start(self):
        """Khởi động hệ thống"""
        try:
            with self.lock:
                self.is_active = True
                self.logger.info("Natural Language Processing System started")
                return True
        except Exception as e:
            self.logger.error(f"Error starting Natural Language Processing System: {e}")
            return False
    
    def stop(self):
        """Dừng hệ thống"""
        try:
            with self.lock:
                self.is_active = False
                self.logger.info("Natural Language Processing System stopped")
                return True
        except Exception as e:
            self.logger.error(f"Error stopping Natural Language Processing System: {e}")
            return False
    
    @log_performance
    def process_command(self, text: str) -> Dict[str, Any]:
        """Xử lý lệnh bằng ngôn ngữ tự nhiên"""
        try:
            if not self.is_active:
                return {'error': 'System not active'}
            
            start_time = time.time()
            
            # Interpret command
            command = self.command_interpreter.interpret_command(text)
            
            # Generate response
            response = self.command_interpreter.generate_response(command)
            
            # Record processing time
            processing_time = time.time() - start_time
            self.processing_times.append(processing_time)
            
            # Record accuracy (simple heuristic)
            if command.get('structure', {}).get('type') != 'unknown':
                self.accuracy_metrics.append(1.0)
            else:
                self.accuracy_metrics.append(0.0)
            
            result = {
                'command': command,
                'response': response,
                'processing_time': processing_time,
                'success': command.get('structure', {}).get('type') != 'unknown'
            }
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error processing command: {e}")
            return {'error': str(e), 'original_text': text}
    
    def batch_process_commands(self, commands: List[str]) -> List[Dict[str, Any]]:
        """Xử lý nhiều lệnh cùng lúc"""
        try:
            results = []
            
            for command in commands:
                result = self.process_command(command)
                results.append(result)
            
            return results
            
        except Exception as e:
            self.logger.error(f"Error batch processing commands: {e}")
            return []
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Lấy thống kê hiệu suất"""
        try:
            stats = {}
            
            # Processing time statistics
            if self.processing_times:
                stats['avg_processing_time'] = sum(self.processing_times) / len(self.processing_times)
                stats['max_processing_time'] = max(self.processing_times)
                stats['min_processing_time'] = min(self.processing_times)
            
            # Accuracy statistics
            if self.accuracy_metrics:
                stats['accuracy_rate'] = sum(self.accuracy_metrics) / len(self.accuracy_metrics)
                stats['total_commands_processed'] = len(self.accuracy_metrics)
            
            # Command statistics
            command_stats = self.command_interpreter.get_command_statistics()
            stats.update(command_stats)
            
            stats['system_active'] = self.is_active
            
            return stats
            
        except Exception as e:
            self.logger.error(f"Error getting performance stats: {e}")
            return {}
    
    def cleanup(self):
        """Dọn dẹp tài nguyên"""
        try:
            self.stop()
            self.logger.info("Natural Language Processing System cleanup completed")
        except Exception as e:
            self.logger.error(f"Error during Natural Language Processing System cleanup: {e}") 
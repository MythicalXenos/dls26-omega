#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration file for AI/ML Systems
File cấu hình cho các hệ thống AI/ML
"""

from typing import Dict, Any, List

# Machine Learning Configuration
ML_CONFIG = {
    'learning': {
        'max_memory_size': 10000,
        'learning_rate': 0.1,
        'discount_factor': 0.9,
        'num_agents': 5,
        'epsilon': 0.1,
        'confidence_threshold': 0.7,
        'success_rate_threshold': 0.6
    },
    'decision_tree': {
        'max_rules': 1000,
        'min_confidence': 0.5,
        'rule_update_rate': 0.1
    },
    'reinforcement_learning': {
        'q_table_size': 10000,
        'exploration_decay': 0.99,
        'min_epsilon': 0.01
    },
    'multi_agent': {
        'evolution_frequency': 100,  # games
        'mutation_rate': 0.1,
        'crossover_rate': 0.8
    },
    'performance': {
        'optimization_interval': 300,  # seconds
        'memory_cleanup_threshold': 0.8,
        'learning_rate_adjustment': 0.9
    }
}

# Computer Vision Configuration
CV_CONFIG = {
    'detection': {
        'confidence_threshold': 0.7,
        'nms_threshold': 0.4,
        'min_object_size': 50,
        'max_object_size': 1000
    },
    'ball_detection': {
        'template_matching_threshold': 0.8,
        'color_range': {
            'lower': [0, 0, 200],  # White objects
            'upper': [180, 30, 255]
        },
        'min_circularity': 0.7,
        'size_range': [20, 100]
    },
    'player_detection': {
        'hog_scale': 1.05,
        'hog_win_stride': (8, 8),
        'hog_padding': (4, 4),
        'min_aspect_ratio': 1.5,
        'max_aspect_ratio': 3.0
    },
    'field_detection': {
        'green_range': {
            'lower': [35, 50, 50],
            'upper': [85, 255, 255]
        },
        'min_field_area': 100000
    },
    'processing': {
        'frame_resize_factor': 0.5,
        'max_processing_time': 0.1,  # seconds
        'batch_size': 10
    }
}

# Deep Learning Configuration
DL_CONFIG = {
    'models': {
        'action_prediction': {
            'type': 'transformer',
            'input_size': 50,
            'hidden_size': 128,
            'num_layers': 4,
            'num_heads': 8,
            'dropout': 0.3
        },
        'outcome_prediction': {
            'type': 'attention',
            'input_size': 60,
            'hidden_size': 128,
            'attention_heads': 4,
            'dropout': 0.3
        },
        'tactical_analysis': {
            'type': 'cnn_lstm',
            'input_shape': (40,),
            'cnn_filters': [32, 64, 128],
            'lstm_units': 64,
            'dropout': 0.3
        }
    },
    'training': {
        'batch_size': 32,
        'epochs': 100,
        'validation_split': 0.2,
        'early_stopping_patience': 10,
        'learning_rate': 0.001,
        'learning_rate_decay': 0.5
    },
    'optimization': {
        'use_gpu': True,
        'mixed_precision': True,
        'gradient_clipping': 1.0,
        'weight_decay': 0.0001
    },
    'data_management': {
        'max_training_samples': 50000,
        'data_augmentation': True,
        'normalization': True,
        'feature_scaling': True
    }
}

# Natural Language Processing Configuration
NLP_CONFIG = {
    'languages': {
        'supported': ['tiếng_việt', 'tiếng_anh'],
        'default': 'tiếng_việt',
        'auto_detection': True
    },
    'vietnamese': {
        'stop_words': True,
        'lemmatization': True,
        'stemming': False,
        'diacritics_preservation': True
    },
    'english': {
        'stop_words': True,
        'lemmatization': True,
        'stemming': True,
        'pos_tagging': True
    },
    'command_processing': {
        'max_command_length': 200,
        'min_confidence': 0.6,
        'fuzzy_matching': True,
        'context_awareness': True
    },
    'response_generation': {
        'templates_enabled': True,
        'dynamic_responses': True,
        'multilingual_responses': True,
        'response_variation': True
    },
    'performance': {
        'batch_processing': True,
        'max_batch_size': 100,
        'caching_enabled': True,
        'max_cache_size': 1000
    }
}

# Integration Configuration
INTEGRATION_CONFIG = {
    'system_coordination': {
        'sync_interval': 1.0,  # seconds
        'data_sharing': True,
        'cross_system_learning': True
    },
    'performance_monitoring': {
        'metrics_collection': True,
        'real_time_monitoring': True,
        'alert_thresholds': {
            'processing_time': 0.1,
            'memory_usage': 0.8,
            'accuracy_drop': 0.1
        }
    },
    'data_pipeline': {
        'real_time_processing': True,
        'batch_processing': True,
        'data_persistence': True,
        'backup_frequency': 3600  # seconds
    },
    'error_handling': {
        'graceful_degradation': True,
        'fallback_systems': True,
        'error_logging': True,
        'auto_recovery': True
    }
}

# Performance Optimization Configuration
PERFORMANCE_CONFIG = {
    'memory_management': {
        'max_memory_usage': 0.8,
        'cleanup_threshold': 0.7,
        'garbage_collection': True,
        'memory_pooling': True
    },
    'threading': {
        'max_worker_threads': 8,
        'thread_pool_size': 16,
        'async_processing': True,
        'load_balancing': True
    },
    'gpu_optimization': {
        'gpu_memory_fraction': 0.8,
        'mixed_precision': True,
        'tensor_cores': True,
        'cuda_graphs': True
    },
    'caching': {
        'model_cache_size': 1000,
        'feature_cache_size': 5000,
        'result_cache_size': 2000,
        'cache_ttl': 3600  # seconds
    }
}

# Development and Testing Configuration
DEV_CONFIG = {
    'debug_mode': False,
    'verbose_logging': True,
    'performance_profiling': True,
    'unit_testing': True,
    'integration_testing': True,
    'benchmark_mode': False,
    'mock_data': True,
    'simulation_mode': True
}

# Complete AI/ML Configuration
AI_ML_CONFIG = {
    'machine_learning': ML_CONFIG,
    'computer_vision': CV_CONFIG,
    'deep_learning': DL_CONFIG,
    'natural_language': NLP_CONFIG,
    'integration': INTEGRATION_CONFIG,
    'performance': PERFORMANCE_CONFIG,
    'development': DEV_CONFIG,
    'version': '1.0.0',
    'last_updated': '2024-01-01'
}

def get_config(system_name: str = None) -> Dict[str, Any]:
    """
    Lấy cấu hình cho hệ thống cụ thể hoặc toàn bộ
    
    Args:
        system_name: Tên hệ thống ('machine_learning', 'computer_vision', etc.)
        
    Returns:
        Dictionary chứa cấu hình
    """
    if system_name is None:
        return AI_ML_CONFIG
    
    if system_name in AI_ML_CONFIG:
        return AI_ML_CONFIG[system_name]
    
    raise ValueError(f"Unknown system: {system_name}")

def update_config(system_name: str, new_config: Dict[str, Any]):
    """
    Cập nhật cấu hình cho hệ thống cụ thể
    
    Args:
        system_name: Tên hệ thống
        new_config: Cấu hình mới
    """
    if system_name in AI_ML_CONFIG:
        AI_ML_CONFIG[system_name].update(new_config)
    else:
        raise ValueError(f"Unknown system: {system_name}")

def get_optimized_config(performance_level: str = 'balanced') -> Dict[str, Any]:
    """
    Lấy cấu hình tối ưu cho mức hiệu suất cụ thể
    
    Args:
        performance_level: 'low', 'balanced', 'high', 'extreme'
        
    Returns:
        Cấu hình tối ưu
    """
    config = AI_ML_CONFIG.copy()
    
    if performance_level == 'low':
        # Tối ưu cho hiệu suất thấp
        config['machine_learning']['max_memory_size'] = 1000
        config['deep_learning']['models']['action_prediction']['type'] = 'mlp'
        config['computer_vision']['processing']['frame_resize_factor'] = 0.25
        
    elif performance_level == 'high':
        # Tối ưu cho hiệu suất cao
        config['machine_learning']['max_memory_size'] = 20000
        config['deep_learning']['training']['batch_size'] = 64
        config['computer_vision']['processing']['batch_size'] = 20
        
    elif performance_level == 'extreme':
        # Tối ưu cho hiệu suất cực cao
        config['machine_learning']['max_memory_size'] = 50000
        config['deep_learning']['training']['batch_size'] = 128
        config['computer_vision']['processing']['batch_size'] = 50
        config['performance']['threading']['max_worker_threads'] = 16
    
    return config

def validate_config(config: Dict[str, Any]) -> List[str]:
    """
    Kiểm tra tính hợp lệ của cấu hình
    
    Args:
        config: Cấu hình cần kiểm tra
        
    Returns:
        Danh sách các lỗi (rỗng nếu hợp lệ)
    """
    errors = []
    
    # Kiểm tra các giá trị bắt buộc
    required_systems = ['machine_learning', 'computer_vision', 'deep_learning']
    for system in required_systems:
        if system not in config:
            errors.append(f"Missing required system: {system}")
    
    # Kiểm tra giá trị hợp lệ
    if 'machine_learning' in config:
        ml_config = config['machine_learning']
        if ml_config.get('max_memory_size', 0) <= 0:
            errors.append("max_memory_size must be positive")
        
        if not 0 < ml_config.get('learning_rate', 0) < 1:
            errors.append("learning_rate must be between 0 and 1")
    
    if 'computer_vision' in config:
        cv_config = config['computer_vision']
        if not 0 < cv_config.get('detection', {}).get('confidence_threshold', 0) < 1:
            errors.append("confidence_threshold must be between 0 and 1")
    
    return errors

# Export các config chính
__all__ = [
    'AI_ML_CONFIG',
    'ML_CONFIG',
    'CV_CONFIG', 
    'DL_CONFIG',
    'NLP_CONFIG',
    'get_config',
    'update_config',
    'get_optimized_config',
    'validate_config'
] 
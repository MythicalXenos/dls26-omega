#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Deep Learning System for Dream League Soccer
Hệ thống Deep Learning nâng cao để cải thiện AI
"""

import numpy as np
import time
import threading
import json
import pickle
from typing import Dict, Any, List, Tuple, Optional, Union
from pathlib import Path
from collections import deque
import random

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, optimizers, callbacks
from tensorflow.keras.models import load_model
TENSORFLOW_AVAILABLE = True

import torch
import torch.nn as nn
import torch.optim as optim
PYTORCH_AVAILABLE = True

from utils.logger import get_logger, log_performance

class DeepNeuralNetwork:
    """Deep Neural Network sử dụng TensorFlow/Keras"""
    
    def __init__(self, input_shape: Tuple[int, ...], output_size: int, 
                 architecture: str = 'cnn_lstm'):
        self.logger = get_logger(__name__)
        
        if not TENSORFLOW_AVAILABLE:
            self.logger.warning("TensorFlow not available, using fallback")
            self.model = None
            return
        
        self.input_shape = input_shape
        self.output_size = output_size
        self.architecture = architecture
        
        # Build model
        self.model = self._build_model()
        
        # Training history
        self.training_history = []
        self.is_trained = False
        
        self.logger.info(f"Deep Neural Network initialized with {architecture} architecture")
    
    def _build_model(self) -> keras.Model:
        """Xây dựng kiến trúc model"""
        try:
            if self.architecture == 'cnn_lstm':
                return self._build_cnn_lstm_model()
            elif self.architecture == 'transformer':
                return self._build_transformer_model()
            elif self.architecture == 'attention':
                return self._build_attention_model()
            else:
                return self._build_mlp_model()
                
        except Exception as e:
            self.logger.error(f"Error building model: {e}")
            return self._build_mlp_model()
    
    def _build_cnn_lstm_model(self) -> keras.Model:
        """Xây dựng model CNN + LSTM"""
        try:
            # Input layer
            input_layer = layers.Input(shape=self.input_shape)
            
            # CNN layers for spatial features
            if len(self.input_shape) == 3:  # Image input
                x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(input_layer)
                x = layers.BatchNormalization()(x)
                x = layers.MaxPooling2D((2, 2))(x)
                
                x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
                x = layers.BatchNormalization()(x)
                x = layers.MaxPooling2D((2, 2))(x)
                
                x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
                x = layers.BatchNormalization()(x)
                x = layers.GlobalAveragePooling2D()(x)
            else:
                # Flatten for 1D input
                x = layers.Flatten()(input_layer)
            
            # Dense layers
            x = layers.Dense(256, activation='relu')(x)
            x = layers.Dropout(0.3)(x)
            x = layers.Dense(128, activation='relu')(x)
            x = layers.Dropout(0.3)(x)
            
            # LSTM layer for temporal features
            if len(self.input_shape) == 3:
                # Reshape for LSTM
                x = layers.Reshape((1, -1))(x)
                x = layers.LSTM(64, return_sequences=False)(x)
            
            # Output layer
            output_layer = layers.Dense(self.output_size, activation='softmax')(x)
            
            # Create model
            model = models.Model(inputs=input_layer, outputs=output_layer)
            
            # Compile model
            model.compile(
                optimizer=optimizers.Adam(learning_rate=0.001),
                loss='categorical_crossentropy',
                metrics=['accuracy']
            )
            
            return model
            
        except Exception as e:
            self.logger.error(f"Error building CNN-LSTM model: {e}")
            return self._build_mlp_model()
    
    def _build_transformer_model(self) -> keras.Model:
        """Xây dựng model Transformer"""
        try:
            # Input layer
            input_layer = layers.Input(shape=self.input_shape)
            
            # Positional encoding
            if len(self.input_shape) == 1:
                x = layers.Embedding(1000, 128)(input_layer)
                x = layers.PositionalEncoding(128)(x)
            else:
                x = layers.Flatten()(input_layer)
                x = layers.Dense(128)(x)
                x = layers.Reshape((1, 128))(x)
            
            # Transformer blocks
            for _ in range(4):
                # Multi-head attention
                attention_output = layers.MultiHeadAttention(
                    num_heads=8, key_dim=128
                )(x, x)
                x = layers.Add()([x, attention_output])
                x = layers.LayerNormalization(epsilon=1e-6)(x)
                
                # Feed-forward network
                ffn = layers.Dense(512, activation='relu')(x)
                ffn = layers.Dense(128)(ffn)
                x = layers.Add()([x, ffn])
                x = layers.LayerNormalization(epsilon=1e-6)(x)
            
            # Global average pooling
            x = layers.GlobalAveragePooling1D()(x)
            
            # Output layers
            x = layers.Dense(256, activation='relu')(x)
            x = layers.Dropout(0.3)(x)
            output_layer = layers.Dense(self.output_size, activation='softmax')(x)
            
            # Create model
            model = models.Model(inputs=input_layer, outputs=output_layer)
            
            # Compile model
            model.compile(
                optimizer=optimizers.Adam(learning_rate=0.001),
                loss='categorical_crossentropy',
                metrics=['accuracy']
            )
            
            return model
            
        except Exception as e:
            self.logger.error(f"Error building Transformer model: {e}")
            return self._build_mlp_model()
    
    def _build_attention_model(self) -> keras.Model:
        """Xây dựng model với Attention mechanism"""
        try:
            # Input layer
            input_layer = layers.Input(shape=self.input_shape)
            
            # Flatten input
            x = layers.Flatten()(input_layer)
            
            # Dense layers
            x = layers.Dense(256, activation='relu')(x)
            x = layers.Dropout(0.3)(x)
            
            # Attention mechanism
            attention_weights = layers.Dense(256, activation='softmax')(x)
            x = layers.Multiply()([x, attention_weights])
            
            # More dense layers
            x = layers.Dense(128, activation='relu')(x)
            x = layers.Dropout(0.3)(x)
            x = layers.Dense(64, activation='relu')(x)
            
            # Output layer
            output_layer = layers.Dense(self.output_size, activation='softmax')(x)
            
            # Create model
            model = models.Model(inputs=input_layer, outputs=output_layer)
            
            # Compile model
            model.compile(
                optimizer=optimizers.Adam(learning_rate=0.001),
                loss='categorical_crossentropy',
                metrics=['accuracy']
            )
            
            return model
            
        except Exception as e:
            self.logger.error(f"Error building Attention model: {e}")
            return self._build_mlp_model()
    
    def _build_mlp_model(self) -> keras.Model:
        """Xây dựng model MLP đơn giản"""
        try:
            # Input layer
            input_layer = layers.Input(shape=self.input_shape)
            
            # Flatten input
            x = layers.Flatten()(input_layer)
            
            # Dense layers
            x = layers.Dense(256, activation='relu')(x)
            x = layers.Dropout(0.3)(x)
            x = layers.Dense(128, activation='relu')(x)
            x = layers.Dropout(0.3)(x)
            x = layers.Dense(64, activation='relu')(x)
            
            # Output layer
            output_layer = layers.Dense(self.output_size, activation='softmax')(x)
            
            # Create model
            model = models.Model(inputs=input_layer, outputs=output_layer)
            
            # Compile model
            model.compile(
                optimizer=optimizers.Adam(learning_rate=0.001),
                loss='categorical_crossentropy',
                metrics=['accuracy']
            )
            
            return model
            
        except Exception as e:
            self.logger.error(f"Error building MLP model: {e}")
            return None
    
    def train(self, X: np.ndarray, y: np.ndarray, 
              validation_split: float = 0.2, epochs: int = 100,
              batch_size: int = 32) -> Dict[str, Any]:
        """Huấn luyện model"""
        try:
            if self.model is None:
                self.logger.error("Model not available")
                return {}
            
            # Data preprocessing
            X_processed, y_processed = self._preprocess_data(X, y)
            
            # Callbacks
            callbacks_list = [
                callbacks.EarlyStopping(patience=10, restore_best_weights=True),
                callbacks.ReduceLROnPlateau(factor=0.5, patience=5),
                callbacks.ModelCheckpoint(
                    'best_model.h5', 
                    save_best_only=True, 
                    monitor='val_accuracy'
                )
            ]
            
            # Training
            start_time = time.time()
            history = self.model.fit(
                X_processed, y_processed,
                validation_split=validation_split,
                epochs=epochs,
                batch_size=batch_size,
                callbacks=callbacks_list,
                verbose=1
            )
            training_time = time.time() - start_time
            
            # Store training history
            self.training_history.append({
                'timestamp': time.time(),
                'epochs': epochs,
                'training_time': training_time,
                'final_accuracy': history.history['accuracy'][-1],
                'final_val_accuracy': history.history['val_accuracy'][-1]
            })
            
            self.is_trained = True
            
            self.logger.info(f"Model trained successfully in {training_time:.2f} seconds")
            
            return {
                'status': 'success',
                'training_time': training_time,
                'final_accuracy': history.history['accuracy'][-1],
                'final_val_accuracy': history.history['val_accuracy'][-1]
            }
            
        except Exception as e:
            self.logger.error(f"Error training model: {e}")
            return {'status': 'error', 'message': str(e)}
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Dự đoán với model"""
        try:
            if self.model is None or not self.is_trained:
                self.logger.warning("Model not available or not trained")
                return np.random.rand(X.shape[0], self.output_size)
            
            # Preprocess input
            X_processed = self._preprocess_input(X)
            
            # Make prediction
            predictions = self.model.predict(X_processed, verbose=0)
            
            return predictions
            
        except Exception as e:
            self.logger.error(f"Error making prediction: {e}")
            return np.random.rand(X.shape[0], self.output_size)
    
    def _preprocess_data(self, X: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Tiền xử lý dữ liệu training"""
        try:
            # Normalize input
            X_processed = X.astype(np.float32) / 255.0 if X.max() > 1.0 else X.astype(np.float32)
            
            # Ensure correct shape
            if len(X_processed.shape) == 2:
                X_processed = X_processed.reshape(-1, X_processed.shape[1], 1)
            
            # Convert labels to categorical
            if len(y.shape) == 1:
                y_processed = tf.keras.utils.to_categorical(y, num_classes=self.output_size)
            else:
                y_processed = y.astype(np.float32)
            
            return X_processed, y_processed
            
        except Exception as e:
            self.logger.error(f"Error preprocessing data: {e}")
            return X, y
    
    def _preprocess_input(self, X: np.ndarray) -> np.ndarray:
        """Tiền xử lý input cho prediction"""
        try:
            # Normalize input
            X_processed = X.astype(np.float32) / 255.0 if X.max() > 1.0 else X.astype(np.float32)
            
            # Ensure correct shape
            if len(X_processed.shape) == 2:
                X_processed = X_processed.reshape(-1, X_processed.shape[1], 1)
            
            return X_processed
            
        except Exception as e:
            self.logger.error(f"Error preprocessing input: {e}")
            return X
    
    def save_model(self, filepath: str):
        """Lưu model"""
        try:
            if self.model is not None:
                self.model.save(filepath)
                self.logger.info(f"Model saved to {filepath}")
        except Exception as e:
            self.logger.error(f"Error saving model: {e}")
    
    def load_model(self, filepath: str):
        """Tải model"""
        try:
            if TENSORFLOW_AVAILABLE and Path(filepath).exists():
                self.model = load_model(filepath)
                self.is_trained = True
                self.logger.info(f"Model loaded from {filepath}")
        except Exception as e:
            self.logger.error(f"Error loading model: {e}")

class PyTorchNeuralNetwork:
    """Neural Network sử dụng PyTorch"""
    
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        self.logger = get_logger(__name__)
        
        if not PYTORCH_AVAILABLE:
            self.logger.warning("PyTorch not available, using fallback")
            self.model = None
            return
        
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Build model
        self.model = self._build_model()
        
        # Training parameters
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        
        # Training history
        self.training_history = []
        self.is_trained = False
        
        self.logger.info("PyTorch Neural Network initialized")
    
    def _build_model(self) -> nn.Module:
        """Xây dựng model PyTorch"""
        try:
            class GameNN(nn.Module):
                def __init__(self, input_size, hidden_size, output_size):
                    super(GameNN, self).__init__()
                    self.fc1 = nn.Linear(input_size, hidden_size)
                    self.fc2 = nn.Linear(hidden_size, hidden_size)
                    self.fc3 = nn.Linear(hidden_size, output_size)
                    self.dropout = nn.Dropout(0.3)
                    self.relu = nn.ReLU()
                
                def forward(self, x):
                    x = self.relu(self.fc1(x))
                    x = self.dropout(x)
                    x = self.relu(self.fc2(x))
                    x = self.dropout(x)
                    x = self.fc3(x)
                    return x
            
            return GameNN(self.input_size, self.hidden_size, self.output_size)
            
        except Exception as e:
            self.logger.error(f"Error building PyTorch model: {e}")
            return None
    
    def train(self, X: np.ndarray, y: np.ndarray, epochs: int = 100) -> Dict[str, Any]:
        """Huấn luyện model PyTorch"""
        try:
            if self.model is None:
                self.logger.error("Model not available")
                return {}
            
            # Convert to PyTorch tensors
            X_tensor = torch.FloatTensor(X)
            y_tensor = torch.LongTensor(y)
            
            # Training loop
            start_time = time.time()
            for epoch in range(epochs):
                self.optimizer.zero_grad()
                
                # Forward pass
                outputs = self.model(X_tensor)
                loss = self.criterion(outputs, y_tensor)
                
                # Backward pass
                loss.backward()
                self.optimizer.step()
                
                if epoch % 10 == 0:
                    self.logger.debug(f"Epoch {epoch}, Loss: {loss.item():.4f}")
            
            training_time = time.time() - start_time
            
            # Store training history
            self.training_history.append({
                'timestamp': time.time(),
                'epochs': epochs,
                'training_time': training_time,
                'final_loss': loss.item()
            })
            
            self.is_trained = True
            
            self.logger.info(f"PyTorch model trained successfully in {training_time:.2f} seconds")
            
            return {
                'status': 'success',
                'training_time': training_time,
                'final_loss': loss.item()
            }
            
        except Exception as e:
            self.logger.error(f"Error training PyTorch model: {e}")
            return {'status': 'error', 'message': str(e)}
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Dự đoán với model PyTorch"""
        try:
            if self.model is None or not self.is_trained:
                self.logger.warning("Model not available or not trained")
                return np.random.rand(X.shape[0], self.output_size)
            
            # Convert to PyTorch tensor
            X_tensor = torch.FloatTensor(X)
            
            # Make prediction
            with torch.no_grad():
                outputs = self.model(X_tensor)
                probabilities = torch.softmax(outputs, dim=1)
            
            return probabilities.numpy()
            
        except Exception as e:
            self.logger.error(f"Error making PyTorch prediction: {e}")
            return np.random.rand(X.shape[0], self.output_size)

class DeepLearningSystem:
    """Hệ thống Deep Learning chính"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = get_logger(__name__)
        
        # Models
        self.models = {}
        self.model_configs = {}
        
        # Training data
        self.training_data = {
            'action_prediction': deque(maxlen=10000),
            'outcome_prediction': deque(maxlen=10000),
            'tactical_analysis': deque(maxlen=10000)
        }
        
        # Performance tracking
        self.performance_metrics = deque(maxlen=1000)
        
        # Threading
        self.lock = threading.Lock()
        self.is_active = False
        
        # Initialize models
        self._initialize_models()
        
        self.logger.info("Deep Learning System initialized")
    
    def _initialize_models(self):
        """Khởi tạo các model"""
        try:
            # Action prediction model
            action_config = {
                'input_shape': (50,),  # 50 features
                'output_size': 7,      # 7 possible actions
                'architecture': 'transformer'
            }
            
            if TENSORFLOW_AVAILABLE:
                self.models['action_prediction'] = DeepNeuralNetwork(**action_config)
                self.model_configs['action_prediction'] = action_config
            elif PYTORCH_AVAILABLE:
                self.models['action_prediction'] = PyTorchNeuralNetwork(
                    input_size=50, hidden_size=128, output_size=7
                )
                self.model_configs['action_prediction'] = action_config
            
            # Outcome prediction model
            outcome_config = {
                'input_shape': (60,),  # 60 features
                'output_size': 3,      # Win/Draw/Loss
                'architecture': 'attention'
            }
            
            if TENSORFLOW_AVAILABLE:
                self.models['outcome_prediction'] = DeepNeuralNetwork(**outcome_config)
                self.model_configs['outcome_prediction'] = outcome_config
            elif PYTORCH_AVAILABLE:
                self.models['outcome_prediction'] = PyTorchNeuralNetwork(
                    input_size=60, hidden_size=128, output_size=3
                )
                self.model_configs['outcome_prediction'] = outcome_config
            
            # Tactical analysis model
            tactical_config = {
                'input_shape': (40,),  # 40 features
                'output_size': 5,      # 5 tactical categories
                'architecture': 'cnn_lstm'
            }
            
            if TENSORFLOW_AVAILABLE:
                self.models['tactical_analysis'] = DeepNeuralNetwork(**tactical_config)
                self.model_configs['tactical_analysis'] = tactical_config
            elif PYTORCH_AVAILABLE:
                self.models['tactical_analysis'] = PyTorchNeuralNetwork(
                    input_size=40, hidden_size=128, output_size=5
                )
                self.model_configs['tactical_analysis'] = tactical_config
            
            self.logger.info(f"Initialized {len(self.models)} deep learning models")
            
        except Exception as e:
            self.logger.error(f"Error initializing models: {e}")
    
    def start(self):
        """Khởi động hệ thống"""
        try:
            with self.lock:
                self.is_active = True
                self.logger.info("Deep Learning System started")
                return True
        except Exception as e:
            self.logger.error(f"Error starting Deep Learning System: {e}")
            return False
    
    def stop(self):
        """Dừng hệ thống"""
        try:
            with self.lock:
                self.is_active = False
                self.logger.info("Deep Learning System stopped")
                return True
        except Exception as e:
            self.logger.error(f"Error stopping Deep Learning System: {e}")
            return False
    
    def add_training_data(self, data_type: str, features: np.ndarray, labels: np.ndarray):
        """Thêm dữ liệu training"""
        try:
            if data_type not in self.training_data:
                self.logger.warning(f"Unknown data type: {data_type}")
                return
            
            # Store training data
            self.training_data[data_type].append({
                'features': features,
                'labels': labels,
                'timestamp': time.time()
            })
            
            self.logger.debug(f"Added training data for {data_type}: {len(features)} samples")
            
        except Exception as e:
            self.logger.error(f"Error adding training data: {e}")
    
    def train_model(self, model_name: str, data_type: str = None) -> Dict[str, Any]:
        """Huấn luyện một model cụ thể"""
        try:
            if model_name not in self.models:
                return {'status': 'error', 'message': f'Model {model_name} not found'}
            
            model = self.models[model_name]
            
            # Use specified data type or infer from model name
            if data_type is None:
                data_type = model_name
            
            if data_type not in self.training_data:
                return {'status': 'error', 'message': f'No training data for {data_type}'}
            
            # Prepare training data
            X, y = self._prepare_training_data(data_type)
            
            if len(X) < 100:
                return {'status': 'error', 'message': 'Insufficient training data'}
            
            # Train model
            if isinstance(model, DeepNeuralNetwork):
                result = model.train(X, y, epochs=50)
            elif isinstance(model, PyTorchNeuralNetwork):
                result = model.train(X, y, epochs=50)
            else:
                return {'status': 'error', 'message': 'Unknown model type'}
            
            # Record performance
            if result.get('status') == 'success':
                self.performance_metrics.append({
                    'model': model_name,
                    'data_type': data_type,
                    'timestamp': time.time(),
                    'result': result
                })
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error training model {model_name}: {e}")
            return {'status': 'error', 'message': str(e)}
    
    def predict(self, model_name: str, features: np.ndarray) -> np.ndarray:
        """Dự đoán với model cụ thể"""
        try:
            if model_name not in self.models:
                self.logger.error(f"Model {model_name} not found")
                return np.array([])
            
            model = self.models[model_name]
            
            # Make prediction
            predictions = model.predict(features)
            
            return predictions
            
        except Exception as e:
            self.logger.error(f"Error making prediction with {model_name}: {e}")
            return np.array([])
    
    def _prepare_training_data(self, data_type: str) -> Tuple[np.ndarray, np.ndarray]:
        """Chuẩn bị dữ liệu training"""
        try:
            data = self.training_data[data_type]
            
            if not data:
                return np.array([]), np.array([])
            
            # Combine all features and labels
            all_features = []
            all_labels = []
            
            for item in data:
                all_features.append(item['features'])
                all_labels.append(item['labels'])
            
            # Concatenate
            X = np.vstack(all_features) if all_features else np.array([])
            y = np.concatenate(all_labels) if all_labels else np.array([])
            
            return X, y
            
        except Exception as e:
            self.logger.error(f"Error preparing training data: {e}")
            return np.array([]), np.array([])
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Lấy thống kê hiệu suất"""
        try:
            stats = {}
            
            # Model statistics
            stats['total_models'] = len(self.models)
            stats['trained_models'] = sum(1 for model in self.models.values() 
                                        if hasattr(model, 'is_trained') and model.is_trained)
            
            # Training data statistics
            for data_type, data in self.training_data.items():
                stats[f'{data_type}_samples'] = len(data)
            
            # Performance metrics
            if self.performance_metrics:
                recent_metrics = list(self.performance_metrics)[-10:]
                stats['recent_training_results'] = [
                    {
                        'model': m['model'],
                        'data_type': m['data_type'],
                        'timestamp': m['timestamp'],
                        'result': m['result']
                    }
                    for m in recent_metrics
                ]
            
            stats['system_active'] = self.is_active
            
            return stats
            
        except Exception as e:
            self.logger.error(f"Error getting performance stats: {e}")
            return {}
    
    def save_models(self, directory: str):
        """Lưu tất cả models"""
        try:
            save_dir = Path(directory)
            save_dir.mkdir(exist_ok=True)
            
            for model_name, model in self.models.items():
                if hasattr(model, 'save_model'):
                    model_path = save_dir / f"{model_name}.h5"
                    model.save_model(str(model_path))
                elif hasattr(model, 'model') and model.model is not None:
                    # Save PyTorch model
                    model_path = save_dir / f"{model_name}.pth"
                    torch.save(model.model.state_dict(), str(model_path))
            
            # Save configurations
            config_path = save_dir / "model_configs.json"
            with open(config_path, 'w') as f:
                json.dump(self.model_configs, f, indent=2)
            
            self.logger.info(f"All models saved to {directory}")
            
        except Exception as e:
            self.logger.error(f"Error saving models: {e}")
    
    def load_models(self, directory: str):
        """Tải tất cả models"""
        try:
            load_dir = Path(directory)
            
            if not load_dir.exists():
                self.logger.warning(f"Directory {directory} does not exist")
                return
            
            # Load configurations
            config_path = load_dir / "model_configs.json"
            if config_path.exists():
                with open(config_path, 'r') as f:
                    self.model_configs = json.load(f)
            
            # Load models
            for model_name, model in self.models.items():
                if hasattr(model, 'load_model'):
                    model_path = load_dir / f"{model_name}.h5"
                    if model_path.exists():
                        model.load_model(str(model_path))
                elif hasattr(model, 'model') and model.model is not None:
                    # Load PyTorch model
                    model_path = load_dir / f"{model_name}.pth"
                    if model_path.exists():
                        model.model.load_state_dict(torch.load(str(model_path)))
                        model.is_trained = True
            
            self.logger.info(f"All models loaded from {directory}")
            
        except Exception as e:
            self.logger.error(f"Error loading models: {e}")
    
    def cleanup(self):
        """Dọn dẹp tài nguyên"""
        try:
            self.stop()
            self.logger.info("Deep Learning System cleanup completed")
        except Exception as e:
            self.logger.error(f"Error during Deep Learning System cleanup: {e}") 
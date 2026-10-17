#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Computer Vision System for Dream League Soccer
Hệ thống thị giác máy tính nâng cao để phân tích game
"""

import cv2
import numpy as np
import time
from typing import Dict, Any, List, Tuple, Optional, Union
from pathlib import Path
import json
from collections import deque
import threading

from utils.logger import get_logger, log_performance
import pytesseract

class GameObjectDetector:
    """Detector để nhận diện các đối tượng trong game"""
    
    def __init__(self):
        self.logger = get_logger(__name__)
        
        # Pre-trained models và templates
        self.ball_template = None
        self.player_templates = []
        self.goal_templates = []
        self.hud_filled_template = None
        self.hud_hollow_template = None
        
        # Detection parameters
        self.confidence_threshold = 0.7
        self.nms_threshold = 0.4
        
        # Color ranges for different objects
        self.color_ranges = {
            'ball': {
                'lower': np.array([0, 0, 200]),  # White objects
                'upper': np.array([180, 30, 255])
            },
            'field': {
                'lower': np.array([35, 50, 50]),   # Green field
                'upper': np.array([85, 255, 255])
            },
            'player_team1': {
                'lower': np.array([0, 100, 100]),  # Red/Orange
                'upper': np.array([20, 255, 255])
            },
            'player_team2': {
                'lower': np.array([100, 100, 100]), # Blue
                'upper': np.array([130, 255, 255])
            },
            'goal_white': {
                'lower': np.array([0, 0, 220]),  # bright white
                'upper': np.array([180, 30, 255])
            }
        }
        
        # Load templates
        self._load_templates()

        # Jersey color samples (HSV) learned at match start
        self.jersey_samples = {
            'own_player': None,
            'opponent_player': None,
            'own_goalkeeper': None,
            'opponent_goalkeeper': None,
        }
    
    def _load_templates(self):
        """Load các template để nhận diện"""
        try:
            # Load ball template
            ball_path = Path(__file__).parent.parent / 'assets' / 'templates' / 'ball.png'
            if ball_path.exists():
                self.ball_template = cv2.imread(str(ball_path), cv2.IMREAD_GRAYSCALE)
            
            # Load player templates
            player_dir = Path(__file__).parent.parent / 'assets' / 'templates' / 'players'
            if player_dir.exists():
                for player_file in player_dir.glob('*.png'):
                    template = cv2.imread(str(player_file), cv2.IMREAD_GRAYSCALE)
                    if template is not None:
                        self.player_templates.append(template)
            # Load HUD indicator templates
            hud_filled = Path(__file__).parent.parent / 'assets' / 'templates' / 'hud_filled.png'
            hud_hollow = Path(__file__).parent.parent / 'assets' / 'templates' / 'hud_hollow.png'
            if hud_filled.exists():
                self.hud_filled_template = cv2.imread(str(hud_filled), cv2.IMREAD_GRAYSCALE)
            if hud_hollow.exists():
                self.hud_hollow_template = cv2.imread(str(hud_hollow), cv2.IMREAD_GRAYSCALE)
            
            self.logger.info(f"Loaded {len(self.player_templates)} player templates")
            
        except Exception as e:
            self.logger.warning(f"Could not load templates: {e}")
    
    def detect_ball(self, image: np.ndarray) -> List[Dict[str, Any]]:
        """Nhận diện bóng trong hình ảnh"""
        try:
            detections = []
            
            # Method 1: Template matching
            if self.ball_template is not None:
                template_detections = self._template_matching(image, self.ball_template, 'ball')
                detections.extend(template_detections)
            
            # Method 2: Color-based detection
            color_detections = self._color_based_detection(image, 'ball')
            detections.extend(color_detections)
            
            # Method 3: Contour detection
            contour_detections = self._contour_based_detection(image, 'ball')
            detections.extend(contour_detections)
            
            # Apply non-maximum suppression
            final_detections = self._apply_nms(detections)
            
            return final_detections
            
        except Exception as e:
            self.logger.error(f"Error detecting ball: {e}")
            return []
    
    def detect_players(self, image: np.ndarray) -> List[Dict[str, Any]]:
        """Nhận diện cầu thủ trong hình ảnh"""
        try:
            detections = []
            
            # Method 1: Template matching
            for i, template in enumerate(self.player_templates):
                template_detections = self._template_matching(image, template, f'player_{i}')
                detections.extend(template_detections)
            
            # Method 2: Color-based detection for team identification
            team1_detections = self._color_based_detection(image, 'player_team1')
            team2_detections = self._color_based_detection(image, 'player_team2')
            
            detections.extend(team1_detections)
            detections.extend(team2_detections)
            
            # Method 3: HOG person detector
            hog_detections = self._hog_person_detection(image)
            detections.extend(hog_detections)
            
            # Apply non-maximum suppression
            final_detections = self._apply_nms(detections)
            
            return final_detections
        except Exception as e:
            self.logger.error(f"Error detecting players: {e}")
            return []

    def sample_team_colors(self, image: np.ndarray, regions: Dict[str, Tuple[int, int, int, int]]):
        """Lấy mẫu màu áo theo các vùng cố định khi bắt đầu trận."""
        try:
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            for role, (x1, y1, x2, y2) in regions.items():
                roi = hsv[y1:y2, x1:x2]
                if roi.size == 0:
                    continue
                # Median HSV as sample
                h = np.median(roi[:, :, 0])
                s = np.median(roi[:, :, 1])
                v = np.median(roi[:, :, 2])
                self.jersey_samples[role] = (float(h), float(s), float(v))
            self.logger.info(f"Jersey samples: {self.jersey_samples}")
        except Exception as e:
            self.logger.error(f"Error sampling team colors: {e}")

    def classify_player_jersey(self, image: np.ndarray, bbox: Tuple[int, int, int, int]) -> Tuple[str, float]:
        """Phân loại áo cầu thủ theo bbox, trả về ('own'|'opponent'|'unknown', confidence)."""
        try:
            x, y, w, h = bbox
            roi = image[y:y+h, x:x+w]
            if roi.size == 0:
                return 'unknown', 0.0
            hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            h_med = np.median(hsv[:, :, 0])
            s_med = np.median(hsv[:, :, 1])
            v_med = np.median(hsv[:, :, 2])
            cand = (h_med, s_med, v_med)

            def dist(a, b):
                return np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

            own_refs = [self.jersey_samples.get('own_player'), self.jersey_samples.get('own_goalkeeper')]
            opp_refs = [self.jersey_samples.get('opponent_player'), self.jersey_samples.get('opponent_goalkeeper')]
            own_refs = [r for r in own_refs if r is not None]
            opp_refs = [r for r in opp_refs if r is not None]
            if not own_refs and not opp_refs:
                return 'unknown', 0.0
            own_d = min([dist(cand, r) for r in own_refs], default=1e9)
            opp_d = min([dist(cand, r) for r in opp_refs], default=1e9)
            if own_d < opp_d:
                conf = max(0.0, min(1.0, (opp_d - own_d) / (opp_d + 1e-6)))
                return 'own', float(conf)
            else:
                conf = max(0.0, min(1.0, (own_d - opp_d) / (own_d + 1e-6)))
                return 'opponent', float(conf)
        except Exception as e:
            self.logger.error(f"Error classifying jersey: {e}")
            return 'unknown', 0.0
    
    def detect_field_boundaries(self, image: np.ndarray) -> Dict[str, Any]:
        """Nhận diện biên sân bóng"""
        try:
            # Convert to HSV
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            
            # Create field mask
            field_mask = cv2.inRange(hsv, self.color_ranges['field']['lower'], 
                                   self.color_ranges['field']['upper'])
            
            # Find contours
            contours, _ = cv2.findContours(field_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            if contours:
                # Find largest contour (should be the field)
                largest_contour = max(contours, key=cv2.contourArea)
                
                # Get bounding rectangle
                x, y, w, h = cv2.boundingRect(largest_contour)
                
                # Get field corners
                corners = self._get_field_corners(largest_contour)
                
                return {
                    'bounding_box': (x, y, w, h),
                    'corners': corners,
                    'field_area': cv2.contourArea(largest_contour),
                    'field_mask': field_mask
                }
            
            return {}
            
        except Exception as e:
            self.logger.error(f"Error detecting field boundaries: {e}")
            return {}

    def detect_goals(self, image: np.ndarray) -> Dict[str, Any]:
        """Nhận diện khung thành gần hai biên để xác định hướng tấn công (zoom-out hỗ trợ tốt)."""
        try:
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.color_ranges['goal_white']['lower'], self.color_ranges['goal_white']['upper'])
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            height, width = image.shape[:2]
            left_goal_score = 0.0
            right_goal_score = 0.0
            left_boxes = []
            right_boxes = []
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                area = w * h
                if area < 500:  # filter very small
                    continue
                # Prefer tall, thin-ish posts near edges
                aspect = h / (w + 1e-6)
                edge_proximity = min(x + w, width - x) / width  # smaller is closer to edge
                score = (aspect * 0.6) + ((1.0 - edge_proximity) * 0.4)
                if x + w/2 < width * 0.2:
                    left_goal_score += score
                    left_boxes.append((x, y, w, h))
                elif x + w/2 > width * 0.8:
                    right_goal_score += score
                    right_boxes.append((x, y, w, h))
            return {
                'left_goal_score': float(left_goal_score),
                'right_goal_score': float(right_goal_score),
                'left_boxes': left_boxes,
                'right_boxes': right_boxes
            }
        except Exception as e:
            self.logger.error(f"Error detecting goals: {e}")
            return {}
    
    def detect_game_ui_elements(self, image: np.ndarray) -> Dict[str, Any]:
        """Nhận diện các phần tử UI của game"""
        try:
            ui_elements = {}
            
            # Score detection
            score_region = image[50:100, 800:1120]  # Approximate score area
            score_text = self._extract_text_from_region(score_region)
            if score_text:
                ui_elements['score'] = score_text
            
            # Time detection
            time_region = image[50:100, 400:600]  # Approximate time area
            time_text = self._extract_text_from_region(time_region)
            if time_text:
                ui_elements['time'] = time_text
            
            # Possession bar detection
            possession_region = image[100:120, 800:1120]
            possession_value = self._detect_possession_bar(possession_region)
            if possession_value is not None:
                ui_elements['possession'] = possession_value
            
            # Formation detection
            formation_info = self._detect_formation(image)
            if formation_info:
                ui_elements['formation'] = formation_info
            
            return ui_elements
            
        except Exception as e:
            self.logger.error(f"Error detecting UI elements: {e}")
            return {}
    
    def _template_matching(self, image: np.ndarray, template: np.ndarray, 
                          object_type: str) -> List[Dict[str, Any]]:
        """Template matching để nhận diện đối tượng"""
        try:
            # Convert to grayscale
            if len(image.shape) == 3:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            else:
                gray = image
            
            # Template matching
            result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
            
            # Find locations where matching exceeds threshold
            locations = np.where(result >= self.confidence_threshold)
            
            detections = []
            for pt in zip(*locations[::-1]):
                detection = {
                    'type': object_type,
                    'bbox': (pt[0], pt[1], template.shape[1], template.shape[0]),
                    'confidence': float(result[pt[1], pt[0]]),
                    'method': 'template_matching'
                }
                detections.append(detection)
            
            return detections
            
        except Exception as e:
            self.logger.error(f"Error in template matching: {e}")
            return []
    
    def _color_based_detection(self, image: np.ndarray, object_type: str) -> List[Dict[str, Any]]:
        """Nhận diện dựa trên màu sắc"""
        try:
            if object_type not in self.color_ranges:
                return []
            
            # Convert to HSV
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            
            # Create mask
            mask = cv2.inRange(hsv, self.color_ranges[object_type]['lower'],
                              self.color_ranges[object_type]['upper'])
            
            # Find contours
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            detections = []
            for contour in contours:
                area = cv2.contourArea(contour)
                if area > 100:  # Filter small contours
                    x, y, w, h = cv2.boundingRect(contour)
                    
                    detection = {
                        'type': object_type,
                        'bbox': (x, y, w, h),
                        'confidence': 0.8,  # Default confidence for color detection
                        'method': 'color_based',
                        'area': area
                    }
                    detections.append(detection)
            
            return detections
            
        except Exception as e:
            self.logger.error(f"Error in color-based detection: {e}")
            return []

    def detect_hud_indicators(self, image: np.ndarray) -> Dict[str, Any]:
        """Detect HUD indicators (filled/hollow) using multi-scale template matching with NMS."""
        try:
            # Limit search to upper 2/3 height (HUD sits above heads)
            h_img, w_img = image.shape[:2]
            roi_img = image[: int(h_img * 0.7), :]
            gray_full = cv2.cvtColor(roi_img, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray_full, (3, 3), 0.5)

            results = {'filled': [], 'hollow': []}

            def run_multiscale(template: np.ndarray, label: str):
                if template is None:
                    return
                thr = 0.56
                scales = [0.8, 0.9, 1.0, 1.1, 1.2]
                for s in scales:
                    t = cv2.resize(template, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
                    if t.shape[0] < 8 or t.shape[1] < 8:
                        continue
                    res = cv2.matchTemplate(gray, t, cv2.TM_CCOEFF_NORMED)
                    loc = np.where(res >= thr)
                    th, tw = t.shape[:2]
                    for pt in zip(*loc[::-1]):
                        conf = float(res[pt[1], pt[0]])
                        # Map back to full image coords
                        x, y = int(pt[0]), int(pt[1])
                        results[label].append({'bbox': (x, y, int(tw), int(th)), 'confidence': conf})

            run_multiscale(self.hud_filled_template, 'filled')
            run_multiscale(self.hud_hollow_template, 'hollow')

            # Apply simple NMS per label
            def iou(a, b):
                ax, ay, aw, ah = a
                bx, by, bw, bh = b
                x1 = max(ax, bx)
                y1 = max(ay, by)
                x2 = min(ax + aw, bx + bw)
                y2 = min(ay + ah, by + bh)
                inter = max(0, x2 - x1) * max(0, y2 - y1)
                ua = aw * ah + bw * bh - inter
                return inter / ua if ua > 0 else 0.0

            def nms(items, iou_thr=0.3):
                items = sorted(items, key=lambda d: d['confidence'], reverse=True)
                kept = []
                for it in items:
                    if all(iou(it['bbox'], k['bbox']) <= iou_thr for k in kept):
                        kept.append(it)
                return kept

            results['filled'] = nms(results['filled'])
            results['hollow'] = nms(results['hollow'])
            return results
        except Exception as e:
            self.logger.error(f"Error detecting HUD indicators: {e}")
            return {'filled': [], 'hollow': []}
    
    def _contour_based_detection(self, image: np.ndarray, object_type: str) -> List[Dict[str, Any]]:
        """Nhận diện dựa trên contour"""
        try:
            # Convert to grayscale
            if len(image.shape) == 3:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            else:
                gray = image
            
            # Apply Gaussian blur
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            
            # Edge detection
            edges = cv2.Canny(blurred, 50, 150)
            
            # Find contours
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            detections = []
            for contour in contours:
                area = cv2.contourArea(contour)
                
                # Filter based on object type
                if object_type == 'ball' and 50 < area < 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    
                    # Check if it's roughly circular
                    perimeter = cv2.arcLength(contour, True)
                    circularity = 4 * np.pi * area / (perimeter * perimeter) if perimeter > 0 else 0
                    
                    if circularity > 0.7:  # Circular objects
                        detection = {
                            'type': object_type,
                            'bbox': (x, y, w, h),
                            'confidence': 0.7,
                            'method': 'contour_based',
                            'circularity': circularity
                        }
                        detections.append(detection)
                
                elif object_type == 'player' and 1000 < area < 10000:
                    x, y, w, h = cv2.boundingRect(contour)
                    
                    # Check aspect ratio (players are usually taller than wide)
                    aspect_ratio = h / w if w > 0 else 0
                    if 1.5 < aspect_ratio < 3.0:
                        detection = {
                            'type': object_type,
                            'bbox': (x, y, w, h),
                            'confidence': 0.6,
                            'method': 'contour_based',
                            'aspect_ratio': aspect_ratio
                        }
                        detections.append(detection)
            
            return detections
            
        except Exception as e:
            self.logger.error(f"Error in contour-based detection: {e}")
            return []
    
    def _hog_person_detection(self, image: np.ndarray) -> List[Dict[str, Any]]:
        """Sử dụng HOG để nhận diện người"""
        try:
            # Initialize HOG descriptor
            hog = cv2.HOGDescriptor()
            hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
            
            # Detect people
            boxes, weights = hog.detectMultiScale(image, winStride=(8, 8), padding=(4, 4), scale=1.05)
            
            detections = []
            for (x, y, w, h), weight in zip(boxes, weights):
                detection = {
                    'type': 'player',
                    'bbox': (int(x), int(y), int(w), int(h)),
                    'confidence': float(weight),
                    'method': 'hog_detection'
                }
                detections.append(detection)
            
            return detections
            
        except Exception as e:
            self.logger.error(f"Error in HOG detection: {e}")
            return []
    
    def _apply_nms(self, detections: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Áp dụng Non-Maximum Suppression"""
        try:
            if not detections:
                return []
            
            # Sort by confidence
            detections.sort(key=lambda x: x['confidence'], reverse=True)
            
            final_detections = []
            
            for detection in detections:
                should_add = True
                
                for final_detection in final_detections:
                    if self._calculate_iou(detection['bbox'], final_detection['bbox']) > self.nms_threshold:
                        should_add = False
                        break
                
                if should_add:
                    final_detections.append(detection)
            
            return final_detections
            
        except Exception as e:
            self.logger.error(f"Error applying NMS: {e}")
            return detections
    
    def _calculate_iou(self, bbox1: Tuple[int, int, int, int], 
                       bbox2: Tuple[int, int, int, int]) -> float:
        """Tính toán Intersection over Union"""
        try:
            x1, y1, w1, h1 = bbox1
            x2, y2, w2, h2 = bbox2
            
            # Calculate intersection
            x_left = max(x1, x2)
            y_top = max(y1, y2)
            x_right = min(x1 + w1, x2 + w2)
            y_bottom = min(y1 + h1, y2 + h2)
            
            if x_right < x_left or y_bottom < y_top:
                return 0.0
            
            intersection_area = (x_right - x_left) * (y_bottom - y_top)
            
            # Calculate union
            bbox1_area = w1 * h1
            bbox2_area = w2 * h2
            union_area = bbox1_area + bbox2_area - intersection_area
            
            return intersection_area / union_area if union_area > 0 else 0.0
            
        except Exception as e:
            self.logger.error(f"Error calculating IoU: {e}")
            return 0.0
    
    def _get_field_corners(self, contour: np.ndarray) -> List[Tuple[int, int]]:
        """Lấy các góc của sân bóng"""
        try:
            # Approximate contour to polygon
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            
            # Get corners
            corners = []
            for point in approx:
                corners.append((int(point[0][0]), int(point[0][1])))
            
            return corners
            
        except Exception as e:
            self.logger.error(f"Error getting field corners: {e}")
            return []
    
    def _extract_text_from_region(self, region: np.ndarray) -> Optional[str]:
        """Trích xuất text từ một vùng hình ảnh"""
        try:
            if region is None or region.size == 0 or pytesseract is None:
                return None
            gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
            gray = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            custom_oem_psm_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789:/'
            text = pytesseract.image_to_string(thresh, config=custom_oem_psm_config)
            text = text.strip()
            return text if text else None
            
        except Exception as e:
            self.logger.error(f"Error extracting text: {e}")
            return None
    
    def _detect_possession_bar(self, region: np.ndarray) -> Optional[float]:
        """Nhận diện thanh possession"""
        try:
            # Convert to grayscale
            gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
            
            # Find the possession bar (usually a filled rectangle)
            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            
            # Find contours
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            if contours:
                # Find the largest contour (possession bar)
                largest_contour = max(contours, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(largest_contour)
                
                # Calculate possession percentage based on position
                total_width = region.shape[1]
                possession_percentage = (x + w/2) / total_width
                
                return possession_percentage
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error detecting possession bar: {e}")
            return None
    
    def _detect_formation(self, image: np.ndarray) -> Optional[Dict[str, Any]]:
        """Nhận diện formation của đội"""
        try:
            # This would require more sophisticated analysis
            # For now, return basic formation info
            return {
                'type': '4-4-2',  # Default formation
                'confidence': 0.5
            }
            
        except Exception as e:
            self.logger.error(f"Error detecting formation: {e}")
            return None

class GameStateAnalyzer:
    """Phân tích trạng thái game từ hình ảnh"""
    
    def __init__(self):
        self.logger = get_logger(__name__)
        self.detector = GameObjectDetector()
        self.analysis_history = deque(maxlen=100)
        
    def analyze_game_state(self, image: np.ndarray) -> Dict[str, Any]:
        """Phân tích toàn bộ trạng thái game"""
        try:
            start_time = time.time()
            
            # Detect objects
            ball_detections = self.detector.detect_ball(image)
            player_detections = self.detector.detect_players(image)
            field_info = self.detector.detect_field_boundaries(image)
            goal_info = self.detector.detect_goals(image)
            ui_elements = self.detector.detect_game_ui_elements(image)
            hud = self.detector.detect_hud_indicators(image)
            
            # Analyze game situation
            game_situation = self._analyze_game_situation(
                ball_detections, player_detections, field_info
            )

            # Possession estimation
            possession_label = 'unknown'
            possession_conf = 0.0
            ball_pos = None
            if ball_detections:
                best_ball = max(ball_detections, key=lambda x: x['confidence'])
                x, y, w, h = best_ball['bbox']
                ball_pos = (x + w/2, y + h/2)
                # Find nearest player
                nearest = None
                nearest_dist = 1e9
                for det in player_detections:
                    px, py, pw, ph = det['bbox']
                    pcx = px + pw/2
                    pcy = py + ph/2
                    d = (pcx - ball_pos[0])**2 + (pcy - ball_pos[1])**2
                    if d < nearest_dist:
                        nearest = det
                        nearest_dist = d
                if nearest is not None:
                    label, conf = self.detector.classify_player_jersey(image, nearest['bbox'])
                    possession_label = label
                    possession_conf = conf
            
            # Create comprehensive analysis
            # If HUD filled exists near a player, assume own possession (high confidence)
            if hud.get('filled'):
                # Pick highest confidence
                best_hud = max(hud['filled'], key=lambda x: x['confidence'])
                possession_label = 'own'
                possession_conf = max(possession_conf, min(1.0, 0.8 + best_hud['confidence'] * 0.2))

            analysis = {
                'timestamp': time.time(),
                'ball_detections': ball_detections,
                'player_detections': player_detections,
                'field_info': field_info,
                'goal_info': goal_info,
                'ui_elements': ui_elements,
                'hud': hud,
                'game_situation': game_situation,
                'possession': {'label': possession_label, 'confidence': possession_conf},
                'processing_time': time.time() - start_time
            }
            
            # Store in history
            self.analysis_history.append(analysis)
            
            return analysis
            
        except Exception as e:
            self.logger.error(f"Error analyzing game state: {e}")
            return {}
    
    def _analyze_game_situation(self, ball_detections: List[Dict[str, Any]], 
                               player_detections: List[Dict[str, Any]], 
                               field_info: Dict[str, Any]) -> Dict[str, Any]:
        """Phân tích tình huống game"""
        try:
            situation = {}
            
            # Ball analysis
            if ball_detections:
                best_ball = max(ball_detections, key=lambda x: x['confidence'])
                situation['ball_position'] = best_ball['bbox'][:2]  # (x, y)
                situation['ball_confidence'] = best_ball['confidence']
            else:
                situation['ball_position'] = None
                situation['ball_confidence'] = 0.0
            
            # Player analysis
            if player_detections:
                situation['player_count'] = len(player_detections)
                situation['player_positions'] = [det['bbox'][:2] for det in player_detections]
                
                # Calculate player density in different areas
                situation['player_density'] = self._calculate_player_density(
                    player_detections, field_info
                )
            else:
                situation['player_count'] = 0
                situation['player_positions'] = []
                situation['player_density'] = {}
            
            # Field analysis
            if field_info:
                situation['field_available'] = True
                situation['field_area'] = field_info.get('field_area', 0)
            else:
                situation['field_available'] = False
                situation['field_area'] = 0
            
            # Game phase estimation
            situation['game_phase'] = self._estimate_game_phase(situation)
            
            return situation
            
        except Exception as e:
            self.logger.error(f"Error analyzing game situation: {e}")
            return {}
    
    def _calculate_player_density(self, player_detections: List[Dict[str, Any]], 
                                 field_info: Dict[str, Any]) -> Dict[str, float]:
        """Tính toán mật độ cầu thủ ở các vùng khác nhau"""
        try:
            density = {
                'defense': 0.0,
                'midfield': 0.0,
                'attack': 0.0
            }
            
            if not field_info or not player_detections:
                return density
            
            field_width = field_info.get('bounding_box', (0, 0, 1920, 1080))[2]
            
            for player in player_detections:
                x, y, w, h = player['bbox']
                player_center_x = x + w/2
                
                # Categorize by field position
                if player_center_x < field_width * 0.33:
                    density['defense'] += 1
                elif player_center_x < field_width * 0.66:
                    density['midfield'] += 1
                else:
                    density['attack'] += 1
            
            # Normalize by total players
            total_players = len(player_detections)
            if total_players > 0:
                for area in density:
                    density[area] /= total_players
            
            return density
            
        except Exception as e:
            self.logger.error(f"Error calculating player density: {e}")
            return {'defense': 0.0, 'midfield': 0.0, 'attack': 0.0}
    
    def _estimate_game_phase(self, situation: Dict[str, Any]) -> str:
        """Ước tính phase của game"""
        try:
            if not situation.get('ball_position'):
                return 'unknown'
            
            ball_x, ball_y = situation['ball_position']
            
            # Analyze ball position and player density
            if ball_x < 640:  # Left third
                if situation.get('player_density', {}).get('defense', 0) > 0.4:
                    return 'defense'
                else:
                    return 'counter_attack'
            elif ball_x < 1280:  # Middle third
                return 'midfield_battle'
            else:  # Right third
                if situation.get('player_density', {}).get('attack', 0) > 0.4:
                    return 'attack'
                else:
                    return 'build_up'
            
        except Exception as e:
            self.logger.error(f"Error estimating game phase: {e}")
            return 'unknown'
    
    def get_analysis_history(self) -> List[Dict[str, Any]]:
        """Lấy lịch sử phân tích"""
        return list(self.analysis_history)
    
    def get_trend_analysis(self) -> Dict[str, Any]:
        """Phân tích xu hướng từ lịch sử"""
        try:
            if len(self.analysis_history) < 10:
                return {'status': 'insufficient_data'}
            
            trends = {}
            
            # Ball position trends
            ball_positions = [analysis.get('game_situation', {}).get('ball_position') 
                            for analysis in self.analysis_history if analysis.get('game_situation', {}).get('ball_position')]
            
            if ball_positions:
                x_positions = [pos[0] for pos in ball_positions]
                y_positions = [pos[1] for pos in ball_positions]
                
                trends['ball_movement'] = {
                    'x_trend': 'left' if np.mean(x_positions[-5:]) < np.mean(x_positions[:-5]) else 'right',
                    'y_trend': 'up' if np.mean(y_positions[-5:]) < np.mean(y_positions[:-5]) else 'down',
                    'speed': np.mean([abs(x_positions[i] - x_positions[i-1]) 
                                    for i in range(1, len(x_positions))])
                }
            
            # Game phase trends
            phases = [analysis.get('game_situation', {}).get('game_phase', 'unknown') 
                     for analysis in self.analysis_history]
            
            if phases:
                recent_phases = phases[-5:]
                trends['phase_stability'] = len(set(recent_phases)) == 1
            
            return trends
            
        except Exception as e:
            self.logger.error(f"Error getting trend analysis: {e}")
            return {'status': 'error', 'message': str(e)}

class ComputerVisionSystem:
    """Hệ thống Computer Vision chính"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = get_logger(__name__)
        
        # Components
        self.detector = GameObjectDetector()
        self.analyzer = GameStateAnalyzer()
        
        # Performance tracking
        self.processing_times = deque(maxlen=100)
        self.detection_accuracy = deque(maxlen=100)
        
        # Threading
        self.lock = threading.Lock()
        self.is_active = False
        
        self.logger.info("Computer Vision System initialized")
    
    def start(self):
        """Khởi động hệ thống"""
        try:
            with self.lock:
                self.is_active = True
                self.logger.info("Computer Vision System started")
                return True
        except Exception as e:
            self.logger.error(f"Error starting Computer Vision System: {e}")
            return False
    
    def stop(self):
        """Dừng hệ thống"""
        try:
            with self.lock:
                self.is_active = False
                self.logger.info("Computer Vision System stopped")
                return True
        except Exception as e:
            self.logger.error(f"Error stopping Computer Vision System: {e}")
            return False
    
    @log_performance
    def process_frame(self, image: np.ndarray) -> Dict[str, Any]:
        """Xử lý một frame hình ảnh"""
        try:
            if not self.is_active:
                return {}
            
            start_time = time.time()
            
            # Analyze game state
            analysis = self.analyzer.analyze_game_state(image)
            
            # Record processing time
            processing_time = time.time() - start_time
            self.processing_times.append(processing_time)
            
            # Update performance metrics
            self._update_performance_metrics(analysis)
            
            return analysis
            
        except Exception as e:
            self.logger.error(f"Error processing frame: {e}")
            return {}
    
    def _update_performance_metrics(self, analysis: Dict[str, Any]):
        """Cập nhật metrics hiệu suất"""
        try:
            # Detection accuracy (based on confidence scores)
            if analysis.get('ball_detections'):
                ball_confidence = max([det['confidence'] for det in analysis['ball_detections']])
                self.detection_accuracy.append(ball_confidence)
            
            if analysis.get('player_detections'):
                player_confidence = np.mean([det['confidence'] for det in analysis['player_detections']])
                self.detection_accuracy.append(player_confidence)
                
        except Exception as e:
            self.logger.error(f"Error updating performance metrics: {e}")
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Lấy thống kê hiệu suất"""
        try:
            stats = {}
            
            if self.processing_times:
                stats['avg_processing_time'] = np.mean(self.processing_times)
                stats['max_processing_time'] = np.max(self.processing_times)
                stats['min_processing_time'] = np.min(self.processing_times)
            
            if self.detection_accuracy:
                stats['avg_detection_accuracy'] = np.mean(self.detection_accuracy)
                stats['min_detection_accuracy'] = np.min(self.detection_accuracy)
            
            stats['total_frames_processed'] = len(self.processing_times)
            stats['system_active'] = self.is_active
            
            return stats
            
        except Exception as e:
            self.logger.error(f"Error getting performance stats: {e}")
            return {}
    
    def cleanup(self):
        """Dọn dẹp tài nguyên"""
        try:
            self.stop()
            self.logger.info("Computer Vision System cleanup completed")
        except Exception as e:
            self.logger.error(f"Error during Computer Vision System cleanup: {e}") 
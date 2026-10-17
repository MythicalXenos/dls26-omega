#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Decision Maker for Dream League Soccer
AI logic for making game decisions based on game state and situation analysis
"""

import random
import time
from typing import Dict, Any, List, Optional, Tuple
import json
from pathlib import Path
from enum import Enum
from utils.logger import get_logger, log_performance
from game_logic.action_executor import ActionType

class GameSituation(Enum):
    """Game situations for decision making"""
    ATTACKING = "attacking"
    DEFENDING = "defending"
    COUNTER_ATTACK = "counter_attack"
    SET_PIECE = "set_piece"
    TRANSITION = "transition"
    POSSESSION_LOST = "possession_lost"
    POSSESSION_GAINED = "possession_gained"
    GOAL_SCORING_CHANCE = "goal_scoring_chance"
    DEFENSIVE_CRISIS = "defensive_crisis"

class DecisionMaker:
    """AI decision maker for DLS gameplay"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = get_logger(__name__)
        
        # Decision parameters
        self.aggression_level = config.get('decision', {}).get('AGGRESSION_LEVEL', 0.7)
        self.risk_tolerance = config.get('decision', {}).get('RISK_TOLERANCE', 0.6)
        self.possession_priority = config.get('decision', {}).get('POSSESSION_PRIORITY', 0.8)
        
        # Learning parameters
        self.success_rate = {}  # Track success rate for different actions
        self.learning_rate = 0.1
        self.exploration_rate = 0.2
        
        # Performance tracking
        self.decision_count = 0
        self.successful_decisions = 0
        self.last_decision_time = time.time()
        
        # Initialize action success rates
        self._initialize_action_rates()
        
        self.logger.info("Decision maker initialized")
        
        # Parameter tuner for actions (shoot/pass mainly)
        self.param_tuner = ActionParamTuner(self.config)
    
    def _initialize_action_rates(self):
        """Initialize success rates for different actions"""
        actions = [action.value for action in ActionType]
        for action in actions:
            self.success_rate[action] = 0.5  # Start with neutral success rate
    
    @log_performance
    def get_decision(self, game_state: str, game_context: Dict[str, Any]) -> Dict[str, Any]:
        """Get decision based on current game state and context"""
        try:
            self.decision_count += 1
            
            # Analyze game situation
            situation = self._analyze_situation(game_state, game_context)
            
            # Get appropriate action
            action = self._select_action(situation, game_context)
            
            # Build execution context for the chosen action (with param tuning)
            base_context = self._build_action_context(action, situation, game_context)
            action_context = self.param_tuner.get_tuned_context(action, situation, game_context, base_context)

            # Apply learning and adaptation
            self._adapt_strategy(situation, action)
            
            # Update performance stats
            self._update_decision_stats()
            
            decision = {
                'action': action,
                'situation': situation.value,
                'context': action_context,
                'confidence': self._calculate_confidence(action, situation),
                'reasoning': self._get_reasoning(action, situation, game_context),
                'timestamp': time.time()
            }
            
            self.logger.debug(f"Decision made: {action.value} for {situation.value}")
            return decision
            
        except Exception as e:
            self.logger.error(f"Error making decision: {e}")
            return self._get_fallback_decision()
    
    def _analyze_situation(self, game_state: str, context: Dict[str, Any]) -> GameSituation:
        """Analyze current game situation"""
        try:
            # Extract key context information
            ball_possession = context.get('ball_possession', 'unknown')
            field_position = context.get('field_position', 'center')
            score_difference = context.get('score_difference', 0)
            time_remaining = context.get('time_remaining', 90)
            player_energy = context.get('player_energy', 100)
            
            # Determine situation based on context
            if game_state == 'penalty_kick':
                return GameSituation.SET_PIECE
            elif game_state == 'corner_kick':
                return GameSituation.SET_PIECE
            elif game_state == 'free_kick':
                return GameSituation.SET_PIECE
            
            # Analyze possession and field position
            if ball_possession == 'own':
                if field_position in ['opponent_half', 'penalty_area']:
                    return GameSituation.GOAL_SCORING_CHANCE
                elif field_position in ['own_half', 'center']:
                    return GameSituation.ATTACKING
                else:
                    return GameSituation.TRANSITION
            elif ball_possession == 'opponent':
                if field_position in ['own_penalty_area', 'own_half']:
                    return GameSituation.DEFENSIVE_CRISIS
                else:
                    return GameSituation.DEFENDING
            elif ball_possession == 'contested':
                return GameSituation.TRANSITION
            
            # Default to transition
            return GameSituation.TRANSITION
            
        except Exception as e:
            self.logger.error(f"Error analyzing situation: {e}")
            return GameSituation.TRANSITION
    
    def _select_action(self, situation: GameSituation, context: Dict[str, Any]) -> ActionType:
        """Select appropriate action based on situation"""
        try:
            # High-priority overrides
            if context.get('hud_hollow_near_ball') and situation in (GameSituation.DEFENDING, GameSituation.DEFENSIVE_CRISIS, GameSituation.TRANSITION):
                return ActionType.SWITCH_PLAYER

            # Get available actions for the situation
            available_actions = self._get_available_actions(situation, context)
            
            if not available_actions:
                return ActionType.WAIT
            
            # Apply learning-based selection
            if random.random() < self.exploration_rate:
                # Exploration: try random action
                action = random.choice(available_actions)
            else:
                # Exploitation: choose best action based on success rate
                action = self._select_best_action(available_actions)
            
            return action
            
        except Exception as e:
            self.logger.error(f"Error selecting action: {e}")
            return ActionType.WAIT
    
    def _get_available_actions(self, situation: GameSituation, context: Dict[str, Any]) -> List[ActionType]:
        """Get available actions for current situation"""
        try:
            actions = []
            
            if situation == GameSituation.ATTACKING:
                actions = [ActionType.MOVE, ActionType.PASS, ActionType.SHOOT, ActionType.SKILL]
            elif situation == GameSituation.DEFENDING:
                actions = [ActionType.MOVE, ActionType.TACKLE, ActionType.SWITCH_PLAYER]
            elif situation == GameSituation.COUNTER_ATTACK:
                actions = [ActionType.MOVE, ActionType.PASS, ActionType.SHOOT]
            elif situation == GameSituation.SET_PIECE:
                actions = [ActionType.SHOOT, ActionType.PASS, ActionType.MOVE]
            elif situation == GameSituation.TRANSITION:
                actions = [ActionType.MOVE, ActionType.PASS, ActionType.SWITCH_PLAYER]
            elif situation == GameSituation.GOAL_SCORING_CHANCE:
                actions = [ActionType.SHOOT, ActionType.PASS, ActionType.SKILL]
            elif situation == GameSituation.DEFENSIVE_CRISIS:
                actions = [ActionType.TACKLE, ActionType.MOVE, ActionType.SWITCH_PLAYER]
            else:
                actions = [ActionType.WAIT]
            
            # Filter actions based on context constraints
            filtered_actions = self._filter_actions_by_context(actions, context)
            
            return filtered_actions
            
        except Exception as e:
            self.logger.error(f"Error getting available actions: {e}")
            return [ActionType.WAIT]
    
    def _filter_actions_by_context(self, actions: List[ActionType], context: Dict[str, Any]) -> List[ActionType]:
        """Filter actions based on context constraints"""
        try:
            filtered = []
            
            for action in actions:
                if self._is_action_valid(action, context):
                    filtered.append(action)
            
            return filtered
            
        except Exception as e:
            self.logger.error(f"Error filtering actions: {e}")
            return actions
    
    def _is_action_valid(self, action: ActionType, context: Dict[str, Any]) -> bool:
        """Check if action is valid in current context"""
        try:
            # Check player energy
            player_energy = context.get('player_energy', 100)
            if player_energy < 20 and action in [ActionType.SKILL, ActionType.SHOOT]:
                return False
            
            # Check field position for certain actions
            field_position = context.get('field_position', 'center')
            if action == ActionType.SHOOT and field_position not in ['penalty_area', 'opponent_half']:
                return False
            
            # Check ball possession
            ball_possession = context.get('ball_possession', 'unknown')
            if action in [ActionType.SHOOT, ActionType.PASS] and ball_possession != 'own':
                return False
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error checking action validity: {e}")
            return True
    
    def _select_best_action(self, available_actions: List[ActionType]) -> ActionType:
        """Select best action based on success rates"""
        try:
            best_action = available_actions[0]
            best_rate = self.success_rate[best_action.value]
            
            for action in available_actions:
                rate = self.success_rate[action.value]
                if rate > best_rate:
                    best_rate = rate
                    best_action = action
            
            return best_action
            
        except Exception as e:
            self.logger.error(f"Error selecting best action: {e}")
            return available_actions[0] if available_actions else ActionType.WAIT
    
    def _calculate_confidence(self, action: ActionType, situation: GameSituation) -> float:
        """Calculate confidence level for the decision"""
        try:
            base_confidence = self.success_rate[action.value]
            
            # Adjust confidence based on situation
            situation_multiplier = self._get_situation_multiplier(situation)
            
            # Apply aggression and risk tolerance
            aggression_factor = self.aggression_level if action in [ActionType.SHOOT, ActionType.TACKLE] else 1.0
            risk_factor = self.risk_tolerance if action in [ActionType.SKILL, ActionType.SHOOT] else 1.0
            
            confidence = base_confidence * situation_multiplier * aggression_factor * risk_factor
            
            return min(max(confidence, 0.0), 1.0)
            
        except Exception as e:
            self.logger.error(f"Error calculating confidence: {e}")
            return 0.5
    
    def _get_situation_multiplier(self, situation: GameSituation) -> float:
        """Get confidence multiplier for different situations"""
        multipliers = {
            GameSituation.GOAL_SCORING_CHANCE: 1.2,
            GameSituation.ATTACKING: 1.1,
            GameSituation.COUNTER_ATTACK: 1.15,
            GameSituation.SET_PIECE: 1.1,
            GameSituation.TRANSITION: 1.0,
            GameSituation.DEFENDING: 0.9,
            GameSituation.DEFENSIVE_CRISIS: 0.8
        }
        
        return multipliers.get(situation, 1.0)
    
    def _get_reasoning(self, action: ActionType, situation: GameSituation, context: Dict[str, Any]) -> str:
        """Get reasoning for the decision"""
        try:
            reasoning_templates = {
                ActionType.SHOOT: "Shooting due to {situation} and good field position",
                ActionType.PASS: "Passing to maintain possession and create opportunity",
                ActionType.MOVE: "Moving to better position for {situation}",
                ActionType.TACKLE: "Tackling to regain possession in {situation}",
                ActionType.SWITCH_PLAYER: "Switching player for better {situation} coverage",
                ActionType.SKILL: "Using skill move to create space in {situation}",
                ActionType.WAIT: "Waiting for better opportunity in {situation}"
            }
            
            template = reasoning_templates.get(action, "Action selected for {situation}")
            return template.format(situation=situation.value)
            
        except Exception as e:
            self.logger.error(f"Error getting reasoning: {e}")
            return f"Action {action.value} selected for {situation.value}"

    def _build_action_context(self, action: ActionType, situation: GameSituation, 
                              context: Dict[str, Any]) -> Dict[str, Any]:
        """Compose execution context (direction, power, pass type, etc.) for the action."""
        try:
            ball_pos = context.get('ball_position')
            field_pos = context.get('field_position', 'center')
            opponent_pressure = float(context.get('opponent_pressure', 0.0))
            possession = context.get('possession')  # 0..1 if available
            has_possession = context.get('ball_possession') == 'own' or (isinstance(possession, (int, float)) and possession > 0.55)
            distance_to_goal = float(context.get('distance_to_goal', 1.0))  # 0 near goal, 1 far

            # Default contexts
            if action == ActionType.MOVE:
                # Heuristic movement towards opponent goal (assumed right side)
                if field_pos == 'opponent_half':
                    direction = 'forward_right'
                    intensity = 0.9 if opponent_pressure < 0.6 else 0.6
                elif field_pos == 'own_half':
                    # Build up play: move forward with caution
                    direction = 'forward_right'
                    intensity = 0.7 if opponent_pressure < 0.5 else 0.5
                else:
                    direction = 'forward'
                    intensity = 0.7
                return {'direction': direction, 'intensity': intensity, 'duration': 0.4}

            if action == ActionType.PASS:
                # Choose pass type by pressure and distance to goal
                if opponent_pressure > 0.7:
                    pass_type = 'long'
                elif has_possession and distance_to_goal < 0.4:
                    pass_type = 'through'
                else:
                    pass_type = 'short'
                target_direction = 'forward_right' if field_pos != 'own_half' else 'forward'
                return {'pass_type': pass_type, 'target_direction': target_direction}

            if action == ActionType.SHOOT:
                # Power increases as distance_to_goal shrinks (closer → medium power)
                base_power = 1.0 - max(0.0, min(1.0, distance_to_goal))
                power = 0.6 + 0.4 * base_power
                shot_dir = 'right' if field_pos != 'own_half' else 'center'
                return {'power': round(power, 2), 'direction': shot_dir}

            if action == ActionType.TACKLE:
                tackle_type = 'slide' if opponent_pressure > 0.6 else 'normal'
                return {'tackle_type': tackle_type}

            if action == ActionType.SKILL:
                skill_type = 'basic' if opponent_pressure < 0.7 else 'escape'
                return {'skill_type': skill_type}

            if action == ActionType.SWITCH_PLAYER:
                return {'target_player': 'nearest'}

            if action == ActionType.WAIT:
                return {'duration': 0.3}

            if action == ActionType.MENU_NAVIGATION:
                return {'target_menu': 'main', 'action': 'click'}

            return {}
        except Exception as e:
            self.logger.error(f"Error building action context: {e}")
            return {}

    def report_action_outcome(self, action: ActionType, used_context: Dict[str, Any],
                               game_context: Dict[str, Any], reward: float):
        """Report detailed action outcome for parameter tuning."""
        try:
            self.param_tuner.update_stats(action, used_context, game_context, reward)
        except Exception as e:
            self.logger.error(f"Error reporting action outcome: {e}")


class ActionParamTuner:
    """Lightweight bandit-style tuner for action parameters by situation buckets."""
    def __init__(self, config: Dict[str, Any]):
        self.logger = get_logger(__name__)
        self.config = config or {}
        self.storage_path = Path(__file__).parent.parent / 'data' / 'param_tuner.json'
        self.storage_path.parent.mkdir(exist_ok=True)
        self.stats: Dict[str, Dict[str, Dict[str, float]]] = {}
        self._load()
        # Exploration rate for choosing params
        self.epsilon = 0.15

    def _bucketize(self, game_context: Dict[str, Any]) -> Tuple[int, int]:
        distance = float(game_context.get('distance_to_goal', 0.5))
        pressure = float(game_context.get('opponent_pressure', 0.3))
        dist_bin = min(4, int(distance * 5))  # 0..4
        pres_bin = min(4, int(pressure * 5))  # 0..4
        return dist_bin, pres_bin

    def _key(self, action: ActionType, game_context: Dict[str, Any]) -> str:
        dist_bin, pres_bin = self._bucketize(game_context)
        return f"{action.value}:d{dist_bin}:p{pres_bin}"

    def _serialize_params(self, params: Dict[str, Any]) -> str:
        items = sorted((str(k), str(v)) for k, v in params.items())
        return '|'.join([f"{k}:{v}" for k, v in items])

    def _load(self):
        try:
            if self.storage_path.exists():
                with open(self.storage_path, 'r', encoding='utf-8') as f:
                    self.stats = json.load(f)
        except Exception as e:
            self.logger.warning(f"Could not load param tuner data: {e}")

    def _save(self):
        try:
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump(self.stats, f, indent=2, ensure_ascii=False)
        except Exception as e:
            self.logger.error(f"Error saving param tuner data: {e}")

    def get_tuned_context(self, action: ActionType, situation: GameSituation,
                           game_context: Dict[str, Any], base_context: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # Only tune some actions for now
            if action not in {ActionType.SHOOT, ActionType.PASS}:
                return base_context
            key = self._key(action, game_context)
            action_stats = self.stats.get(key, {})
            if not action_stats:
                return base_context
            import random
            if random.random() < self.epsilon:
                return base_context
            # Pick best param by average reward
            best_param = None
            best_score = float('-inf')
            for param_key, values in action_stats.items():
                avg = float(values.get('avg', 0.0))
                count = int(values.get('count', 0))
                if count >= 3 and avg > best_score:
                    best_score = avg
                    best_param = param_key
            if best_param:
                tuned = base_context.copy()
                # Parse back param_key into dict
                for pair in best_param.split('|'):
                    if ':' in pair:
                        k, v = pair.split(':', 1)
                        # Try to cast numeric
                        try:
                            if v.replace('.', '', 1).isdigit():
                                tuned[k] = float(v)
                            else:
                                tuned[k] = v
                        except Exception:
                            tuned[k] = v
                return tuned
            return base_context
        except Exception as e:
            self.logger.error(f"Error getting tuned context: {e}")
            return base_context

    def update_stats(self, action: ActionType, used_context: Dict[str, Any],
                     game_context: Dict[str, Any], reward: float):
        try:
            if action not in {ActionType.SHOOT, ActionType.PASS}:
                return
            key = self._key(action, game_context)
            params_key = self._serialize_params(used_context or {})
            if key not in self.stats:
                self.stats[key] = {}
            if params_key not in self.stats[key]:
                self.stats[key][params_key] = {'avg': 0.0, 'count': 0}
            entry = self.stats[key][params_key]
            count = int(entry['count'])
            avg = float(entry['avg'])
            new_count = count + 1
            new_avg = (avg * count + reward) / new_count
            entry['count'] = new_count
            entry['avg'] = new_avg
            # Persist occasionally
            if new_count % 5 == 0:
                self._save()
        except Exception as e:
            self.logger.error(f"Error updating tuner stats: {e}")
    
    def _adapt_strategy(self, situation: GameSituation, action: ActionType):
        """Adapt strategy based on decision outcome"""
        try:
            # This would be called after action execution to update success rates
            # For now, we'll implement a simple adaptation mechanism
            
            # Adjust exploration rate based on success
            if self.successful_decisions / max(self.decision_count, 1) > 0.6:
                self.exploration_rate = max(0.1, self.exploration_rate * 0.95)
            else:
                self.exploration_rate = min(0.5, self.exploration_rate * 1.05)
            
        except Exception as e:
            self.logger.error(f"Error adapting strategy: {e}")
    
    def _get_fallback_decision(self) -> Dict[str, Any]:
        """Get fallback decision when error occurs"""
        return {
            'action': ActionType.WAIT,
            'situation': GameSituation.TRANSITION.value,
            'confidence': 0.3,
            'reasoning': 'Fallback decision due to error',
            'timestamp': time.time()
        }
    
    def _update_decision_stats(self):
        """Update decision performance statistics"""
        current_time = time.time()
        
        if current_time - self.last_decision_time > 60:  # Every minute
            decisions_per_minute = self.decision_count / ((current_time - self.last_decision_time) / 60)
            success_rate = self.successful_decisions / max(self.decision_count, 1)
            
            self.logger.debug(f"Decision rate: {decisions_per_minute:.2f} per minute, Success rate: {success_rate:.2%}")
            
            # Reset counters
            self.decision_count = 0
            self.successful_decisions = 0
            self.last_decision_time = current_time
    
    def report_action_result(self, action: ActionType, success: bool, context: Dict[str, Any]):
        """Report the result of an action for learning"""
        try:
            # Update success rate for the action
            current_rate = self.success_rate[action.value]
            
            if success:
                new_rate = current_rate + self.learning_rate * (1.0 - current_rate)
                self.successful_decisions += 1
            else:
                new_rate = current_rate + self.learning_rate * (0.0 - current_rate)
            
            self.success_rate[action.value] = new_rate
            
            # Log the learning
            self.logger.debug(f"Action {action.value} {'succeeded' if success else 'failed'}, "
                            f"success rate updated to {new_rate:.3f}")
            
        except Exception as e:
            self.logger.error(f"Error reporting action result: {e}")
    
    def get_decision_stats(self) -> Dict[str, Any]:
        """Get decision making performance statistics"""
        current_time = time.time()
        uptime = current_time - self.last_decision_time + 60
        
        return {
            'total_decisions': self.decision_count,
            'successful_decisions': self.successful_decisions,
            'success_rate': self.successful_decisions / max(self.decision_count, 1),
            'uptime_seconds': uptime,
            'decisions_per_minute': self.decision_count / (uptime / 60) if uptime > 0 else 0,
            'exploration_rate': self.exploration_rate,
            'action_success_rates': self.success_rate.copy()
        }
    
    def set_parameters(self, aggression: float = None, risk_tolerance: float = None, 
                      possession_priority: float = None):
        """Set decision parameters"""
        if aggression is not None and 0.0 <= aggression <= 1.0:
            self.aggression_level = aggression
            self.logger.info(f"Aggression level set to {aggression}")
        
        if risk_tolerance is not None and 0.0 <= risk_tolerance <= 1.0:
            self.risk_tolerance = risk_tolerance
            self.logger.info(f"Risk tolerance set to {risk_tolerance}")
        
        if possession_priority is not None and 0.0 <= possession_priority <= 1.0:
            self.possession_priority = possession_priority
            self.logger.info(f"Possession priority set to {possession_priority}")
    
    def reset_learning(self):
        """Reset learning state"""
        self.success_rate.clear()
        self._initialize_action_rates()
        self.exploration_rate = 0.2
        self.successful_decisions = 0
        self.decision_count = 0
        self.logger.info("Decision maker learning reset") 
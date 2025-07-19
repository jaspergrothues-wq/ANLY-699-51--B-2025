import pygame
import sys
import math
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
DARK_BLUE = (0, 0, 100)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
ORANGE = (255, 165, 0)
DARK_GREEN = (0, 100, 0)
MAROON = (128, 0, 0)
GOLD = (255, 215, 0)
DARK_RED = (139, 0, 0)
NAVY = (0, 0, 128)
TEAL = (0, 128, 128)

# Economics Questions for Beijing Level
ECON_QUESTIONS = [
    {
        "question": "What is the basic economic problem?",
        "options": ["A) Inflation", "B) Scarcity", "C) Unemployment", "D) Recession"],
        "correct": 1,
        "explanation": "Scarcity - unlimited wants vs limited resources"
    },
    {
        "question": "In a market economy, prices are determined by:",
        "options": ["A) Government", "B) Supply and demand", "C) Businesses only", "D) Consumers only"],
        "correct": 1,
        "explanation": "Supply and demand forces set market prices"
    },
    {
        "question": "What is GDP?",
        "options": ["A) Government Debt Product", "B) Gross Domestic Product", "C) Global Development Plan", "D) Great Depression Period"],
        "correct": 1,
        "explanation": "GDP measures total economic output of a country"
    },
    {
        "question": "Which represents opportunity cost?",
        "options": ["A) Money spent", "B) Time wasted", "C) Next best alternative", "D) Total cost"],
        "correct": 2,
        "explanation": "Opportunity cost is the value of the next best alternative"
    },
    {
        "question": "What causes inflation?",
        "options": ["A) Too much money chasing too few goods", "B) Low employment", "C) High savings", "D) Reduced spending"],
        "correct": 0,
        "explanation": "Inflation occurs when demand exceeds supply"
    },
    {
        "question": "In economics, utility means:",
        "options": ["A) Electric bill", "B) Usefulness", "C) Satisfaction from consumption", "D) Government service"],
        "correct": 2,
        "explanation": "Utility is the satisfaction gained from consuming goods"
    },
    {
        "question": "What is a monopoly?",
        "options": ["A) Many sellers", "B) Single seller", "C) Government control", "D) Foreign trade"],
        "correct": 1,
        "explanation": "A monopoly has only one seller in the market"
    },
    {
        "question": "Microeconomics studies:",
        "options": ["A) National economy", "B) Individual firms/consumers", "C) Global trade", "D) Government policy"],
        "correct": 1,
        "explanation": "Microeconomics focuses on individual economic units"
    }
]

# Database/SQL Questions for Minneapolis Level
DATABASE_QUESTIONS = [
    {
        "question": "Which SQL command retrieves data from a database?",
        "options": ["A) INSERT", "B) SELECT", "C) UPDATE", "D) DELETE"],
        "correct": 1,
        "explanation": "SELECT is used to query and retrieve data"
    },
    {
        "question": "What does PRIMARY KEY ensure in a database?",
        "options": ["A) Fast queries", "B) Unique identification", "C) Data sorting", "D) Backup creation"],
        "correct": 1,
        "explanation": "Primary keys uniquely identify each record"
    },
    {
        "question": "Which is the correct SQL syntax to create a table?",
        "options": ["A) MAKE TABLE", "B) CREATE TABLE", "C) NEW TABLE", "D) BUILD TABLE"],
        "correct": 1,
        "explanation": "CREATE TABLE is the standard SQL command"
    },
    {
        "question": "What is data normalization?",
        "options": ["A) Making data bigger", "B) Removing duplicate data", "C) Encrypting data", "D) Backing up data"],
        "correct": 1,
        "explanation": "Normalization eliminates redundancy and improves integrity"
    },
    {
        "question": "Which SQL clause filters results?",
        "options": ["A) GROUP BY", "B) ORDER BY", "C) WHERE", "D) HAVING"],
        "correct": 2,
        "explanation": "WHERE clause filters rows based on conditions"
    },
    {
        "question": "What is a foreign key?",
        "options": ["A) A key from another country", "B) A reference to another table", "C) An encrypted key", "D) A backup key"],
        "correct": 1,
        "explanation": "Foreign keys link tables together"
    }
]

# Fraud Detection Scenarios for Digital River Level
FRAUD_SCENARIOS = [
    {
        "question": "Customer buys $5000 laptop, billing address in USA, shipping to Russia. Credit card issued yesterday.",
        "options": ["A) Approve - Normal purchase", "B) Flag - Suspicious location", "C) Flag - New card + high value", "D) Approve - Just expensive taste"],
        "correct": 2,
        "explanation": "New card + high value + unusual shipping pattern = fraud risk"
    },
    {
        "question": "Regular customer (2 years) buys $50 software, same address as always, normal payment method.",
        "options": ["A) Approve - Trusted customer", "B) Flag - Too cheap", "C) Flag - Software suspicious", "D) Manual review needed"],
        "correct": 0,
        "explanation": "Established customer with normal purchase pattern"
    },
    {
        "question": "Multiple orders from different emails, same credit card, all shipping to different addresses in one day.",
        "options": ["A) Approve - Gift shopping", "B) Flag - Card testing pattern", "C) Approve - Holiday season", "D) Ask for ID"],
        "correct": 1,
        "explanation": "Classic card testing fraud pattern"
    },
    {
        "question": "Customer tries to buy 20 identical expensive items, expedited shipping, first-time buyer.",
        "options": ["A) Approve - Bulk discount", "B) Flag - Reseller activity", "C) Flag - Fraud pattern", "D) Approve - Business customer"],
        "correct": 2,
        "explanation": "First-time buyer + high quantity + rush = fraud risk"
    }
]

# Banking Risk Assessment for Tampa Level
BANKING_SCENARIOS = [
    {
        "question": "A transaction of $50,000 occurs at 3 AM from an ATM in a different state than usual. What's your assessment?",
        "options": ["A) Normal - People travel", "B) Low risk - Under $100k", "C) High risk - Time & location", "D) Medium risk - Check later"],
        "correct": 2,
        "explanation": "Unusual time, large amount, and location change = high fraud risk"
    },
    {
        "question": "System shows 15% higher transaction volume than normal. Server CPU at 85%. What's the priority action?",
        "options": ["A) Ignore - Weekend spike", "B) Scale resources immediately", "C) Monitor for 1 hour", "D) Restart servers"],
        "correct": 1,
        "explanation": "High load requires immediate scaling to prevent outages"
    },
    {
        "question": "Customer reports unauthorized charge but transaction shows correct PIN, location near home, normal amount.",
        "options": ["A) Deny claim - Valid transaction", "B) Investigate PIN compromise", "C) Full refund immediately", "D) Ask for police report"],
        "correct": 1,
        "explanation": "PIN usage doesn't eliminate fraud possibility - investigate thoroughly"
    },
    {
        "question": "Market volatility: stock down 15% in 1 hour. Your bank has $2M exposure. Action?",
        "options": ["A) Hold position - Markets recover", "B) Sell immediately - Cut losses", "C) Hedge position - Risk management", "D) Buy more - Opportunity"],
        "correct": 2,
        "explanation": "Risk management through hedging protects against further losses"
    },
    {
        "question": "New regulation requires customer data encryption upgrade by next month. Resources are limited.",
        "options": ["A) Request extension", "B) Prioritize over other projects", "C) Partial implementation", "D) Hire external contractors"],
        "correct": 1,
        "explanation": "Regulatory compliance is mandatory - prioritize to avoid penalties"
    }
]

# Machine Learning Scenarios for Healthcare Level
ML_SCENARIOS = [
    {
        "question": "Your insurance claim denial model has 85% accuracy but denies 60% of claims. What's the issue?",
        "options": ["A) Good accuracy is enough", "B) Model is too aggressive", "C) Need more data", "D) Retrain with different algorithm"],
        "correct": 1,
        "explanation": "High denial rate suggests model is biased against patients"
    },
    {
        "question": "Training data has 90% approved claims, 10% denied. Your model predicts 98% approvals. Problem?",
        "options": ["A) Excellent - High approval rate", "B) Class imbalance - Biased model", "C) Perfect - Matches data", "D) Need bigger dataset"],
        "correct": 1,
        "explanation": "Model learned data bias - need balanced training or resampling"
    },
    {
        "question": "Hospital wants to predict patient readmission risk. Which features are most important?",
        "options": ["A) Age, insurance type", "B) Previous admissions, severity", "C) Hospital staff preferences", "D) Patient zip code only"],
        "correct": 1,
        "explanation": "Medical history and severity are strongest predictors of readmission"
    },
    {
        "question": "Your model works great in testing but fails in production. Most likely cause?",
        "options": ["A) Data drift - Real data differs", "B) Server is too slow", "C) Model is perfect", "D) Need more RAM"],
        "correct": 0,
        "explanation": "Data drift - production data differs from training data over time"
    },
    {
        "question": "Ethics review: Your AI denies claims for expensive treatments. What's the priority?",
        "options": ["A) Maximize profit - Deny more", "B) Balance accuracy with fairness", "C) Always approve expensive treatments", "D) Remove expensive treatment data"],
        "correct": 1,
        "explanation": "Healthcare AI must balance cost with patient care and fairness"
    }
]

# Guitar Rhythm Challenges (Bonus Level)
GUITAR_CHALLENGES = [
    {
        "pattern": "AAAA",
        "name": "Basic Strum",
        "difficulty": "Easy"
    },
    {
        "pattern": "ABAB",
        "name": "Two Chord",
        "difficulty": "Easy"
    },
    {
        "pattern": "AABBAA",
        "name": "Rhythm Pattern",
        "difficulty": "Medium"
    },
    {
        "pattern": "ABCABC",
        "name": "Three Chord Progression",
        "difficulty": "Medium"
    },
    {
        "pattern": "ABCDABCD",
        "name": "Complex Progression",
        "difficulty": "Hard"
    }
]

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 35
        self.height = 35
        self.speed = 6
        self.health = 100
        self.max_health = 100
        self.experience = 0
        self.level = 1
        self.skills = []
        
    def move(self, dx, dy):
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed
        
        if 50 <= new_x <= SCREEN_WIDTH - self.width - 50:
            self.x = new_x
        if 50 <= new_y <= SCREEN_HEIGHT - self.height - 50:
            self.y = new_y
    
    def draw(self, screen):
        # Draw player as a professor (blue with graduation cap)
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
        # Graduation cap
        pygame.draw.rect(screen, BLACK, (self.x - 3, self.y - 5, self.width + 6, 8))
        # Health bar
        bar_width = 50
        bar_height = 6
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, RED, (self.x - 7, self.y - 20, bar_width, bar_height))
        pygame.draw.rect(screen, GREEN, (self.x - 7, self.y - 20, bar_width * health_ratio, bar_height))

class Enemy:
    def __init__(self, x, y, enemy_type="confusion", level_type="teaching"):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.speed = 1.2  # Slower for better balance
        self.health = 40
        self.max_health = 40
        self.type = enemy_type
        self.level_type = level_type
        self.last_damage_time = 0
        self.direction_change_timer = 0
        self.direction = random.uniform(0, 2 * math.pi)
        
    def update(self, player):
        # Different AI behavior based on enemy type
        if self.level_type == "teaching":
            # Confusion clouds drift around classroom slowly
            self.direction_change_timer += 1
            if self.direction_change_timer > 90:  # Change direction less frequently
                self.direction = random.uniform(0, 2 * math.pi)
                self.direction_change_timer = 0
            
            self.x += math.cos(self.direction) * self.speed * 0.5  # Much slower
            self.y += math.sin(self.direction) * self.speed * 0.5
            
        elif self.level_type == "database":
            # Data corruption bugs move more erratically (corrupted behavior)
            self.direction_change_timer += 1
            if self.direction_change_timer > 45:  # More frequent direction changes
                self.direction = random.uniform(0, 2 * math.pi)
                self.direction_change_timer = 0
            
            # Erratic movement pattern
            self.x += math.cos(self.direction) * self.speed * 0.7
            self.y += math.sin(self.direction) * self.speed * 0.7
            
        elif self.level_type == "fraud":
            # Fraudsters try to avoid being caught, move erratically
            dx = player.x - self.x
            dy = player.y - self.y
            distance = math.sqrt(dx*dx + dy*dy)
            if distance < 100:  # Run away if player gets close
                self.x -= (dx/distance) * self.speed * 1.2
                self.y -= (dy/distance) * self.speed * 1.2
            else:
                # Move randomly
                self.direction_change_timer += 1
                if self.direction_change_timer > 40:
                    self.direction = random.uniform(0, 2 * math.pi)
                    self.direction_change_timer = 0
                self.x += math.cos(self.direction) * self.speed
                self.y += math.sin(self.direction) * self.speed
                
        elif self.level_type == "banking":
            # Risk alerts move in patterns like financial data
            self.direction_change_timer += 1
            if self.direction_change_timer > 60:
                self.direction = random.uniform(0, 2 * math.pi)
                self.direction_change_timer = 0
            
            # Steady, deliberate movement like financial systems
            self.x += math.cos(self.direction) * self.speed * 0.6
            self.y += math.sin(self.direction) * self.speed * 0.6
            
        elif self.level_type == "healthcare":
            # Medical data patterns - predictable but complex
            self.direction_change_timer += 1
            if self.direction_change_timer > 75:
                self.direction = random.uniform(0, 2 * math.pi)
                self.direction_change_timer = 0
            
            # Smooth, medical-like movement
            self.x += math.cos(self.direction) * self.speed * 0.5
            self.y += math.sin(self.direction) * self.speed * 0.5
        
        # Keep enemies on screen
        self.x = max(50, min(SCREEN_WIDTH - 50, self.x))
        self.y = max(50, min(SCREEN_HEIGHT - 50, self.y))
    
    def draw(self, screen):
        # Different colors and shapes for different enemy types
        if self.type == "confusion":
            color = PURPLE
            pygame.draw.ellipse(screen, color, (self.x, self.y, self.width, self.height))  # Cloud-like
            # Add question mark on confusion cloud
            font = pygame.font.Font(None, 24)
            question_text = font.render("?", True, WHITE)
            text_rect = question_text.get_rect(center=(self.x + self.width//2, self.y + self.height//2))
            screen.blit(question_text, text_rect)
        elif self.type == "data_bug":
            color = RED
            pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
            # Add database symbol
            font = pygame.font.Font(None, 20)
            db_text = font.render("DB", True, WHITE)
            text_rect = db_text.get_rect(center=(self.x + self.width//2, self.y + self.height//2))
            screen.blit(db_text, text_rect)
        elif self.type == "fraudster":
            color = MAROON
            pygame.draw.polygon(screen, color, [(self.x + self.width//2, self.y), 
                                              (self.x, self.y + self.height),
                                              (self.x + self.width, self.y + self.height)])
            # Add dollar sign
            font = pygame.font.Font(None, 20)
            fraud_text = font.render("$", True, WHITE)
            text_rect = fraud_text.get_rect(center=(self.x + self.width//2, self.y + self.height//2 + 5))
            screen.blit(fraud_text, text_rect)
        elif self.type == "risk_alert":
            color = NAVY
            pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
            # Add risk symbol
            font = pygame.font.Font(None, 18)
            risk_text = font.render("!", True, WHITE)
            text_rect = risk_text.get_rect(center=(self.x + self.width//2, self.y + self.height//2))
            screen.blit(risk_text, text_rect)
        elif self.type == "medical_data":
            color = TEAL
            pygame.draw.ellipse(screen, color, (self.x, self.y, self.width, self.height))
            # Add medical symbol
            font = pygame.font.Font(None, 18)
            med_text = font.render("+", True, WHITE)
            text_rect = med_text.get_rect(center=(self.x + self.width//2, self.y + self.height//2))
            screen.blit(med_text, text_rect)
        
        # Health bar (only for action-based enemies)
        if self.type in ["risk_alert", "medical_data"]:  # Only banking and healthcare levels have health bars
            bar_width = 35
            bar_height = 4
            health_ratio = self.health / self.max_health
            pygame.draw.rect(screen, RED, (self.x - 2, self.y - 10, bar_width, bar_height))
            pygame.draw.rect(screen, GREEN, (self.x - 2, self.y - 10, bar_width * health_ratio, bar_height))

class QuizScreen:
    def __init__(self):
        self.font_large = pygame.font.Font(None, 36)
        self.font_medium = pygame.font.Font(None, 28)
        self.font_small = pygame.font.Font(None, 24)
        self.current_question = None
        self.selected_answer = None
        self.question_type = "economics"  # economics, database, fraud, banking, healthcare
        
    def show_question(self, question_data, question_type="economics"):
        self.current_question = question_data
        self.selected_answer = None
        self.question_type = question_type
        
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.selected_answer = 0
                return True
            elif event.key == pygame.K_2:
                self.selected_answer = 1
                return True
            elif event.key == pygame.K_3:
                self.selected_answer = 2
                return True
            elif event.key == pygame.K_4:
                self.selected_answer = 3
                return True
        return False
        
    def draw(self, screen):
        if not self.current_question:
            return
            
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # Quiz box with different colors based on type
        box_width = 750
        box_height = 450
        box_x = (SCREEN_WIDTH - box_width) // 2
        box_y = (SCREEN_HEIGHT - box_height) // 2
        
        pygame.draw.rect(screen, WHITE, (box_x, box_y, box_width, box_height))
        
        # Different border colors for different question types
        if self.question_type == "economics":
            border_color = DARK_RED
            header_text = "ECONOMICS QUESTION"
        elif self.question_type == "database":
            border_color = DARK_BLUE
            header_text = "DATABASE REPAIR"
        elif self.question_type == "fraud":
            border_color = MAROON
            header_text = "FRAUD ANALYSIS"
        elif self.question_type == "banking":
            border_color = NAVY
            header_text = "BANKING RISK ASSESSMENT"
        elif self.question_type == "healthcare":
            border_color = TEAL
            header_text = "HEALTHCARE ML DECISION"
        else:
            border_color = BLACK
            header_text = "QUESTION"
        
        pygame.draw.rect(screen, border_color, (box_x, box_y, box_width, box_height), 3)
        
        # Header
        header_surface = self.font_medium.render(header_text, True, border_color)
        header_rect = header_surface.get_rect(center=(SCREEN_WIDTH//2, box_y + 25))
        screen.blit(header_surface, header_rect)
        
        # Question
        question_lines = self.wrap_text(self.current_question["question"], 70)
        y_offset = box_y + 60
        for line in question_lines:
            question_surface = self.font_medium.render(line, True, BLACK)
            question_rect = question_surface.get_rect(center=(SCREEN_WIDTH//2, y_offset))
            screen.blit(question_surface, question_rect)
            y_offset += 35
            
        # Options
        y_offset += 20
        for i, option in enumerate(self.current_question["options"]):
            color = BLUE if self.selected_answer == i else BLACK
            option_surface = self.font_small.render(f"{i+1}) {option}", True, color)
            option_rect = option_surface.get_rect(center=(SCREEN_WIDTH//2, y_offset))
            screen.blit(option_surface, option_rect)
            y_offset += 30
            
        # Instructions
        if self.selected_answer is None:
            inst_text = "Press 1, 2, 3, or 4 to select your answer"
            inst_surface = self.font_small.render(inst_text, True, DARK_BLUE)
            inst_rect = inst_surface.get_rect(center=(SCREEN_WIDTH//2, box_y + box_height - 40))
            screen.blit(inst_surface, inst_rect)
    
    def wrap_text(self, text, max_chars):
        words = text.split()
        lines = []
        current_line = ""
        
        for word in words:
            if len(current_line + " " + word) <= max_chars:
                current_line += (" " + word) if current_line else word
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        return lines

class RhythmGame:
    def __init__(self):
        self.current_pattern = []
        self.player_input = []
        self.pattern_index = 0
        self.score = 0
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 32)
        self.challenge = None
        self.game_active = False
        self.success = False
        
    def start_challenge(self, challenge):
        self.challenge = challenge
        self.current_pattern = list(challenge["pattern"])
        self.player_input = []
        self.pattern_index = 0
        self.game_active = True
        self.success = False
        
    def handle_input(self, event):
        if not self.game_active:
            return False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.player_input.append('A')
                return self.check_progress()
            elif event.key == pygame.K_b:
                self.player_input.append('B')
                return self.check_progress()
            elif event.key == pygame.K_c:
                self.player_input.append('C')
                return self.check_progress()
            elif event.key == pygame.K_d:
                self.player_input.append('D')
                return self.check_progress()
        return False
        
    def check_progress(self):
        if len(self.player_input) > len(self.current_pattern):
            self.game_active = False
            return True
            
        # Check if current input matches pattern so far
        for i, note in enumerate(self.player_input):
            if note != self.current_pattern[i]:
                self.game_active = False
                return True
                
        # Check if pattern is complete
        if len(self.player_input) == len(self.current_pattern):
            self.success = True
            self.game_active = False
            return True
            
        return False
        
    def draw(self, screen):
        if not self.challenge:
            return
            
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # Guitar game box
        box_width = 600
        box_height = 400
        box_x = (SCREEN_WIDTH - box_width) // 2
        box_y = (SCREEN_HEIGHT - box_height) // 2
        
        pygame.draw.rect(screen, WHITE, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, ORANGE, (box_x, box_y, box_width, box_height), 3)
        
        # Header
        header_text = f"LiberLive C1 Guitar Challenge: {self.challenge['name']}"
        header_surface = self.small_font.render(header_text, True, ORANGE)
        header_rect = header_surface.get_rect(center=(SCREEN_WIDTH//2, box_y + 30))
        screen.blit(header_surface, header_rect)
        
        # Pattern display
        pattern_text = f"Pattern: {self.challenge['pattern']}"
        pattern_surface = self.font.render(pattern_text, True, BLACK)
        pattern_rect = pattern_surface.get_rect(center=(SCREEN_WIDTH//2, box_y + 80))
        screen.blit(pattern_surface, pattern_rect)
        
        # Player input
        input_text = f"Your input: {''.join(self.player_input)}"
        input_surface = self.font.render(input_text, True, BLUE)
        input_rect = input_surface.get_rect(center=(SCREEN_WIDTH//2, box_y + 130))
        screen.blit(input_surface, input_rect)
        
        # Progress indicator
        progress = len(self.player_input) / len(self.current_pattern) if self.current_pattern else 0
        bar_width = 400
        bar_height = 20
        bar_x = (SCREEN_WIDTH - bar_width) // 2
        bar_y = box_y + 180
        pygame.draw.rect(screen, GRAY, (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, bar_width * progress, bar_height))
        
        # Instructions
        if self.game_active:
            inst1 = "Play the pattern using A, B, C, D keys"
            inst2 = f"Difficulty: {self.challenge['difficulty']}"
        elif self.success:
            inst1 = "Perfect! You've mastered the LiberLive C1!"
            inst2 = "The family gatherings will love this!"
        else:
            inst1 = "Oops! Try again to master the smart guitar"
            inst2 = "Even tech-savvy musicians need practice!"
            
        inst1_surface = self.small_font.render(inst1, True, BLACK)
        inst1_rect = inst1_surface.get_rect(center=(SCREEN_WIDTH//2, box_y + 230))
        screen.blit(inst1_surface, inst1_rect)
        
        inst2_surface = self.small_font.render(inst2, True, DARK_GREEN)
        inst2_rect = inst2_surface.get_rect(center=(SCREEN_WIDTH//2, box_y + 260))
        screen.blit(inst2_surface, inst2_rect)

class GameLevel:
    def __init__(self, level_num, name, location, year, description, objective, enemy_type, enemy_name, gameplay_type="action", path_coords=(0,0)):
        self.level_num = level_num
        self.name = name
        self.location = location
        self.year = year
        self.description = description
        self.objective = objective
        self.enemy_type = enemy_type
        self.enemy_name = enemy_name
        self.gameplay_type = gameplay_type  # "quiz", "action", "rhythm"
        self.enemies_to_defeat = 3  # Reduced to 3 per level!
        self.path_coords = path_coords  # (x, y) coordinates for bicycle path

# Define all career levels with thematic gameplay and bicycle path coordinates
LEVELS = [
    GameLevel(1, "The Teaching Trials", "Beijing University, China", "2009-2011",
              "Fresh out of graduate school, you're teaching Economics 101 to Chinese students.\nAnswer economics questions to clear up confusion in the classroom.",
              "Answer 3 economics questions correctly to clear confusion clouds",
              "confusion", "Confusion Clouds", "quiz", (150, 500)),
              
    GameLevel(2, "Database Debugging", "Minneapolis, Minnesota", "2011-2013", 
              "Working at Metropolitan State University developing student information systems.\nFix corrupted database entries by solving SQL and data management problems.",
              "Repair 3 corrupted database entries with your SQL knowledge",
              "data_bug", "Database Corruption Bugs", "quiz", (300, 350)),
              
    GameLevel(3, "Fraud Fighter", "Minneapolis, Minnesota", "2013-2014",
              "At Digital River, you're analyzing e-commerce transactions to prevent fraud.\nAnalyze suspicious transactions and identify fraudulent patterns.",
              "Correctly analyze 3 suspicious e-commerce transactions",
              "fraudster", "Suspicious Transactions", "quiz", (450, 300)),
              
    GameLevel(4, "Financial Fortress", "Tampa, Florida", "2014-2017",
              "Working at major banks (JPMorgan Chase & Citi) on enterprise systems.\nAssess financial risks and make critical banking decisions under pressure.",
              "Successfully handle 3 critical banking risk scenarios",
              "risk_alert", "Risk Alerts", "quiz", (650, 350)),
              
    GameLevel(5, "Healthcare Hero", "Lakeland, Florida", "2017",
              "At Lakeland Regional Health, building machine learning models.\nMake ML decisions to predict insurance claims and help patients get better care.",
              "Solve 3 machine learning model challenges for patient care",
              "medical_data", "ML Model Challenges", "quiz", (750, 400)),
              
    GameLevel(6, "Smart Guitar Mastery", "Family Gatherings Everywhere", "2024",
              "Master the LiberLive C1 smart guitar! This high-tech, foldable instrument\nhas become a hit at family gatherings. Show off your tech-savvy musical skills!",
              "Complete 3 rhythm challenges on the smart guitar",
              "guitar_note", "Musical Notes", "rhythm", (850, 450))
]

class BicycleJourneyMap:
    def __init__(self, current_level):
        self.current_level = current_level
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        
    def draw_flag(self, screen, x, y, country):
        """Draw simple country flags"""
        flag_width = 40
        flag_height = 25
        
        if country == "china":
            # Chinese flag - red with yellow star
            pygame.draw.rect(screen, RED, (x, y, flag_width, flag_height))
            pygame.draw.circle(screen, GOLD, (x + 10, y + 8), 4)
        elif country == "usa":
            # USA flag - simplified stripes
            pygame.draw.rect(screen, RED, (x, y, flag_width, flag_height))
            for i in range(0, flag_height, 4):
                if i % 8 == 0:
                    pygame.draw.rect(screen, WHITE, (x, y + i, flag_width, 2))
            # Blue corner
            pygame.draw.rect(screen, DARK_BLUE, (x, y, flag_width//2, flag_height//2))
        
        # Flag pole
        pygame.draw.line(screen, BROWN, (x, y), (x, y + flag_height + 15), 3)
        
    def draw(self, screen):
        # Sky blue background
        screen.fill((135, 206, 235))
        
        # Title
        title_text = "Career Journey by Bicycle 🚴"
        title_surface = self.font_large.render(title_text, True, DARK_BLUE)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH//2, 50))
        screen.blit(title_surface, title_rect)
        
        # Subtitle
        subtitle_text = "Following the path of academic adventure"
        subtitle_surface = self.font_medium.render(subtitle_text, True, DARK_GREEN)
        subtitle_rect = subtitle_surface.get_rect(center=(SCREEN_WIDTH//2, 85))
        screen.blit(subtitle_surface, subtitle_rect)
        
        # Draw the winding bicycle path
        path_points = []
        for level in LEVELS:
            path_points.append(level.path_coords)
        
        # Draw path segments
        for i in range(len(path_points) - 1):
            # Curved path between points
            start = path_points[i]
            end = path_points[i + 1]
            
            # Draw path segments with multiple lines for width
            for offset in [-6, -3, 0, 3, 6]:
                start_offset = (start[0], start[1] + offset)
                end_offset = (end[0], end[1] + offset)
                
                if i <= self.current_level:
                    color = BROWN  # Traveled path
                else:
                    color = LIGHT_GRAY  # Future path
                    
                pygame.draw.line(screen, color, start_offset, end_offset, 2)
        
        # Draw country flags and regions
        self.draw_flag(screen, 100, 150, "china")
        china_label = self.font_small.render("CHINA", True, BLACK)
        screen.blit(china_label, (75, 200))
        
        self.draw_flag(screen, 400, 120, "usa")
        usa_label = self.font_small.render("UNITED STATES", True, BLACK)
        screen.blit(usa_label, (380, 170))
        
        # Draw stops for each level
        for i, level in enumerate(LEVELS):
            x, y = level.path_coords
            
            # Determine stop color based on progress
            if i < self.current_level:
                stop_color = GREEN  # Completed
                text_color = BLACK
            elif i == self.current_level:
                stop_color = YELLOW  # Current
                text_color = BLACK
            else:
                stop_color = LIGHT_GRAY  # Future
                text_color = GRAY
            
            # Draw stop circle
            pygame.draw.circle(screen, stop_color, (x, y), 20)
            pygame.draw.circle(screen, BLACK, (x, y), 20, 3)
            
            # Level number
            level_num = self.font_medium.render(str(level.level_num), True, text_color)
            level_rect = level_num.get_rect(center=(x, y))
            screen.blit(level_num, level_rect)
            
            # Location name (shortened)
            if "China" in level.location:
                location_short = "Beijing"
            elif "Minnesota" in level.location:
                location_short = "Minneapolis" if "Database" in level.name else "Digital River"
            elif "Tampa" in level.location:
                location_short = "Tampa"
            elif "Lakeland" in level.location:
                location_short = "Lakeland"
            else:
                location_short = "Musical"
            
            location_surface = self.font_small.render(location_short, True, text_color)
            location_rect = location_surface.get_rect(center=(x, y + 35))
            screen.blit(location_surface, location_rect)
            
            # Year
            year_surface = self.font_small.render(level.year.split('-')[0], True, text_color)
            year_rect = year_surface.get_rect(center=(x, y - 35))
            screen.blit(year_surface, year_rect)
        
        # Current cyclist position (bicycle emoji substitute)
        if self.current_level < len(LEVELS):
            cyclist_x, cyclist_y = LEVELS[self.current_level].path_coords
            # Draw simple bicycle
            pygame.draw.circle(screen, BLACK, (cyclist_x - 25, cyclist_y + 10), 8, 2)  # Wheel
            pygame.draw.circle(screen, BLACK, (cyclist_x - 5, cyclist_y + 10), 8, 2)   # Wheel
            pygame.draw.line(screen, BLACK, (cyclist_x - 25, cyclist_y + 10), (cyclist_x - 15, cyclist_y), 2)  # Frame
            pygame.draw.line(screen, BLACK, (cyclist_x - 15, cyclist_y), (cyclist_x - 5, cyclist_y + 10), 2)   # Frame
            # Cyclist (simple figure)
            pygame.draw.circle(screen, BLUE, (cyclist_x - 15, cyclist_y - 10), 5)  # Head
            pygame.draw.line(screen, BLUE, (cyclist_x - 15, cyclist_y - 5), (cyclist_x - 15, cyclist_y + 5), 3)  # Body
        
        # Current level info
        if self.current_level < len(LEVELS):
            current = LEVELS[self.current_level]
            current_text = f"Next Stop: {current.name}"
            current_surface = self.font_medium.render(current_text, True, RED)
            current_rect = current_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 120))
            screen.blit(current_surface, current_rect)
        
        # Legend
        legend_y = SCREEN_HEIGHT - 80
        pygame.draw.circle(screen, GREEN, (50, legend_y), 12)
        legend1 = self.font_small.render("Completed", True, BLACK)
        screen.blit(legend1, (70, legend_y - 8))
        
        pygame.draw.circle(screen, YELLOW, (200, legend_y), 12)
        legend2 = self.font_small.render("Current", True, BLACK)
        screen.blit(legend2, (220, legend_y - 8))
        
        pygame.draw.circle(screen, LIGHT_GRAY, (320, legend_y), 12)
        legend3 = self.font_small.render("Future", True, BLACK)
        screen.blit(legend3, (340, legend_y - 8))
        
        # Instructions
        inst_text = "Press SPACE to continue your cycling adventure!"
        inst_surface = self.font_medium.render(inst_text, True, DARK_BLUE)
        inst_rect = inst_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 40))
        screen.blit(inst_surface, inst_rect)

class IntroScreen:
    def __init__(self, level_info):
        self.level_info = level_info
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 28)
        
    def draw(self, screen):
        screen.fill(LIGHT_GRAY)
        
        # Title
        title = f"Level {self.level_info.level_num}: {self.level_info.name}"
        title_text = self.font_large.render(title, True, DARK_BLUE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, 80))
        screen.blit(title_text, title_rect)
        
        # Location and Year
        location_text = f"{self.level_info.location} ({self.level_info.year})"
        location_surface = self.font_medium.render(location_text, True, DARK_GREEN)
        location_rect = location_surface.get_rect(center=(SCREEN_WIDTH//2, 130))
        screen.blit(location_surface, location_rect)
        
        # Description
        y_offset = 200
        description_lines = self.level_info.description.split('\n')
        for line in description_lines:
            desc_surface = self.font_small.render(line, True, BLACK)
            desc_rect = desc_surface.get_rect(center=(SCREEN_WIDTH//2, y_offset))
            screen.blit(desc_surface, desc_rect)
            y_offset += 35
        
        # Objective
        y_offset += 30
        obj_title = self.font_medium.render("OBJECTIVE:", True, RED)
        obj_title_rect = obj_title.get_rect(center=(SCREEN_WIDTH//2, y_offset))
        screen.blit(obj_title, obj_title_rect)
        
        y_offset += 40
        obj_surface = self.font_small.render(self.level_info.objective, True, MAROON)
        obj_rect = obj_surface.get_rect(center=(SCREEN_WIDTH//2, y_offset))
        screen.blit(obj_surface, obj_rect)
        
        # Controls
        y_offset += 80
        controls_title = self.font_medium.render("CONTROLS:", True, BLUE)
        controls_rect = controls_title.get_rect(center=(SCREEN_WIDTH//2, y_offset))
        screen.blit(controls_title, controls_rect)
        
        if self.level_info.gameplay_type == "quiz":
            controls = [
                "WASD or Arrow Keys - Move Professor",
                f"Walk into {self.level_info.enemy_name.lower()} to get questions",
                "Answer correctly to solve problems (wrong answers hurt!)"
            ]
        elif self.level_info.gameplay_type == "rhythm":
            controls = [
                "WASD or Arrow Keys - Move Professor",
                "Walk into musical notes to start rhythm challenges",
                "Use A, B, C, D keys to play guitar patterns"
            ]
        else:
            controls = [
                "WASD or Arrow Keys - Move Professor",
                "Walk into enemies to solve problems",
                "Don't let your health reach zero!"
            ]
        
        y_offset += 35
        for control in controls:
            control_surface = self.font_small.render(control, True, BLACK)
            control_rect = control_surface.get_rect(center=(SCREEN_WIDTH//2, y_offset))
            screen.blit(control_surface, control_rect)
            y_offset += 30
        
        # Start instruction
        start_text = "Press SPACE to begin this chapter of the career journey!"
        start_surface = self.font_medium.render(start_text, True, DARK_BLUE)
        start_rect = start_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 80))
        screen.blit(start_surface, start_rect)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Professor's Quest: A Career Adventure")
        self.clock = pygame.time.Clock()
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.enemies = []
        self.enemy_spawn_timer = 0
        self.current_level = 0
        self.enemies_defeated = 0
        self.font = pygame.font.Font(None, 32)
        self.small_font = pygame.font.Font(None, 24)
        self.game_state = "map"  # map, intro, playing, quiz, rhythm, level_complete, game_over
        self.map_screen = BicycleJourneyMap(self.current_level)
        self.intro_screen = IntroScreen(LEVELS[self.current_level])
        self.quiz_screen = QuizScreen()
        self.rhythm_game = RhythmGame()
        self.quiz_enemy = None
        self.result_timer = 0
        self.result_message = ""
        
    def spawn_enemy(self):
        level_info = LEVELS[self.current_level]
        side = random.randint(0, 3)
        if side == 0:  # Top
            x, y = random.randint(100, SCREEN_WIDTH-100), 50
        elif side == 1:  # Right
            x, y = SCREEN_WIDTH-50, random.randint(100, SCREEN_HEIGHT-100)
        elif side == 2:  # Bottom
            x, y = random.randint(100, SCREEN_WIDTH-100), SCREEN_HEIGHT-50
        else:  # Left
            x, y = 50, random.randint(100, SCREEN_HEIGHT-100)
            
        enemy_type = level_info.enemy_type
        level_type = ["teaching", "database", "fraud", "banking", "healthcare", "rhythm"][self.current_level]
        self.enemies.append(Enemy(x, y, enemy_type, level_type))
    
    def handle_combat(self):
        current_time = pygame.time.get_ticks()
        
        for enemy in self.enemies[:]:
            if (abs(self.player.x - enemy.x) < 40 and 
                abs(self.player.y - enemy.y) < 40):
                
                level_info = LEVELS[self.current_level]
                
                if level_info.gameplay_type == "quiz":
                    # Quiz-based levels
                    if self.current_level == 0:  # Economics
                        question = random.choice(ECON_QUESTIONS)
                        self.quiz_screen.show_question(question, "economics")
                    elif self.current_level == 1:  # Database
                        question = random.choice(DATABASE_QUESTIONS)
                        self.quiz_screen.show_question(question, "database")
                    elif self.current_level == 2:  # Fraud
                        question = random.choice(FRAUD_SCENARIOS)
                        self.quiz_screen.show_question(question, "fraud")
                    elif self.current_level == 3:  # Banking
                        question = random.choice(BANKING_SCENARIOS)
                        self.quiz_screen.show_question(question, "banking")
                    elif self.current_level == 4:  # Healthcare
                        question = random.choice(ML_SCENARIOS)
                        self.quiz_screen.show_question(question, "healthcare")
                    
                    self.quiz_enemy = enemy
                    self.game_state = "quiz"
                    return
                elif level_info.gameplay_type == "rhythm":
                    # Rhythm game for guitar level
                    challenge = random.choice(GUITAR_CHALLENGES)
                    self.rhythm_game.start_challenge(challenge)
                    self.quiz_enemy = enemy
                    self.game_state = "rhythm"
                    return
                else:
                    # Action-based levels (if any remain)
                    if current_time - enemy.last_damage_time > 800:
                        self.player.health -= 8
                        enemy.last_damage_time = current_time
                    
                    enemy.health -= 20
                    
                    if enemy.health <= 0:
                        self.enemies.remove(enemy)
                        self.enemies_defeated += 1
                        self.player.experience += 15
    
    def handle_quiz_result(self, correct):
        if correct:
            self.enemies.remove(self.quiz_enemy)
            self.enemies_defeated += 1
            self.player.experience += 20
            
            # Different success messages based on level
            messages = [
                "Correct! Confusion cleared!",
                "Database repaired successfully!",
                "Fraudulent transaction blocked!",
                "Risk properly assessed!",
                "ML model decision validated!"
            ]
            self.result_message = messages[min(self.current_level, len(messages)-1)]
        else:
            self.player.health -= 15
            
            # Different failure messages based on level
            fail_messages = [
                "Wrong answer! Confusion persists...",
                "Database corruption worsened!",
                "Fraud went undetected!",
                "Poor risk assessment!",
                "ML model failed validation!"
            ]
            self.result_message = fail_messages[min(self.current_level, len(fail_messages)-1)]
        
        self.result_timer = pygame.time.get_ticks()
        self.quiz_enemy = None
        self.game_state = "playing"
    
    def handle_rhythm_result(self, success):
        if success:
            self.enemies.remove(self.quiz_enemy)
            self.enemies_defeated += 1
            self.player.experience += 25
            self.result_message = "Perfect! Guitar mastery achieved!"
        else:
            self.player.health -= 10
            self.result_message = "Musical mishap! Practice makes perfect..."
        
        self.result_timer = pygame.time.get_ticks()
        self.quiz_enemy = None
        self.game_state = "playing"
    
    def draw_level_background(self):
        level_info = LEVELS[self.current_level]
        
        # Different backgrounds for different levels
        if self.current_level == 0:  # Beijing University - Enhanced Chinese authenticity
            # Traditional Chinese colors - red and gold theme
            self.screen.fill((248, 248, 240))  # Warm ivory background
            
            # Traditional Chinese decorative border
            pygame.draw.rect(self.screen, DARK_RED, (20, 20, SCREEN_WIDTH-40, SCREEN_HEIGHT-40), 5)
            pygame.draw.rect(self.screen, GOLD, (25, 25, SCREEN_WIDTH-50, SCREEN_HEIGHT-50), 2)
            
            # Professor's podium (more ornate)
            pygame.draw.rect(self.screen, BROWN, (80, 140, 140, 100))  # Main podium
            pygame.draw.rect(self.screen, GOLD, (85, 145, 130, 90), 2)  # Gold trim
            
            # Large blackboard with Chinese characters
            pygame.draw.rect(self.screen, BLACK, (250, 100, 250, 120))
            pygame.draw.rect(self.screen, BROWN, (245, 95, 260, 130), 3)  # Frame
            
            # Chinese characters on blackboard (Economics in Chinese: 经济学)
            font_chinese = pygame.font.Font(None, 48)
            chinese_text = font_chinese.render("经济学", True, WHITE)
            self.screen.blit(chinese_text, (320, 130))
            
            # Economics equations on blackboard
            eq_font = pygame.font.Font(None, 24)
            eq1 = eq_font.render("Supply = Demand", True, WHITE)
            eq2 = eq_font.render("Utility Max", True, WHITE)
            self.screen.blit(eq1, (260, 170))
            self.screen.blit(eq2, (260, 190))
            
            # Traditional Chinese student desks (more rows, smaller desks)
            for i in range(5):  # 5 columns
                for j in range(6):  # 6 rows
                    desk_x = 520 + i*80
                    desk_y = 180 + j*70
                    if desk_x < SCREEN_WIDTH - 100 and desk_y < SCREEN_HEIGHT - 100:
                        # Desk
                        pygame.draw.rect(self.screen, BROWN, (desk_x, desk_y, 50, 30))
                        # Chair
                        pygame.draw.rect(self.screen, BROWN, (desk_x + 10, desk_y + 35, 30, 15))
            
            # Chinese lanterns (decorative)
            pygame.draw.circle(self.screen, RED, (150, 80), 20)
            pygame.draw.circle(self.screen, GOLD, (150, 80), 18, 2)
            pygame.draw.circle(self.screen, RED, (SCREEN_WIDTH-150, 80), 20)
            pygame.draw.circle(self.screen, GOLD, (SCREEN_WIDTH-150, 80), 18, 2)
            
            # Bamboo decorative elements
            for x in [60, SCREEN_WIDTH-60]:
                for y in range(250, 600, 30):
                    pygame.draw.rect(self.screen, DARK_GREEN, (x-3, y, 6, 25))
                    pygame.draw.circle(self.screen, DARK_GREEN, (x, y), 4)
            
            # Easter egg: Bicycle (cycling hobby)
            pygame.draw.circle(self.screen, BLACK, (50, 600), 15, 2)  # Wheel
            pygame.draw.circle(self.screen, BLACK, (100, 600), 15, 2)  # Wheel
            pygame.draw.line(self.screen, BLACK, (50, 600), (75, 580), 3)  # Frame
            pygame.draw.line(self.screen, BLACK, (75, 580), (100, 600), 3)  # Frame
            
        elif self.current_level == 1:  # Minneapolis Database - Enhanced tech environment
            self.screen.fill((240, 240, 250))  # Slight blue tint for tech
            
            # Server room with more detail
            for i in range(6):
                server_x = 80 + i*140
                pygame.draw.rect(self.screen, GRAY, (server_x, 100, 80, 400))  # Server rack
                pygame.draw.rect(self.screen, BLACK, (server_x, 90, 80, 20))  # Top
                
                # Multiple status lights per server
                for j in range(8):
                    light_y = 120 + j*40
                    if j % 3 == 0:
                        pygame.draw.circle(self.screen, GREEN, (server_x + 20, light_y), 4)  # OK
                    elif j % 3 == 1:
                        pygame.draw.circle(self.screen, YELLOW, (server_x + 40, light_y), 4)  # Warning
                    else:
                        pygame.draw.circle(self.screen, RED, (server_x + 60, light_y), 4)  # Error
                
                # Cable management
                pygame.draw.rect(self.screen, BLACK, (server_x - 5, 500, 90, 10))
            
            # Network monitoring screens
            for i in range(3):
                screen_x = 200 + i*200
                pygame.draw.rect(self.screen, BLACK, (screen_x, 520, 120, 80))
                pygame.draw.rect(self.screen, GREEN, (screen_x + 10, 530, 100, 60))
                
                # Fake network data
                font = pygame.font.Font(None, 16)
                data_text = font.render("DB STATUS", True, BLACK)
                self.screen.blit(data_text, (screen_x + 20, 540))
                
        elif self.current_level == 2:  # Digital River Fraud - Enhanced office
            self.screen.fill((255, 250, 240))  # Warm office
            
            # Multiple workstations with transaction data
            for i in range(4):
                for j in range(2):
                    desk_x = 150 + i*180
                    desk_y = 200 + j*150
                    if desk_x < SCREEN_WIDTH - 120:
                        # Desk
                        pygame.draw.rect(self.screen, BROWN, (desk_x, desk_y, 120, 60))
                        # Monitor
                        pygame.draw.rect(self.screen, BLACK, (desk_x + 10, desk_y - 40, 100, 60))
                        pygame.draw.rect(self.screen, WHITE, (desk_x + 15, desk_y - 35, 90, 50))
                        
                        # Transaction data on screen
                        font = pygame.font.Font(None, 14)
                        trans_text = font.render("$$$", True, RED)
                        self.screen.blit(trans_text, (desk_x + 35, desk_y - 20))
            
            # Fraud alerts board
            pygame.draw.rect(self.screen, RED, (50, 100, 200, 150))
            pygame.draw.rect(self.screen, WHITE, (60, 110, 180, 130))
            alert_font = pygame.font.Font(None, 24)
            alert_text = alert_font.render("FRAUD ALERTS", True, RED)
            self.screen.blit(alert_text, (90, 130))
            
        elif self.current_level == 3:  # Tampa Banking - Enhanced financial environment
            self.screen.fill((248, 248, 255))  # Professional blue-white
            
            # Banking infrastructure
            pygame.draw.rect(self.screen, DARK_BLUE, (150, 100, 300, 200))  # Main server
            pygame.draw.rect(self.screen, WHITE, (160, 110, 280, 180))
            
            # Financial data displays
            font = pygame.font.Font(None, 20)
            for i in range(6):
                y_pos = 130 + i*25
                data_text = font.render(f"Account ${random.randint(1000, 9999)}: ${random.randint(10000, 999999)}", True, BLACK)
                self.screen.blit(data_text, (170, y_pos))
            
            # ATM systems
            pygame.draw.rect(self.screen, YELLOW, (500, 150, 200, 100))
            pygame.draw.rect(self.screen, GREEN, (510, 160, 180, 80))
            atm_font = pygame.font.Font(None, 24)
            atm_text = atm_font.render("ATM NETWORK", True, BLACK)
            self.screen.blit(atm_text, (540, 185))
            
            # Risk monitoring dashboard
            pygame.draw.rect(self.screen, RED, (150, 320, 300, 100))
            pygame.draw.rect(self.screen, WHITE, (160, 330, 280, 80))
            risk_text = font.render("RISK MONITORING ACTIVE", True, RED)
            self.screen.blit(risk_text, (200, 360))
            
        elif self.current_level == 4:  # Healthcare - Enhanced medical environment
            self.screen.fill((255, 255, 248))  # Hospital white
            
            # Medical equipment
            pygame.draw.rect(self.screen, WHITE, (200, 200, 100, 150))  # Hospital bed
            pygame.draw.rect(self.screen, BLACK, (190, 190, 120, 10))  # Bed frame
            
            # Medical monitors
            pygame.draw.rect(self.screen, GREEN, (350, 180, 120, 100))
            pygame.draw.rect(self.screen, BLACK, (360, 190, 100, 80))
            
            # Heartbeat line simulation
            font = pygame.font.Font(None, 16)
            vitals_text = font.render("♡ 72 BPM", True, GREEN)
            self.screen.blit(vitals_text, (370, 200))
            
            # ML Model dashboard
            pygame.draw.rect(self.screen, BLUE, (500, 200, 200, 150))
            pygame.draw.rect(self.screen, WHITE, (510, 210, 180, 130))
            ml_font = pygame.font.Font(None, 18)
            ml_text = ml_font.render("ML PREDICTION MODEL", True, BLUE)
            self.screen.blit(ml_text, (530, 220))
            
            accuracy_text = font.render("Accuracy: 94.2%", True, BLACK)
            self.screen.blit(accuracy_text, (520, 250))
            
            claims_text = font.render("Claims Processed: 1,247", True, BLACK)
            self.screen.blit(claims_text, (520, 270))
            
            # Easter egg: Basketball hoop (basketball hobby)
            pygame.draw.rect(self.screen, ORANGE, (800, 80, 150, 10))  # Backboard
            pygame.draw.circle(self.screen, ORANGE, (875, 120), 25, 3)  # Hoop
            pygame.draw.circle(self.screen, BROWN, (875, 160), 8)  # Basketball
            
        elif self.current_level == 5:  # Guitar Level - Musical environment
            self.screen.fill((255, 248, 220))  # Warm musical background
            
            # Stage setup
            pygame.draw.rect(self.screen, BROWN, (100, 400, 800, 200))  # Stage
            pygame.draw.rect(self.screen, GOLD, (100, 400, 800, 10))  # Stage edge
            
            # Musical notes floating around
            notes = ['♪', '♫', '♬', '♩']
            font = pygame.font.Font(None, 48)
            for i in range(20):
                x = random.randint(50, SCREEN_WIDTH-50)
                y = random.randint(50, 350)
                note = random.choice(notes)
                note_surface = font.render(note, True, PURPLE)
                self.screen.blit(note_surface, (x, y))
            
            # LiberLive C1 Guitar display
            pygame.draw.rect(self.screen, BLACK, (400, 450, 200, 80))  # Guitar body
            pygame.draw.rect(self.screen, BROWN, (405, 455, 190, 70))  # Guitar face
            
            # Guitar strings
            for i in range(6):
                y_pos = 465 + i*10
                pygame.draw.line(self.screen, WHITE, (410, y_pos), (590, y_pos), 1)
            
            # Tech elements (smart guitar)
            pygame.draw.circle(self.screen, BLUE, (450, 490), 8)  # LED
            pygame.draw.circle(self.screen, GREEN, (470, 490), 8)  # LED
            pygame.draw.circle(self.screen, RED, (490, 490), 8)  # LED
            
            # Family gathering setup
            for i in range(5):
                x = 150 + i*150
                y = 300
                pygame.draw.circle(self.screen, random.choice([BLUE, RED, GREEN, YELLOW, PURPLE]), (x, y), 20)  # Family members
            
            guitar_font = pygame.font.Font(None, 24)
            guitar_text = guitar_font.render("LiberLive C1 Smart Guitar", True, ORANGE)
            self.screen.blit(guitar_text, (420, 530))
    
    def draw_ui(self):
        level_info = LEVELS[self.current_level]
        
        # Level info
        level_text = self.font.render(f"Level {level_info.level_num}: {level_info.name}", True, BLACK)
        self.screen.blit(level_text, (10, 10))
        
        location_text = self.small_font.render(f"{level_info.location} ({level_info.year})", True, DARK_GREEN)
        self.screen.blit(location_text, (10, 40))
        
        # Player stats
        health_text = self.small_font.render(f"Health: {self.player.health}/{self.player.max_health}", True, BLACK)
        exp_text = self.small_font.render(f"Experience: {self.player.experience}", True, BLACK)
        defeated_text = self.small_font.render(f"{level_info.enemy_name} Solved: {self.enemies_defeated}/{level_info.enemies_to_defeat}", True, PURPLE)
        
        self.screen.blit(health_text, (10, 70))
        self.screen.blit(exp_text, (10, 90))
        self.screen.blit(defeated_text, (10, 110))
        
        # Progress bar
        progress = self.enemies_defeated / level_info.enemies_to_defeat
        bar_width = 300
        bar_height = 20
        pygame.draw.rect(self.screen, RED, (SCREEN_WIDTH - bar_width - 20, 20, bar_width, bar_height))
        pygame.draw.rect(self.screen, GREEN, (SCREEN_WIDTH - bar_width - 20, 20, bar_width * progress, bar_height))
        
        progress_text = self.small_font.render("Level Progress", True, BLACK)
        self.screen.blit(progress_text, (SCREEN_WIDTH - bar_width - 20, 45))
        
        # Show result message
        if self.result_message and pygame.time.get_ticks() - self.result_timer < 2000:
            result_surface = self.font.render(self.result_message, True, BLUE)
            result_rect = result_surface.get_rect(center=(SCREEN_WIDTH//2, 150))
            self.screen.blit(result_surface, result_rect)
    
    def run(self):
        running = True
        
        while running:
            dt = self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.game_state == "map":
                            self.game_state = "intro"
                        elif self.game_state == "intro":
                            self.game_state = "playing"
                        elif self.game_state == "level_complete":
                            self.current_level += 1
                            if self.current_level < len(LEVELS):
                                self.enemies_defeated = 0
                                self.enemies = []
                                self.player.health = min(self.player.max_health, self.player.health + 30)  # More healing
                                self.map_screen = BicycleJourneyMap(self.current_level)
                                self.intro_screen = IntroScreen(LEVELS[self.current_level])
                                self.game_state = "map"
                            else:
                                print("Congratulations! You've completed the entire career journey!")
                                print("🎸 Bonus: You've mastered the LiberLive C1 smart guitar!")
                                print("🚴 You discovered the cycling paths of adventure!")
                                print("🏀 You found time for basketball breaks!")
                                running = False
                    elif self.game_state == "quiz":
                        if self.quiz_screen.handle_input(event):
                            question = self.quiz_screen.current_question
                            correct = self.quiz_screen.selected_answer == question["correct"]
                            self.handle_quiz_result(correct)
                    elif self.game_state == "rhythm":
                        if self.rhythm_game.handle_input(event):
                            success = self.rhythm_game.success
                            self.handle_rhythm_result(success)
            
            if self.game_state == "map":
                self.map_screen.draw(self.screen)
                
            elif self.game_state == "intro":
                self.intro_screen.draw(self.screen)
                
            elif self.game_state == "playing":
                # Handle input
                keys = pygame.key.get_pressed()
                dx = dy = 0
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    dx = -1
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    dx = 1
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    dy = -1
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    dy = 1
                
                self.player.move(dx, dy)
                
                # Spawn enemies (less frequently for quiz levels)
                self.enemy_spawn_timer += dt
                level_info = LEVELS[self.current_level]
                if level_info.gameplay_type in ["quiz", "rhythm"]:
                    spawn_rate = 4000  # Slower spawning for interactive levels
                else:
                    spawn_rate = 2500  # Moderate spawning for action levels
                
                if self.enemy_spawn_timer > spawn_rate:
                    self.spawn_enemy()
                    self.enemy_spawn_timer = 0
                
                # Update enemies
                for enemy in self.enemies:
                    enemy.update(self.player)
                
                # Handle combat
                self.handle_combat()
                
                # Check conditions
                if self.player.health <= 0:
                    print("Game Over! The challenges of academia proved too much...")
                    running = False
                
                if self.enemies_defeated >= level_info.enemies_to_defeat:
                    self.game_state = "level_complete"
                
                # Draw everything
                self.draw_level_background()
                self.player.draw(self.screen)
                
                for enemy in self.enemies:
                    enemy.draw(self.screen)
                
                self.draw_ui()
                
            elif self.game_state == "quiz":
                # Draw game background but paused
                self.draw_level_background()
                self.player.draw(self.screen)
                for enemy in self.enemies:
                    enemy.draw(self.screen)
                self.draw_ui()
                
                # Draw quiz on top
                self.quiz_screen.draw(self.screen)
                
            elif self.game_state == "rhythm":
                # Draw game background but paused
                self.draw_level_background()
                self.player.draw(self.screen)
                for enemy in self.enemies:
                    enemy.draw(self.screen)
                self.draw_ui()
                
                # Draw rhythm game on top
                self.rhythm_game.draw(self.screen)
                
            elif self.game_state == "level_complete":
                self.screen.fill(LIGHT_GRAY)
                complete_text = self.font.render("LEVEL COMPLETE!", True, GREEN)
                complete_rect = complete_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
                self.screen.blit(complete_text, complete_rect)
                
                next_text = self.small_font.render("Press SPACE to continue to the next chapter", True, BLACK)
                next_rect = next_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 20))
                self.screen.blit(next_text, next_rect)
            
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run() 
# scenes/quiz_scene.py

import pygame
import random
import os
from settings import ASSET_PATH, QUIZ_FONT_SIZE, QUESTION_TIMER, WIDTH, HEIGHT

QUIZ_FILE_PATH = os.path.join(ASSET_PATH, "quiz_creator_questions.txt")

class QuizScene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = pygame.font.Font(None, QUIZ_FONT_SIZE)

        self.background = pygame.transform.scale(
            pygame.image.load(ASSET_PATH + "quiz_background.png"), (WIDTH, HEIGHT)
        )

        self.questions = self.load_questions()
        if not self.questions:
            print("ERROR: No quiz questions loaded!")        
        random.shuffle(self.questions)

        self.current_question = 0
        self.score = 0

        self.option_boxes = []
        self.generate_option_boxes()

        self.timer = QUESTION_TIMER
        self.clock = pygame.time.Clock()
# scenes/quiz_scene.py

import pygame
import os
from settings import ASSET_PATH, QUIZ_FONT_SIZE

QUIZ_FILE_PATH = os.path.join(ASSET_PATH, "quiz_creator_questions.txt")

class QuizScene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = pygame.font.Font(None, QUIZ_FONT_SIZE)
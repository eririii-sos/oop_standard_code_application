# scenes/result_scene.py

import pygame
from settings import QUIZ_FONT_SIZE, ASSET_PATH, WIDTH, HEIGHT

class ResultScene:
    def __init__(self, game, user_score, total_questions):
        self.game = game
        self.screen = game.screen
        self.font = pygame.font.Font(None, QUIZ_FONT_SIZE)
        self.title_font = pygame.font.Font(None, QUIZ_FONT_SIZE + 16)

        self.user_score = user_score
        self.total_questions = total_questions

        # Load background
        self.background = pygame.transform.scale(
            pygame.image.load(ASSET_PATH + "quiz_background.png"), (WIDTH, HEIGHT)
        )
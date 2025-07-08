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

        # Load mark images
        self.failed_mark = pygame.transform.scale(pygame.image.load(ASSET_PATH + "failed_mark.png"), (300, 150))
        self.poor_mark = pygame.transform.scale(pygame.image.load(ASSET_PATH + "poor_mark.png"), (300, 150))
        self.passed_mark = pygame.transform.scale(pygame.image.load(ASSET_PATH + "passed_mark.png"), (300, 150))
        self.perfect_mark = pygame.transform.scale(pygame.image.load(ASSET_PATH + "perfect_mark.png"), (300, 150))

        # Load expressions
        self.failed_expression = pygame.transform.scale(pygame.image.load(ASSET_PATH + "failed_face.png"), (300, 300))
        self.poor_expression = pygame.transform.scale(pygame.image.load(ASSET_PATH + "average_face.png"), (300, 300))
        self.passed_expression = pygame.transform.scale(pygame.image.load(ASSET_PATH + "passed_face.png"), (300, 300))
        self.happy_expression = pygame.transform.scale(pygame.image.load(ASSET_PATH + "happy_face.png"), (300, 300))

        self.exit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 230, 200, 50)
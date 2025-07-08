# scenes/result_scene.py

import pygame
from settings import QUIZ_FONT_SIZE

class ResultScene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = pygame.font.Font(None, QUIZ_FONT_SIZE)
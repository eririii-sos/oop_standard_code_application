# scenes/developer_info_scene.py

import pygame
from settings import TEXT_FONT_SIZE

class DeveloperInfoScene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = pygame.font.Font(None, TEXT_FONT_SIZE)
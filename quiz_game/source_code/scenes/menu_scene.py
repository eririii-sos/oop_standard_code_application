# scenes/menu_scene.py

import pygame
from settings import WIDTH, HEIGHT, TEXT_FONT_SIZE, ASSET_PATH
from core.music import play_music

class MenuScene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.background = pygame.transform.scale(
            pygame.image.load(ASSET_PATH + "home_background.png"), (WIDTH, HEIGHT)
        )
        self.font = pygame.font.Font(None, TEXT_FONT_SIZE)
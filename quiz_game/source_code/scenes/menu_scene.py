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
        self.start_button = pygame.Rect(395, 270, 280, 60)
        self.exit_button = pygame.Rect(395, 360, 280, 60)
        self.info_button = pygame.Rect(WIDTH - 60, HEIGHT - 60, 40, 40)

    def render(self):
        self.screen.blit(self.background, (0, 0))
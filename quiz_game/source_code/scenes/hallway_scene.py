# scenes/hallway_scene.py

import pygame
from settings import ASSET_PATH, WIDTH, HEIGHT

class HallwayScene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

        self.background = pygame.transform.scale(
            pygame.image.load(ASSET_PATH + "school_hall_background.jpg"), (WIDTH, HEIGHT)
        )
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

        # Character facial expression set
        self.char_expression_1 = pygame.transform.scale(pygame.image.load(ASSET_PATH + "neutral_face_2.png"), (300, 400))
        self.char_expression_2 = pygame.transform.scale(pygame.image.load(ASSET_PATH + "shocked_face.png"), (300, 400))
        self.char_expression_3 = pygame.transform.scale(pygame.image.load(ASSET_PATH + "disbelief_face.png"), (300, 400))
        self.char_expression_4 = pygame.transform.scale(pygame.image.load(ASSET_PATH + "wondering_face.png"), (300, 400))
        self.char_expression_5 = pygame.transform.scale(pygame.image.load(ASSET_PATH + "thinking_face_2.png"), (300, 400))
        self.char_expression_6 = pygame.transform.scale(pygame.image.load(ASSET_PATH + "plotting_face.png"), (300, 400))
        self.char_expression_7 = pygame.transform.scale(pygame.image.load(ASSET_PATH + "begging_face.png"), (300, 400))
        self.char_expression_8 = pygame.transform.scale(pygame.image.load(ASSET_PATH + "begging_face_2.png"), (300, 400))
        self.char_expression_9 = pygame.transform.scale(pygame.image.load(ASSET_PATH + "thinking_face.png"), (300, 400))
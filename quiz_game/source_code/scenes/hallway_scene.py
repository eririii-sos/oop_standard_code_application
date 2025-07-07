# scenes/hallway_scene.py

import pygame
from settings import ASSET_PATH, WIDTH, HEIGHT, TEXT_FONT_SIZE

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

        # Map expressions to dialogue lines
        self.expression_map = {
            0: self.char_expression_1,
            1: self.char_expression_2,
            2: self.char_expression_2,
            3: self.char_expression_3,
            4: self.char_expression_3,
            5: self.char_expression_4,
            6: self.char_expression_4,
            7: self.char_expression_5,
            8: self.char_expression_6,
            9: self.char_expression_7,
            10: self.char_expression_8,
            11: self.char_expression_9,
        }

        # Set font
        self.font = pygame.font.Font(None, TEXT_FONT_SIZE)

        # Monologue
        self.monologue = [
            "(Press SPACE to proceed)",
            "OH",
            "MY",
            "GOOOOOOOOOOSH!",
            "I completely forgot about our quiz today!",
            "I wasn't able to study! What am I going to do?",
            "...",
            "...",
            "...",
            "hey, uh...",
            "...will you help me?",
            "PLEASEEEEEEEE :3",
        ]
        self.current_line = 0
        self.typed_text = ""
        self.char_index = 0
        self.text_timer = 0
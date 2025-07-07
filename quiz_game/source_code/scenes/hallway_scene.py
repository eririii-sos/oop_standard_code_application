# scenes/hallway_scene.py

import pygame
from settings import ASSET_PATH, WIDTH, HEIGHT, TEXT_FONT_SIZE, TEXT_SPEED
from core.utilities import fade_in

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

        # Character name display
        self.character_name_display = self.font.render("Eri", True, (255, 255, 255))

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

        self.show_buttons = False
        self.yes_button = pygame.Rect(300, 500, 200, 50)
        self.no_button = pygame.Rect(550, 500, 200, 50)

        # Insert fade in transition
        fade_in(self.screen, self.background)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if self.current_line < len(self.monologue):
                self.current_line += 1
                self.typed_text = ""
                self.char_index = 0
                self.text_timer = 0
            if self.current_line >= len(self.monologue):
                self.show_buttons = True

    def update(self, dt):
        if self.current_line < len(self.monologue):
            line = self.monologue[self.current_line]
            if self.char_index < len(line):
                self.text_timer += dt
                if self.text_timer >= TEXT_SPEED:
                    self.typed_text += line[self.char_index]
                    self.char_index += 1
                    self.text_timer = 0

    def render(self):
        self.screen.blit(self.background, (0, 0))

        # Draw the current character expression
        expression_to_use = self.expression_map.get(self.current_line, self.char_expression_9)
        self.screen.blit(expression_to_use, (WIDTH // 2 - 150, HEIGHT - 400))

        if not self.show_buttons:
        # Draw text box
            box = pygame.Surface((700, 250))
            box.set_alpha(180)
            box.fill((0, 0, 0))
            self.screen.blit(box, (200, 500))

            # Draw character name above the box
            self.screen.blit(self.character_name_display, (210, 475))    

            # Draw monologue text
            wrapped = self.wrap_text(self.typed_text)
            for i, line in enumerate(wrapped):
                text_surface = self.font.render(line, True, (255, 255, 255))
                self.screen.blit(text_surface, (210, 510 + i * 28))

        # Draw Yes/No buttons
        else:
            pygame.draw.rect(self.screen, (0, 120, 0), self.yes_button)
            pygame.draw.rect(self.screen, (120, 0, 0), self.no_button)
            yes_text = self.font.render("Yes", True, (255, 255, 255))
            no_text = self.font.render("No", True, (255, 255, 255))
            self.screen.blit(yes_text, (self.yes_button.x + 75, self.yes_button.y + 15))
            self.screen.blit(no_text, (self.no_button.x + 75, self.no_button.y + 15))

    def wrap_text(self, text):
        words = text.split(' ')
        lines = []
        line = ''
        for word in words:
            test_line = line + word + ' '
            if self.font.size(test_line)[0] < 680:
                line = test_line
            else:
                lines.append(line)
                line = word + ' '
        lines.append(line)
        return lines
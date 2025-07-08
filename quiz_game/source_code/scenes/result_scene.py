# scenes/result_scene.py

import pygame
from settings import QUIZ_FONT_SIZE, ASSET_PATH, WIDTH, HEIGHT
from core.utilities import fade_in

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

        # Fade in
        fade_in(self.screen, self.background)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            from scenes.menu_scene import MenuScene
            self.game.scene_manager.go_to(MenuScene(self.game))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                from scenes.menu_scene import MenuScene
                self.game.scene_manager.go_to(MenuScene(self.game))

    def update(self, dt):
        pass
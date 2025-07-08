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

    def render(self):
        self.screen.blit(self.background, (0, 0))

        # Draw result text
        result_text = f"You got {self.user_score}/{self.total_questions} correct!"
        result_surface = self.title_font.render(result_text, True, (12, 0, 0))
        self.screen.blit(result_surface, (WIDTH - 490, 220))

        # Decide which mark and expression to show
        mark_image, char_expression = self.get_result_assets()

        self.screen.blit(mark_image, (WIDTH - 500, 230))
        self.screen.blit(char_expression, (WIDTH - 880, 130))

        # Draw Exit button
        pygame.draw.rect(self.screen, (255, 0, 0), self.exit_button_rect)
        exit_text = self.font.render("Press Esc to Exit", True, (255, 255, 255))
        self.screen.blit(exit_text, (self.exit_button_rect.x + 20, self.exit_button_rect.y + 15))

    def get_result_assets(self):
        if self.user_score == 0:
            return self.failed_mark, self.failed_expression
        elif self.user_score < self.total_questions // 2:
            return self.poor_mark, self.poor_expression
        elif self.user_score < self.total_questions:
            return self.passed_mark, self.passed_expression
        else:
            return self.perfect_mark, self.happy_expression
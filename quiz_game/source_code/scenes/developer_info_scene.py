# scenes/developer_info_scene.py

import pygame
from settings import TEXT_FONT_SIZE

class DeveloperInfoScene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = pygame.font.Font(None, TEXT_FONT_SIZE)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            from scenes.menu_scene import MenuScene
            self.game.scene_manager.go_to(MenuScene(self.game))
            
    def render(self):
        self.screen.fill((0, 0, 128))
        lines = [
            "Quiz Day",
            "",
            "Developed by: Jacey Erin D. Concepcion",
            "",
            "GitHub: eririii-sos",
            "https://github.com/eririii-sos/quiz_creator_program_2",
            "",
            "Special thanks to Prof. Danilo Madrigalajos!",
            "",
            "2025 | Made with Python and Pygame.",
            "",
            "[ Press ESC to return to Menu ]"
        ]

        y = 50
        for line in lines:
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text_surface, (50, y))
            y += 30
# scenes/menu_scene.py

import pygame
from settings import WIDTH, HEIGHT, TEXT_FONT_SIZE, ASSET_PATH
from core.music import play_music
from scenes.hallway_scene import HallwayScene
from scenes.developer_info_scene import DeveloperInfoScene

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

        play_music(ASSET_PATH + "home_bg_music.mp3")

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if self.start_button.collidepoint(pos):
                self.game.scene_manager.go_to(HallwayScene(self.game))
            elif self.exit_button.collidepoint(pos):
                self.game.running = False
            elif self.info_button.collidepoint(pos):
                self.game.scene_manager.go_to(DeveloperInfoScene(self.game))

    def update(self, dt):
        pass

    def render(self):
        self.screen.blit(self.background, (0, 0))
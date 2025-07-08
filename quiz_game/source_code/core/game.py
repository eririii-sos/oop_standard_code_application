# core/game.py

import pygame
from settings import WIDTH, HEIGHT, FPS
from core.scene_manager import SceneManager
from scenes.menu_scene import MenuScene

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Quiz Day")
        self.clock = pygame.time.Clock()
        self.running = True

        self.scene_manager = SceneManager(self.screen, MenuScene(self))

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.scene_manager.handle_event(event)

            self.scene_manager.update(dt)
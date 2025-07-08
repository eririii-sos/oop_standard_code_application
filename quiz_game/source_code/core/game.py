# core/game.py

import pygame
from settings import WIDTH, HEIGHT
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
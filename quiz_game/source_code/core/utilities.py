# core/utils.py

import pygame

def fade_in(screen, background, duration=1000):
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill((0, 0, 0))
    clock = pygame.time.Clock()
    alpha = 255
    fade_speed = 255 / (duration / 10)

    while alpha > 0:
        fade_surface.set_alpha(int(alpha))
        screen.blit(background, (0, 0))
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        alpha -= fade_speed
        clock.tick(60)

def fade_out(screen, duration=1000):
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill((0, 0, 0))
    clock = pygame.time.Clock()
    alpha = 0
    fade_speed = 255 / (duration / 10)

    while alpha < 255:
        fade_surface.set_alpha(int(alpha))
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        alpha += fade_speed
        clock.tick(60)
# core/music.py

import pygame

def play_music(track, volume=0.5):
    pygame.mixer.music.load(track)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)
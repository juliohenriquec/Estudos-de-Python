import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('Black Veil Brides - The Legacy.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()



import pygame


def initialize_pygame():
    pygame.init()
    game_screen = pygame.display.set_mode((25, 50))
    game_clock = pygame.time.Clock()
    return True
import pygame
soldier_img = pygame.image.load('soldier.png')
pygame.image.save(soldier_img, 'soldier.png')
soldier_img = pygame.transform.scale(soldier_img,(2, 6))

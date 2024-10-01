import pygame

ENTER = "enter"
UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"
# for randon bush function forbidden places for bushes
FORBIDDEN_IND_FOR_BOMBS = [(21, 46), (21, 47), (21, 48), (21, 49),
                            (22, 46), (22, 47), (22, 48), (22, 49),
                            (23, 46), (23, 47), (23, 48), (23, 48),
                            (0, 0), (0, 1),
                            (1, 0), (1, 1),
                            (2, 0), (2, 1),
                            (3, 0), (3, 1),
                            (4, 0), (4, 1),
                            (5, 0), (5, 1),
                            (6, 0), (6, 1)]
BOMB = "mine"
FREE = 0
SOLDIER = "soldier"
FLAG = "flag"
GREEN = (0, 128, 0)


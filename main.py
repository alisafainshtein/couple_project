import pygame
from screen import *
from game_field import *
from consts import *


def main():
    game_matrix = []
    initalize_game_metrix(game_matrix)
    set_screen_size()
    mine_index_list = []
    random_mines(mine_index_list)
    finish = False
    while not finish:



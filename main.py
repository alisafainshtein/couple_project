import pygame
from screen import *
from game_field import *
from consts import *


def main():
    game_matrix = []
    initalize_game_metrix(game_matrix)
    set_screen_size()
    mine_index_list = []
    mine_index_list = random_mines(mine_index_list)
    position_mines(game_matrix, mine_index_list)
    finish = False
    while not finish:
        for event in pygame.event.get():
            players_move = event.type
            if players_move != pygame.K_KP_ENTER:
                players_move = get_players_move(players_move)
                move_soldier_in_matrix(game_matrix, players_move)
            #elif players_move == pygame.K_KP_ENTER:
                # show mines
        # update screen
        pygame.display.flip()

main()






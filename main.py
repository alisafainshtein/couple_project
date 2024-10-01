import pygame
from screen import *
from game_field import *
from consts import *


def main():
    game_matrix = []
    initalize_game_metrix(game_matrix)
    pygame.init()
    size = 20
    num_rows = 25
    num_cols = 50
    screen = pygame.display.set_mode((num_cols * size, num_rows * size))
    # screen.fill(color_)
    assign_metrix_to_screen(game_matrix, screen, size)
    flag_img = pygame.image.load('flag.png')
    flag_img = pygame.transform.scale(flag_img,
                                      (4 * size, 3 * size))
    screen.blit(flag_img, ((49 * size) - (3 * size), (24 * size) - (4 * size)))
    pygame.display.flip()
    pygame.display.update()
    soldier_img = pygame.image.load('soldier.png')
    soldier_img = pygame.transform.scale(soldier_img,
                                         (2 * size, 6 * size))
    screen.blit(soldier_img, (0, 0))
    pygame.display.flip()
    pygame.display.update()

    time.sleep(10)
    #mine_index_list = []
    #mine_index_list = random_mines(mine_index_list)
    # position_mines(game_matrix, mine_index_list)
    # finish = False
    # while not finish:
    #     for event in pygame.event.get():
    #         players_move = event.type
    #         if players_move != pygame.K_KP_ENTER:
    #             players_move = get_players_move(players_move)
    #             move_soldier_in_matrix(game_matrix, players_move)
    #         #elif players_move == pygame.K_KP_ENTER:
    #             # show mines
    #     # update screen
    #     pygame.display.flip()


main()

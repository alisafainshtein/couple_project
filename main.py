# importing modules
import pygame
import screen
import soldier
import consts
import game_field
import sys

# initializing game

game_matrix = []
screen.initalize_game_metrix(game_matrix)
soldier_object = soldier.create_soldier_image()
flag_object = screen.create_flag_image()
game_field.init_object(game_matrix, soldier_object)
game_field.init_object(game_matrix, flag_object)
bush_places = []
bush_places = game_field.random_bushes(bush_places)
game_field.position_bushes(game_matrix, bush_places)
screen.blit((soldier.soldier_img), (0, 0))

# running game
while initPygame.initialize_pygame():
    while #not flag or bomb - consts bulian
        player_move = game_field.get_players_move()
        if player_move == consts.UP or player_move == consts.DOWN or player_move == consts.RIGHT or player_move == consts.LEFT:
            game_field.move_soldier(game_matrix, player_move)
        elif player_move == consts.ENTER:
            game_field.show_bushes()
        else:
            # show massage to not press unnececery buttons


    if flag:
        game_field.win_messege()
        pygame.QUIT
    elif bomb:
        game_field.lose_messege()
        pygame.QUIT
        sys.exit()
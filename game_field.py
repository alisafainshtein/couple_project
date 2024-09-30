import initPygame
import screen
import soldier
import pygame
import  consts


# game starting position
def init_object(game_metrix, game_object, object_indexes):



def get_players_move():
    for event in pygame.event.get():
        players_move = event.type
        if players_move == pygame.K_UP:
            players_move = consts.UP
            return players_move
        elif players_move == pygame.K_DOWN:
            players_move = consts.DOWN
            return players_move
        elif players_move == pygame.K_LEFT:
            players_move = consts.LEFT
            return players_move
        elif players_move == pygame.K_RIGHT:
            players_move = consts.RIGHT
            return players_move
        elif players_move == pygame.K_KP_ENTER:
            players_move = consts.ENTER
            return players_move

def move_soldier(game_matrix, players_move):
    if players_move == pygame.K_UP:

    elif players_move == pygame.K_DOWN:
    elif players_move == pygame.K_LEFT:
    elif players_move == pygame.K_RIGHT:
    elif players_move == pygame.K_KP_ENTER:

def show_bushes():



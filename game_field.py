import initPygame
import screen
import soldier
import pygame
import  consts
import random

# game starting position
def init_object(game_metrix, game_object, object_indexes):

def random_mines(mine_index_list):
    tmp_forbidden_list = consts.FORBIDDEN_IND_FOR_BOMBS
    for i in range(20):
        indexes_allowed = False
        block_counter = 0
        while not indexes_allowed:
            indexes_of_entire_mine = []
            index_of_part_of_mine = ()
            row = random.randrange(0, 25)
            while block_counter <= 3:
                col = random.randrange(0, 50)
                index_of_part_of_mine = (row, col)
                if not index_of_part_of_mine in tmp_forbidden_list:
                    tmp_forbidden_list.append(index_of_part_of_mine)
                    indexes_of_entire_mine.append(index_of_part_of_mine)
                    block_counter += 1
                    if block_counter == 3:
                        indexes_allowed = True
                else:
                    indexes_allowed = False
                    block_counter = 0
                    indexes_of_entire_mine.clear()
        mine_index_list.append(indexes_of_entire_mine)
    return mine_index_list

def position_bushes(game_metrix, bush_index_list):
    for b in range(len(bush_index_list)):
        for i in range(len(game_metrix)):
            for j in range(len(game_metrix[i])):
                if bush_index_list[b][0] == i and bush_index_list[b][1] == j:
                    game_metrix[i][j] = consts.BOMB
    return game_metrix
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



def show_bushes():





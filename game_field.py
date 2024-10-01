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
        while not indexes_allowed:
            indexes_of_entire_mine = []
            index_of_part_of_mine = ()
            row = random.randrange(0, 25)
            col = random.randrange(0, 50)
            index_of_part_of_mine = (row, col)
            index_of_part_of_mine2 = (row, col + 1)
            index_of_part_of_mine3 = (row, col + 2)
            if not index_of_part_of_mine in tmp_forbidden_list or not index_of_part_of_mine2 in tmp_forbidden_list or not index_of_part_of_mine3 in tmp_forbidden_list:
                    tmp_forbidden_list.append(index_of_part_of_mine)
                    tmp_forbidden_list.append(index_of_part_of_mine2)
                    tmp_forbidden_list.append(index_of_part_of_mine3)
                    indexes_of_entire_mine.append(index_of_part_of_mine)
                    indexes_of_entire_mine.append(index_of_part_of_mine2)
                    indexes_of_entire_mine.append(index_of_part_of_mine3)
                    indexes_allowed = True
                else:
                    indexes_allowed = False
                    indexes_of_entire_mine.clear()
        mine_index_list.append(indexes_of_entire_mine)
    return mine_index_list



def position_mines(game_metrix, mine_index_list):
    for row in mine_index_list:
        for tuple_index in mine_index_list:
            for i in range(len(game_metrix)):
                for j in range(len(game_metrix[i])):
                    if row == i and tuple == j:
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
    for i in range(len())
    if players_move == pygame.K_UP:

    elif players_move == pygame.K_DOWN:

    elif players_move == pygame.K_LEFT:

    elif players_move == pygame.K_RIGHT:



def show_mines():





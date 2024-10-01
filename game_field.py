import screen
import soldier
import pygame
from consts import *
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
                        game_metrix[i][j] = BOMB
    return game_metrix
def get_players_move(players_move):
    if players_move == pygame.K_UP:
        players_move = UP
        return players_move
    elif players_move == pygame.K_DOWN:
        players_move = DOWN
        return players_move
    elif players_move == pygame.K_LEFT:
        players_move = LEFT
        return players_move
    elif players_move == pygame.K_RIGHT:
        players_move = RIGHT
        return players_move


def move_soldier_in_matrix(game_matrix, players_move, game_screen):
    tmp_game_matrix = game_matrix
    for i in range(len(tmp_game_matrix)):
        for j in range(len(tmp_game_matrix[i])):
            soldier_counter = 0
            if tmp_game_matrix == SOLDIER:
                soldier_counter += 1 #check when cant move to that directions
                if i > 0 and players_move == UP:
                    if tmp_game_matrix[i][j] != BOMB:
                        game_matrix[i][j] = FREE
                        game_matrix[i - 1][j] = SOLDIER
                        if soldier_counter == 1:
                            soldier_index = (i - 1, j)
                            screen.position_soldier(game_screen, soldier_index)

                    elif tmp_game_matrix[i][j] == BOMB and soldier_counter > 4:
                            lose
                    elif tmp_game_matrix[i][j] == FLAG and soldier_counter <= 4:
                        win

                elif i < 50 and players_move == DOWN:
                    if tmp_game_matrix[i][j] != BOMB:
                        game_matrix[i][j] = FREE
                        game_matrix[i + 1][j] = SOLDIER
                        if soldier_counter == 1:
                            soldier_index = (i + 1, j)
                            screen.position_soldier(game_screen, soldier_index)

                    elif soldier_counter > 4:
                            lose
                    elif tmp_game_matrix[i][j] == FLAG and soldier_counter <= 4:
                        win
                elif j > 0 and players_move == LEFT:
                    if tmp_game_matrix[i][j] != BOMB:
                        game_matrix[i][j] = FREE
                        game_matrix[i][j - 1] = SOLDIER
                        if soldier_counter == 1:
                            soldier_index = (i, j - 1)
                            screen.position_soldier(game_screen, soldier_index)
                    elif soldier_counter > 4:
                            lose
                    elif tmp_game_matrix[i][j] == FLAG and soldier_counter <= 4:
                        win
                elif j < 25 and players_move == RIGHT:
                    if tmp_game_matrix[i][j] != BOMB:
                        game_matrix[i][j] = FREE
                        game_matrix[i][j + 1] = SOLDIER
                        if soldier_counter == 1:
                            soldier_index = (i, j + 1)
                            screen.position_soldier(game_screen, soldier_index)

                    elif soldier_counter > 4:
                        lose
                    elif tmp_game_matrix[i][j] == FLAG and soldier_counter <= 4:
                        win
    return game_matrix



def show_mines():





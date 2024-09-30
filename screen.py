import pygame
import consts
import time



# make screen background

def initalize_game_metrix(game_matrix):
    for i in range(25):
        inner_list = []
        for j in range(50):
            if 0 <= j <= 6 and 0 <= i <= 1:
                inner_list.append("soldier")
            elif 46 <= j <= 49 and 21 <= i <= 23:
                inner_list.append("flag")
            else:
                inner_list.append(consts.FREE)
        game_matrix.append(inner_list)
    return game_matrix


game_matrix = []
initalize_game_metrix(game_matrix)


# def set_screen_size():
#     pygame.init()
#     size = 20
#     color = (10, 10, 10)
#     num_rows = 25
#     num_cols = 50
#     screen = pygame.display.set_mode((num_cols * size, num_rows * size))
#     screen.fill(color)
#     pygame.display.flip()
#     pygame.display.update()
#     pygame.time.wait()
#
# set_screen_size()

# pygame.init()
# global screen
# screen_size = (50, 25)
# screen = pygame.display.set_mode(screen_size)
# color = (10, 10, 10)
# screen.fill(color)
# pygame.display.flip()
# time.sleep(30)


screen = pygame.display.set_mode((100,200))

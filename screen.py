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

color = (0, 128, 0)
color_ = (10, 10, 10)


def assign_metrix_to_screen(matrix, screen, size):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for i in range(num_rows):
        for j in range(num_cols):
            pygame.draw.rect(screen, color, (j * size, i * size, size - 1, size - 1))
    pygame.display.update()


def set_screen_size():
    pygame.init()
    size = 20
    num_rows = 25
    num_cols = 50
    screen = pygame.display.set_mode((num_cols * size, num_rows * size))
    # screen.fill(color_)
    assign_metrix_to_screen(game_matrix, screen, size)
    img = pygame.image.load('flag.png')
    img = pygame.transform.scale(img,
                                 (4 * size, 3 * size))
    screen.blit(img, ((49 * size) - (3 * size), (24 * size) - (4 * size)))

    pygame.display.flip()
    pygame.display.update()

    time.sleep(10)
    return screen




set_screen_size()

import time
import pygame
import copy

# Set the size of each cell in the screen
size = 10

# Set the sleepInterval (update time) between each generation
sleepInterval = 0.001

# set colors
black_color = (10, 10, 10)
alive_color = (255, 255, 255)
grid_color = (40, 40, 40)

# defualt values
ALIVE_CELL = 1
DEAD_CELL = 0


# --------------------------------Implement this function--------------------------------
def next_generation(current_generation_matrix):
    pass


# Update screen colors by the recieved matrix. Cell with '0' value will be black, otherwise white.
def fill_colors(matrix, screen, size):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # run over all the cells in the current matrix
    for i in range(num_rows):
        for j in range(num_cols):
            color = black_color if matrix[i][j] == 0 else alive_color
            pygame.draw.rect(screen, color, (j * size, i * size, size - 1, size - 1))
    pygame.display.update()


# Main function
def main():
    # Initial pygame
    pygame.init()
    # Set the screen size
    num_cols, num_rows = 80, 60
    screen = pygame.display.set_mode((num_cols * size, num_rows * size))
    screen.fill(grid_color)
    pygame.display.flip()
    pygame.display.update()
    running = False
    # Create zeros matrix
    current_generation_matrix = [[0 for x in range(num_cols)] for y in range(num_rows)]
    fill_colors(current_generation_matrix, screen, size)

    while True:
        # Wait for events
        for event in pygame.event.get():
            # if user wants to QUIT, close pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # If space was pressed, stop/resume the game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running

            # Mouse is used to active cells
            # If mouse was pressed
            if pygame.mouse.get_pressed()[0]:
                # Get the location of the mouse
                position = pygame.mouse.get_pos()
                # Change the cell of wich the mouse pressed value to 1
                current_generation_matrix[position[1] // size][position[0] // size] = 1-current_generation_matrix[position[1] // size][position[0] // size]
                # pygame.draw.rect(screen, alive_color, ((position[0] // size) * size, (position[1] // size) * size, size - 1, size - 1))
                fill_colors(current_generation_matrix, screen, size)
                pygame.display.update()

        if running:
            next_generation_matrix = next_generation(current_generation_matrix)
            current_generation_matrix = next_generation_matrix
            fill_colors(current_generation_matrix, screen, size)

        # sleep for sleepInterval seconds
        time.sleep(sleepInterval)


if __name__ == '__main__':
    main()
import pygame
import sys
import numpy as np

# Constants initialization
WIDTH, HEIGHT = 600, 600
BG_COLOR = (25, 25, 25)
CELL_SIZE = 5
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
GRAY_COLOR = (128, 128, 128)

# Initialization Stuff
pygame.init()
pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
grid = np.random.randint(2, size=(ROWS, COLS))


def draw_grid():
    """Draws the game grid"""
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY_COLOR, (0, y), (WIDTH, y))


def draw_cells():
    """Draws cells"""
    for x in range(COLS):
        for y in range(ROWS):
            if grid[y, x]:
                pygame.draw.rect(screen, (255, 255, 255), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def get_neighbors(x, y):
    """Returns neighbors of the cell by X & Y """
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            col = (x + i + COLS) % COLS
            row = (y + j + ROWS) % ROWS
            neighbors.append(grid[row, col])
    return neighbors


def main():
    global grid
    while True:
        screen.fill(BG_COLOR)
        draw_grid()
        draw_cells()
        new_grid = np.copy(grid)
        for x in range(COLS):
            for y in range(ROWS):
                neighbors = get_neighbors(x, y)
                live_neighbors = np.count_nonzero(neighbors)
                if grid[y, x]:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[y, x] = 0
                else:
                    if live_neighbors == 3:
                        new_grid[y, x] = 1
        grid = new_grid
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main()

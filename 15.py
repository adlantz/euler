"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

(picture not shown)

How many such routes are there through a 20x20 grid?
"""


def fill_grid(x, y, grid):
    if grid[x][y] is None:
        num_paths_x = 0
        num_paths_y = 0
        if x + 1 < len(grid):
            num_paths_x, grid = fill_grid(x + 1, y, grid)
        if y + 1 < len(grid):
            num_paths_y, grid = fill_grid(x, y + 1, grid)

        grid[x][y] = num_paths_x + num_paths_y
    return grid[x][y], grid


N = 20
grid = [[None for i in range(N + 1)] for i in range(N + 1)]

grid[len(grid) - 1][len(grid) - 1] = 1

num_paths, grid = fill_grid(0, 0, grid)


print(num_paths)
# import numpy as np
# print(np.matrix(grid))

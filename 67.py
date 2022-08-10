"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
"""

import numpy as np


grid = np.loadtxt("67.txt", delimiter=",")

N = 100
for i in range(N - 2, -1, -1):
    for j in range(i + 1):
        grid[i][j] = grid[i][j] + max([grid[i + 1][j], grid[i + 1][j + 1]])

print(grid[0][0])

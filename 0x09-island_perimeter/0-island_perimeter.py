#!/usr/bin/python3

"""Gets Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in a grid
    Args:
        grid: 2d list of intergers containing water(0) or land(1)
    Return:
        the perimeter of the island
    """

    P = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if (grid[x][y] == 1):
                if (x <= 0 or grid[x - 1][y] == 0):
                    P += 1
                if (x >= len(grid) - 1 or grid[x + 1][y] == 0):
                    P += 1
                if (y <= 0 or grid[x][y - 1] == 0):
                    P += 1
                if (y >= len(grid[x]) - 1 or grid[x][y + 1] == 0):
                    P += 1
    return P

#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ Rotates 2D matrix at 90 degrees clockwise.
    Args:
        matrix (list[[list]]): The matrix
    """
    n = len(matrix)
    for a in range(int(n / 2)):
        y = (n - a - 1)
        for b in range(a, y):
            x = (n - 1 - b)
            # Current number
            tmp = matrix[a][b]
            # change top to the left
            matrix[a][b] = matrix[x][a]
            # change left for bottom
            matrix[x][a] = matrix[y][x]
            # change bottom to the right
            matrix[y][x] = matrix[b][y]
            # change right for top
            matrix[b][y] = tmp

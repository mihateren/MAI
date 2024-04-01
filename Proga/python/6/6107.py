import numpy as np


def make_board(n):
    board = np.zeros((n, n), dtype="int8")
    for i in range(n):
        for j in range(n):
            if not (j % 2):
                if not (i % 2):
                    board[i][j] = 1
            else:
                if (i % 2):
                    board[i][j] = 1
    return board
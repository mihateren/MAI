import numpy as np


def snake(m, n, direction="H"):
    matrix = np.zeros((n, m), dtype="int16")
    num = 1
    if direction == "H":
        for i in range(n):
            for j in range(m):
                if i % 2 == 0:
                    matrix[i][j] = num
                else:
                    matrix[i][m - 1 - j] = num
                num += 1
    else:
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    matrix[j][i] = num
                else:
                    matrix[n - 1 - j][i] = num
                num += 1
    return matrix

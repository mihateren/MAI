import numpy as np


def stairs(vector):
    n = len(vector)
    matrix = np.zeros((n, n), dtype="int")
    for i in range(n):
        for j in range(n):
            if (i == 0):
                matrix[i][j] = vector[j]
            else:
                matrix[i][j] = matrix[i - 1][(j - 1) % n]
    return matrix

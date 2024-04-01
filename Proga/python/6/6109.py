import numpy as np


def rotate(matrix, angle):
    if angle == 90:
        return np.rot90(matrix, -1)
    elif angle == 180:
        return np.rot90(np.rot90(matrix, -1), -1)
    elif angle == 270:
        return np.rot90(matrix)
    return matrix
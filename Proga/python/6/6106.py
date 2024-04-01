import numpy as np


def multiplication_matrix(n):
    m = np.arange(1, n + 1)
    return m * m[:, None]
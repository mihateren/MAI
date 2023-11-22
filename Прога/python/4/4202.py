def make_matrix(size, value=0):
    result = []
    m, n = 0, 0
    if isinstance(size, tuple):
        m, n = size
    else:
        m = n = size
    for i in range(n):
        boofer = []
        for j in range(m):
            boofer.append(int(value))
        result.append(boofer)
    return result
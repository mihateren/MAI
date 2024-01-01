def merge(a, b):
    c = list(a + b)
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            if c[i] > c[j]:
                x = c[i]
                c[i] = c[j]
                c[j] = x
    return tuple(c)
def merge(a, b):
    try:
        a1 = iter(a)
        b1 = iter(b)
    except TypeError:
        raise StopIteration
    if not (all(isinstance(i, type(a[0])) for i in a) and all(isinstance(i, type(a[0])) for i in b)):
        raise TypeError
    if list(a) != sorted(a) or list(b) != sorted(b):
        raise ValueError
    c = list(a) + list(b)
    c.sort()
    return tuple(c)
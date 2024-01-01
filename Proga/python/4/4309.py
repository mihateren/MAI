def cycle(s):
    while s:
        for x in s:
            yield x

print(*(x for t, x in zip(range(5), cycle([1, 2, 3]))))

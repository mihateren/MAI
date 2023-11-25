def cycle(arr):
    while 1:
        for x in arr:
            yield x

print(*(x for t, x in zip(range(5), cycle([1, 2, 3]))))

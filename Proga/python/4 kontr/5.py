from itertools import product, accumulate


def grasshopper(start, finish, length):
    res = []
    for x in product([1, 2], repeat=length):
        if start + sum(x) == finish:
            res.append([start] + [start + y for y in accumulate(x)])
    return res


result = grasshopper(1, 10, 5)
print(*result, sep="\n")

from itertools import product, accumulate


def notfinish(arr, n):
    for i in range(len(arr) - 1):
        if n == arr[i]:
            return 0
    return 1


def bunny(start, finish, length):
    res = []
    for x in product([1, -1, 3, -3], repeat=length):
        if start + sum(x) == finish and notfinish([start] + [start + y for y in accumulate(x)], finish):
            res.append([start] + [start + y for y in accumulate(x)])
    return res


result = bunny(7, 10, 3)
print(*result, sep="\n")
from math import prod, pow


def G(arr):
    n = len(arr)
    return pow(prod(arr), 1 / n)


s = input()
x = list(map(float, s.split()))
print(G(x))

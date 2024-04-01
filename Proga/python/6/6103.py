from math import comb


x, y = map(int, input().split())
print(comb(x, y) * y // x, comb(x, y))
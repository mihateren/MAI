from itertools import product


def f(a, b, c):
    return eval(example)


example = input()
print('a b c f')
for a, b, c in product(range(0, 2), repeat=3):
    print(a, b, c, int(f(a, b, c)))
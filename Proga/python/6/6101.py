import math


def f(x):
    return (
        math.log(math.pow(x, 3 / 16), 32)
        + math.pow(x, math.cos((math.pi * x) / (2 * math.exp(1))))
        - math.pow(math.sin(x / math.pi), 2)
    )


x = float(input())
print(f(x))

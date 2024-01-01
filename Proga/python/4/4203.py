def gcd(*numbers):
    x = numbers[0]
    for i in range(1, len(numbers)):
        y = numbers[i]
        while x != y:
            x, y = max(x, y), min(x, y)
            x = x - y
    return x
def gcd(a, b):
    while a != b:
        a, b = min(a, b), max(a, b)
        b = b - a
    return b
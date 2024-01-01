def f():
    numbers = set(map(int, input().split(";")))
    for a in sorted(numbers):
        boofer = set()
        for b in numbers:
            if a != b:
                nod = evklid(a, b)
                if nod == 1:
                    boofer.add(b)
        boofer = list(map(str, sorted(boofer)))
        if len(boofer) != 0:
            print(a, "-", ", ".join(boofer))


def evklid(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def main():
    f()


if __name__ == '__main__':
    main()
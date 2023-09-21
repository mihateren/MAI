def f(x, y):
    while x != y:
        x, y = max(x, y), min(x, y)
        x -= y
    print(x)


def main():
    x = int(input())
    y = int(input())
    f(x, y)


if __name__ == '__main__':
    main()
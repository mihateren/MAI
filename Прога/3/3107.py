def f(a, b):
    print(a + b)


def main():
    a, b = map(int, input().split())
    f(a, b)


if __name__ == '__main__':
    main()
def f(n, m):
    print("Петя") if ((6 + n) > (12 + m)) else print("Вася")


def main():
    n = int(input())
    m = int(input())
    f(n, m)


if __name__ == '__main__':
    main()
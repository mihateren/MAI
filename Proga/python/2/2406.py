def f(n):
    x1 = int(input())
    for i in range(n - 1):
        x2 = int(input())
        while x1 != x2:
            if x1 > x2:
                x1 -= x2
            else:
                x2 -= x1
        x1 = x2
    print(x1)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
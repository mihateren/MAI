def f(n):
    maxim = base = -1
    for i in range(2, 11):
        x = n
        s = 0
        while x > 0:
             s += x % i
             x = x // i
        if s > maxim:
            maxim = s
            base = i
    print(base)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
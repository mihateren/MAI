def f():
    numbers = list(map(int, input().split()))
    x1 = numbers[0]
    for i in range(1, len(numbers)):
        x2 = numbers[i]
        while x1 != x2:
            if x1 > x2:
                x1 -= x2
            else:
                x2 -= x1
        x1 = x2
    print(x1)


def main():
    f()


if __name__ == '__main__':
    main()
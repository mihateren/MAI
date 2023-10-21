def f(n):
    size = n
    for i in range(size):
        for j in range(size):
            digit = str(min(i, j, size - i - 1, size - j - 1) + 1)
            print(digit.rjust(len(str((size + 1) // 2)), ' '), end=' ')
        print()


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
from itertools import product


def f(n, m):
    nArr = [i for i in range(1, n + 1)]
    mArr = [i for i in range(1, m + 1)]
    for x, y in list(product(nArr, mArr)):
        item = (x - 1) * m + y
        cellSize = len(str(n * m))
        print(str(item).rjust(cellSize), end=" ")
        if y == m:
            print("\r")


def main():
    n = int(input())
    m = int(input())
    f(n, m)


if __name__ == '__main__':
    main()
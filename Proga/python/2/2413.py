def f(n, m):
    for i in range(n):
        k = 0
        for j in range(m):
            item = i + j * n + 1
            cellSize = len(str(n * m))
            print(str(item).rjust(cellSize), end=" ")
            k += 1
            if (k == m):
                print("\r")


def main():
    n = int(input())
    m = int(input())
    f(n, m)


if __name__ == '__main__':
    main()
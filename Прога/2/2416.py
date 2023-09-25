def f(n, m):
    rowLen = m * n + (m - 1)
    for i in range(1, n + 1):
        k = 0
        for j in range(i, (n + 1) * i, i):
            if m % 2 != 0:
                spaces = m // 2
                if j < 10:
                    print(" " * spaces + str(j) + " " * spaces, end="")
                else:
                    print(" " * (spaces - 1) + str(j) + " " * spaces, end="")
            if (k < n - 1):
                print("|", end="")
            k += 1
            if k == n:
                print("\r")
                if i != n:
                    print("-" * rowLen)    


def main():
    n = int(input())
    m = int(input())
    f(n, m)


if __name__ == '__main__':
    main()
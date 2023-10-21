def f(n, m):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == n:
                print(f'{(str(i * j) + " " if m % 2 else str(i * j)).center(m)}')
            else:
                print(f'{(str(i * j) + " " if m % 2 else str(i * j)).center(m)}|', end='')
        if i * j != n * n:
            print(f'{"-"* ((m + 1) * n - 1)}')    


def main():
    n = int(input())
    m = int(input())
    f(n, m)


if __name__ == '__main__':
    main()
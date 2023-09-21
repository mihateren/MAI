def f(n, m):
    if m > n:
        for i in range(n, m + 1):
            print(i, end=" ")
    else:
        step = -1
        for i in range(n, m - 1, -1):
            print(i, end=" ")
    

def main():
    n = int(input())
    m = int(input())
    f(n, m)


if __name__ == '__main__':
    main()
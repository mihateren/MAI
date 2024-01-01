def f(n):
    x = 1
    i = k = 0
    while x < n:
        while True:
            x += i
            if x > n:
                break
            k += 1
            i += 1
    numbersInStr = 0
    c = 1
    if n == 1:
        print(1)
    else:
        for j in range(1, n + 1):
            if c != k + 1:
                print(j, end=" ")
                numbersInStr += 1
                if numbersInStr == c:
                    print("\r")
                    numbersInStr = 0
                    c += 1


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
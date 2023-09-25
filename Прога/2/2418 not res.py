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
    currentRow = 1
    if n == 1:
        print(1)
        return
    rowSize = k * len(str(n)) + (k - 1)
    s = ""
    for j in range(1, n + 1):
        if currentRow != k + 1:
            numbersInStr += 1
            if () != currentRow:
                s += f"{j} "
            else:
                s += f"{j}"
                print(s.center(rowSize), end="")
                print("\r")
                numbersInStr = 0
                currentRow += 1
                s = ""


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
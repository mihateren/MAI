def f(n, maxLen):
    maxLen -= 3
    for i in range(n):
        s = input()
        if len(s) < maxLen:
            print(s)
            maxLen -= len(s)
        elif maxLen > 0:
            print(s[:maxLen], '...', sep='')
            maxLen = 0


def main():
    maxLen = int(input())
    n = int(input())
    f(n, maxLen)


if __name__ == '__main__':
    main()
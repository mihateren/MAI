def f(n, maxLen):
    currentLen = 0
    text = []
    for i in range(n):
        text.append(input())
    for i in range(n):
        s = text[i]
        currentLen += len(s)
        if currentLen + 3 < maxLen:
            print(s)
        elif currentLen + 3 == maxLen:
            print(s[:-3:] + "." * 3)
            break
        else:
            print(s[:(maxLen - currentLen - 3):] + "." * 3)
            break


def main():
    maxLen = int(input())
    n = int(input())
    f(n, maxLen)


if __name__ == '__main__':
    main()
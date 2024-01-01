def f(s):
    x = s[0]
    counter = 1
    for i in range(1, len(s)):
        if x == s[i]:
            counter += 1
        else:
            print(x, counter)
            counter = 1
        x = s[i]
    print(x, counter)


def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
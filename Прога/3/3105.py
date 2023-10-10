def f(s):
    s1 = ''.join(reversed(s))
    if s == s1:
        print("YES")
    else:
        print("NO")


def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
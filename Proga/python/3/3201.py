def f(s):
    s1 = ""
    for i in set(s):
        s1 += i
    print(s1)


def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
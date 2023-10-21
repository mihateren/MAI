def f(n):
    s1 = int(n[1]) + int(n[2])
    s2 = int(n[0]) + int(n[1])
    print(max(s1, s2), min(s1, s2), sep='')


def main():
    n = input()
    f(n)


if __name__ == '__main__':
    main()
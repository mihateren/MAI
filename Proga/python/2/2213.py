def f(a, b, c):
    x1, x2 = a[0], a[1]
    if ((x1 == b[0]) and (x1 == c[0] or x1 == c[1])) or ((x1 == b[1]) and (x1 == c[0] or x1 == c[1])):
        print(x1)
    elif ((x2 == b[0]) and (x2 == c[0] or x2 == c[1])) or ((x2 == b[1]) and (x2 == c[0] or x2 == c[1])):
        print(x2)


def main():
    a = input()
    b = input()
    c = input()
    f(a, b, c)


if __name__ == '__main__':
    main()
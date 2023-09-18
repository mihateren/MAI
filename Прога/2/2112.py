def f(n, m):
    x0 = ""
    x1 = ""
    x2 = ""
    n1 = zero(n)
    m1 = zero(m)   
    x0 = str((int(n1[0]) + int(m1[0])) % 10)
    x1 = str((int(n1[1]) + int(m1[1])) % 10)
    x2 = str((int(n1[2]) + int(m1[2])) % 10)
    result = x0 + x1 + x2
    print(result)


def zero(s):
    x = "0" * (3 - len(s)) + s
    return x


def main():
    n = input()
    m = input()
    f(n, m)


if __name__ == '__main__':
    main()
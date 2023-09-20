def f(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("YES")
    else:
        print("NO")


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    f(a, b, c)


if __name__ == '__main__':
    main()
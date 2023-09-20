def f(n):
    if n == n[::-1]:
        print("YES")
    else:
        print("NO")


def main():
    n = input()
    f(n)


if __name__ == '__main__':
    main()
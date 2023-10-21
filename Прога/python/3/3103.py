def f(L, N):
    for i in range(N):
        s = input()
        if len(s) > L:
            print(s[:(L - 3)] + "." * 3)
        else:
            print(s)


def main():
    L = int(input())
    N = int(input())
    f(L, N)


if __name__ == '__main__':
    main()
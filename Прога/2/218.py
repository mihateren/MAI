def printer(n, s):
    if n == 1:
        print(f'Я больше никогда не буду писать "{s}"!')
    else:
        print((f'Я больше никогда не буду писать "{s}"!\n') * (n - 1) + f'Я больше никогда не буду писать "{s}"!')


def main():
    n = int(input())
    s = input()
    printer(n, s)


if __name__ == '__main__':
    main()
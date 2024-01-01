def f(n):
    k = 0
    for i in range(n):
        x = input()
        if x == x[::-1]:
            k += 1
    print(k)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
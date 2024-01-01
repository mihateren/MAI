from itertools import product


def f(n):
    arr = [i for i in range(1, n + 1)]
    values = list(product(arr, arr))
    s = ""
    for x, y in values:
        s += str(x * y) + " "
        if len(s.split()) == n:
            print(s)
            s = ""


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
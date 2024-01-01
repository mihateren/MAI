from itertools import product


def f(n):
    arr = [i for i in range(1, n + 1)]
    print("А Б В")
    for x, y, z in list(product(arr, arr, arr)):
        if x + y + z == n:
            print(f"{x} {y} {z}")


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
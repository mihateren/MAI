def f(n):
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    p = int(input())
    for i in range(n):
        print(numbers[i] ** p)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
def f(n):
    porridge = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
    for i in range(n):
        print(porridge[i % len(porridge)])


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
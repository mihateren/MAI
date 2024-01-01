def f(petya, vasya):
    print("Петя") if petya > vasya else print("Вася")


def main():
    petya = int(input())
    vasya = int(input())
    f(petya, vasya)


if __name__ == '__main__':
    main()
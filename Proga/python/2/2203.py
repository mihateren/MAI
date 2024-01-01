def f(petya, vasya, tolya):
    if (petya > vasya) and (petya > tolya):
        print("Петя")
    elif (vasya > petya) and (vasya > tolya):
        print("Вася")
    else:
        print("Толя")


def main():
    petya = int(input())
    vasya = int(input())
    tolya = int(input())
    f(petya, vasya, tolya)


if __name__ == '__main__':
    main()
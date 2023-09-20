def f(name):
    print(f"Здравствуйте, {name}!")
    print("Как дела?")
    answer = input()
    if answer == "хорошо":
        print("Я за вас рада!")
    else:
        print("Всё наладится!")


def main():
    print("Как Вас зовут?")
    name = input()
    f(name)


if __name__ == '__main__':
    main()
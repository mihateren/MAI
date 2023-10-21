def f(name, n):
    print(f"Группа №{n[0]}.")
    print(f"{n[2]}. {name}.")
    print(f"Шкафчик: {n}.")
    print(f"Кроватка: {n[1]}.")


def main():
    name = input()
    n = input()
    f(name, n)


if __name__ == '__main__':
    main()
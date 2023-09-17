def printer(n):
    if n == 1:
        print("Купи слона!")
    else:
        print((f"Купи слона! \n") * (n - 1) + "Купи слона!")


def main():
    n = int(input())
    printer(n)


if __name__ == '__main__':
    main()
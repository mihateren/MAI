from math import sqrt


def f(a, b, c):
    D = b * b - 4 * a * c
    if (a == b == c == 0):
        print('Infinite solutions')
    if (a != 0):
        if (D > 0):
            x1 = (-b + sqrt(D))/(2 * a)
            x2 = (-b - sqrt(D))/(2 * a)
            print(f"{x2:.2f} {x1:.2f}")
        elif (D == 0):
            x = -b / (2 * a)
            print(f"{x:.2f}")
        else:
            print('No solution')
    elif (b != 0):
        x = -c / b
        print(f"{x:.2f}")
    elif (c != 0):
        print('No solution')


def main():
    a = float(input())
    b = float(input())
    c = float(input())
    f(a, b, c)


if __name__ == '__main__':
    main()
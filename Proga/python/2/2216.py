def f(petya, vasya, tolya):
    x1, x2, x3 = "", "", ""
    maxim = max(petya, vasya, tolya)
    minim = min(petya, vasya, tolya)
    y1, y2 = maxim, petya + vasya + tolya - maxim - minim
    if petya == y1:
        x1 = "Петя"
    elif petya == y2:
        x2 = "Петя"
    else:
        x3 = "Петя"
    if vasya == y1:
        x1 = "Вася"
    elif vasya == y2:
        x2 = "Вася"
    else:
        x3 = "Вася"
    if tolya == y1:
        x1 = "Толя"
    elif tolya == y2:
        x2 = "Толя"
    else:
        x3 = "Толя"
    print(x1.center(23))
    print(f"   {x2}")
    print(f"{x3:>23}")
    print("    II      I      III")


def main():
    petya = int(input())
    vasya = int(input())
    tolya = int(input())
    f(petya, vasya, tolya)


if __name__ == '__main__':
    main()
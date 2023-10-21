def f(a):
    x1, x2, x3 = a[0], a[1], a[2]
    maxim1 = max(a[0], a[1], a[2])
    minim = min(a[0], a[1], a[2])
    maxim2 = int(x1) + int(x2) + int(x3) - int(maxim1) - int(minim)
    maxim2 = str(maxim2)
    if (minim != "0"):
        print(minim + maxim2, maxim1 + maxim2)
    else:
        print(maxim2 + minim, maxim1 + maxim2)


def main():
    a = input()
    f(a)


if __name__ == '__main__':
    main()
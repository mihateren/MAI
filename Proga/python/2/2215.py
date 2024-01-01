def f(a, b):
    x1, x2, x3, x4 = a[0], a[1], b[0], b[1]
    maxim = max(a[0], a[1], b[0], b[1])
    minim = min(a[0], a[1], b[0], b[1])
    summa = int(x1) + int(x2) + int(x3) + int(x4)
    medium = str((summa - int(maxim) - int(minim)) % 10)
    print(maxim + medium + minim)
    

def main():
    a = input()
    b = input()
    f(a, b)


if __name__ == '__main__':
    main()
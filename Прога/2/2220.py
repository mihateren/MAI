def f(x, y, z):
    a, c = max(x, y, z), min(x, y, z)
    if (x != a) or (x != c):
        b = x
    elif (y != a) and (y != c):
        b = y
    elif (z != a) and (z != c):
        b = z
    if "зайка" in c:
        print(c, len(c))
    elif "зайка" in b:
        print(b, len(b))
    else:
        print(a, len(a))

    
def main():
    x = input()
    y = input()
    z = input()
    f(x, y, z)


if __name__ == '__main__':
    main()
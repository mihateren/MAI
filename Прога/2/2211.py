def f(n):
    x1, x2, x3 = int(n[0]), int(n[1]), int(n[2])
    y1, y2, y3 = max(x1, x2, x3), x1 + x2 + x3 - max(x1, x2, x3) - min(x1, x2, x3), min(x1, x2, x3)
    if y1 + y3 == y2 * 2:
        print("YES")
    else:
        print("NO")


def main():
    n = input()
    f(n)


if __name__ == '__main__':
    main()
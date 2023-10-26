from itertools import product, combinations


def f(s1, s2, last):
    dict = {
        "буби": "бубен",
        "пики": "пик",
        "трефы": "треф",
        "червы": "червей"
    }
    nominal = ['10']
    for i in range(2, 10):
        nominal.append(str(i))
    nominal += ["валет", "дама", "король", "туз"]
    suit = ["бубен", "пик", "треф", "червей"]
    boof = list(combinations(product(nominal, suit), 3))
    s = last.split(", ")
    x, y, z = tuple(s[0].split()), tuple(s[1].split()), tuple(s[2].split())
    flag = False
    for i in range(len(boof)):
        if flag:
            a, b, c = boof[i]
            if ((dict[s1] in a) or (dict[s1] in b) or (dict[s1] in c)) and (s2 not in a) and (s2 not in b) and (s2 not in c):
                print(f"{a[0]} {a[1]}, {b[0]} {b[1]}, {c[0]} {c[1]}")
                break
        if (x == boof[i][0]) and (y == boof[i][1]) and (z == boof[i][2]):
            flag = True


def main():
    s1 = input()
    s2 = input()
    last = input()
    f(s1, s2, last)


if __name__ == '__main__':
    main()
from itertools import product, combinations


def createDeck():
    nominal = ['10']
    for i in range(2, 10):
        nominal.append(str(i))
    nominal += ["валет", "дама", "король", "туз"]
    suit = ["бубен", "пик", "треф", "червей"]
    return nominal, suit


def f(s1, s2):
    dict = {
        "буби": "бубен",
        "пики": "пик",
        "трефы": "треф",
        "червы": "червей"
    }
    nominal, suit = createDeck()
    boof = list(product(nominal, suit))
    k = 0
    for x in combinations(boof, 3):
        if k == 10:
            break
        a, b, c = x
        if ((dict[s1] in a) or (dict[s1] in b) or (dict[s1] in c)) and (s2 not in a) and (s2 not in b) and (s2 not in c):
            print(f"{a[0]} {a[1]}, {b[0]} {b[1]}, {c[0]} {c[1]}")
            k += 1
    

def main():
    s1 = input()
    s2 = input()
    f(s1, s2)


if __name__ == '__main__':
    main()
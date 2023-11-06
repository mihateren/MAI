from itertools import product, permutations


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
    nominal.remove(s2)
    count = 0
    for x in permutations(product(nominal, suit), 3):
        cards = f'{x[0][0]} {x[0][1]}, {x[1][0]} {x[1][1]}, {x[2][0]} {x[2][1]}'
        if dict[s1] in cards:
            print(cards)
            count = count + 1
        if count == 10:
            break
    

def main():
    s1 = input()
    s2 = input()
    f(s1, s2)


if __name__ == '__main__':
    main()
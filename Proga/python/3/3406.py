from itertools import product


def f(s):
    nominal = []
    for i in range(2, 11):
        nominal.append(str(i))
    nominal += ["валет", "дама", "король", "туз"]
    suit = ["пик", "треф", "бубен", "червей"]
    for x, y in list(product(nominal, suit)):
        if y != s:
            print(x, y)
    

def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
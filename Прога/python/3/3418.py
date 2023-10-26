from itertools import product


def f(s):
    print("a b c f")
    for i in product("01", "01", "01"):
        a, b, c = i
        f = eval(s, {'a': a, 'b': b, 'c': c})
        print(a, b, c, int(f))
        

def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
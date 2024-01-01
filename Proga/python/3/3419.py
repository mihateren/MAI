from itertools import product


def f(s):
    all_vars = sorted(set([x for x in s if x.isupper()]))
    print(' '.join(all_vars), 'F')
    for stroka in product(range(0, 2), repeat=len(all_vars)):
        res = {}
        for key, value in zip(all_vars, stroka):
            res[key] = value
        print(' '.join(str(letter) for letter in stroka), int(eval(s, res)))
        

def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
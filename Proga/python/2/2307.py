def f(n, m):
    nok = max(n, m)
    if (nok % n == 0) and (nok % m == 0):
        print(nok)
    else:
        while not ((nok % n == 0) and (nok % m == 0)):
            nok += 1
        print(nok)
    

def main():
    n = int(input())
    m = int(input())
    f(n, m)


if __name__ == '__main__':
    main()
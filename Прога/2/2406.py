def f(n):
    a = int(input())
    flag = True
    nod1 = nod2 = -1
    for i in range(n - 1):
        b = int(input())
        if flag:
            nod2 = nod1 = evklid(a, b)
            flag = False
        else:
            nod2 = evklid(a, b)
        if nod2 == nod1:
            nod1 = nod2
            a = b
    print(nod2)


def evklid(a, b):
    nod = -1
    x, y = a, b
    while x != y:
        x, y = max(x, y), min(x, y)
        x -= y
    nod = x
    return nod        


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
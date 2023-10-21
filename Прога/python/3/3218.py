def f(n):
    d = dict()
    for i in range(n):
        n, m = map(str, input().split())
        n = n[:-1]
        m = m[:-1]
        if (n, m) not in d.keys():
            d[(n, m)] = 1
        else:
            d[(n, m)] += 1
    print(max([i for i in d.values()]))
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
from itertools import islice


def f(n):
    kashi = []
    for i in range(n):
        kashi.append(input())
    days = int(input())
    ans = []
    if days <= n:
        ans += list(islice(kashi, days))
    else:
        ans += kashi * (days // n) + list(islice(kashi, days % n))
    for x in ans:
        print(x)
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
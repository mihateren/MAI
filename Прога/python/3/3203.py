def f(n):
    union = set(map(str, input().split()))
    for i in range(n - 1):
        unionArr = set(map(str, input().split()))
        union = unionArr | union
    for i in union:
        print(i)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
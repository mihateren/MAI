def f(n, m):
    children = set()
    manka = set()
    ovsyanka = set()
    for i in range(n):
        child = input()
        manka.add(child)
        children.add(child)
    for i in range(m):
        child = input()
        ovsyanka.add(child)
        children.add(child)
    res = manka & ovsyanka
    one = children - res
    one = sorted(one)
    if len(one) == 0:
        print("Таких нет")
    else:
        for child in one:
            print(child)


def main():
    n = int(input())
    m = int(input())
    f(n, m)


if __name__ == '__main__':
    main()
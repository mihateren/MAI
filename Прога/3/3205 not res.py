def f(n, m):
    manka = set()
    ovsyanka = set()
    for i in range(n):
        manka.add(input())
    for i in range(m):
        ovsyanka.add(input())
    obe = manka & ovsyanka
    ans = (manka - obe) | (ovsyanka - obe)
    print("Таких нет") if len(ans) == 0 else print(len(ans))
    

def main():
    n = int(input())
    m = int(input())
    f(n, m)


if __name__ == '__main__':
    main()
def f(n, m):
    names = []
    for i in range(n + m):
        names.append(input())
    ans = []
    for x in names:
        if names.count(x) == 1:
            ans.append(x)
    if len(ans) == 0:
        print("Таких нет")
    else:
        for x in sorted(ans):
            print(x)
    

def main():
    n = int(input())
    m = int(input())
    f(n, m)


if __name__ == '__main__':
    main()
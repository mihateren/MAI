def f(n, m):
    names = []
    for i in range(n + m):
        names.append(input())
    ans = 0
    for x in names:
        if names.count(x) == 1:
            ans += 1
    print(ans) if ans > 0 else print("Таких нет")
    

def main():
    n = int(input())
    m = int(input())
    f(n, m)


if __name__ == '__main__':
    main()
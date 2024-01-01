def f(n):
    menu = []
    for i in range(n):
        menu.append(input())
    m = int(input())
    arr = []
    for i in range(m):
        k = int(input())
        for j in range(k):
            arr.append(input())
    ans = []
    for i in range(n):
        if menu[i] not in arr:
            ans.append(menu[i])
    if len(ans) > 0:
        for x in sorted(ans):
            print(x)
    else:
        print("Готовить нечего")


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
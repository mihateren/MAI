def f(n):
    keys = []
    for i in range(n):
        keys.append(input())
    m = int(input())
    menu = {}
    for key in keys:
        menu[key] = 0
    for i in range(m):
        k = int(input())
        for j in range(k):
            s = input()
            menu[s] += 1
    ans = []
    for key, value in menu.items():
        if value == 0:
            ans.append(key)
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
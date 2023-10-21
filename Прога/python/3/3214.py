def f(n):
    keys = []
    for i in range(n):
        keys.append(input())
    menu = []
    m = int(input())
    for i in range(m):
        name = input()
        k = int(input())
        flag = True
        for j in range(k):
            s = input()
            if s not in keys:
                flag = False
        if flag:
            menu.append(name)
    menu.sort()
    if len(menu) == 0:
        print("Готовить нечего")
    else:
        for name in menu:
            print(name)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
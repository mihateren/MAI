def f(n):
    ans = 0
    for i in range(n):
        s = input()
        a = s.split()
        for word in a:
            if word == "зайка":
                ans += 1
    print(ans)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
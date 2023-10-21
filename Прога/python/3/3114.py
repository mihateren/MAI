def f():
    numbers = map(int, input().split())
    p = int(input())
    ans = ""
    for i in numbers:
        ans += str(i ** p) + " "
    print(ans[:-1:])


def main():
    f()


if __name__ == '__main__':
    main()
def f(n):
    letters = ["а", "б", "в"]
    flag = "YES"
    for i in range(n):
        s = input()
        if flag == "YES":
            if s[0] not in letters:
                flag = "NO"
    print(flag)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
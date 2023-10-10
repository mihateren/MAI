def f():
    s = input()
    while s != "":
        ans = ""
        for i in range(len(s)):
            if s[i] != "#":
                ans += s[i]
            else:
                break
        if ans != "":
            print(ans)
        s = input()


def main():
    f()


if __name__ == '__main__':
    main()
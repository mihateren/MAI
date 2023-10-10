def f():
    s = input()
    while s != "":
        if (s[-3:] != "@@@"):
            if (s[0] == "#" and s[1] == "#"): 
                print(s[2:])
            else:
                print(s)
        s = input()


def main():
    f()


if __name__ == '__main__':
    main()
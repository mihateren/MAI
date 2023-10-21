def f(s):
    x1 = "".join(s.lower().split())
    x2 = x1[::-1]
    if x1 == x2:
        print("YES")
    else:
        print("NO")  


def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
def f(s, n):
    x, y = 0, 0
    while s != "СТОП":
        if s == "СЕВЕР":
            y += n
        elif s == "ЮГ":
            y -= n
        elif s == "ЗАПАД":
            x -= n
        elif s == "ВОСТОК":
            x += n
        s = input()
        if s == "СТОП":
            break
        n = int(input())
    print(y)
    print(x)
    

def main():
    s = input()
    n = int(input())
    f(s, n)


if __name__ == '__main__':
    main()
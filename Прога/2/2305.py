def f(n):
    s = 0.0
    while n != 0:
        s += n * 0.9 if (n >= 500) else n
        n = float(input())
    print(s)
    

def main():
    n = float(input())
    f(n)


if __name__ == '__main__':
    main()
def f(n):
    s = 0
    for i in n:
        s += int(i)
    print(s)
    

def main():
    n = input()
    f(n)


if __name__ == '__main__':
    main()
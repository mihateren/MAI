def f(n):
    s = ""
    for i in range(1, n + 1):
        for j in range(i, (n + 1) * i, i):
            s += str(j) + " "
        print(s[:-1])
        s = ""
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
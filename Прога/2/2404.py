def f(n):
    s = 0
    for i in range(n):
        c = input()
        for j in c:
            s += int(j)
    print(s)
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
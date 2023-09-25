def f(n):
    maxC = -1
    maxName = ""
    for i in range(n):
        name = input()
        c = input()
        s = 0
        for j in c:
            s += int(j)
        if s >= maxC:
            maxC = s
            maxName = name
    print(maxName)
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
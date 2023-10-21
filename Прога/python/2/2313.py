def f(n):
    s = input()
    minim = s
    for i in range(n-1):
        s = input()
        minim = s if s < minim else minim
    print(minim)
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
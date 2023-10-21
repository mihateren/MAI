def f(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
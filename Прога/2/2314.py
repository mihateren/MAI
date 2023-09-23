def f(n):
    flag = "YES"
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            flag = "NO"
    if n == 1:
        print("NO")
    else:
        print(flag)
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
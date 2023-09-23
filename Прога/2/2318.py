def f(n):
    ans = ""
    for i in range(2, round(n / 2) + 1):
        while n % i == 0:
            ans += f"{i} * "
            n = int(n / i)
    print(ans[:-2])
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
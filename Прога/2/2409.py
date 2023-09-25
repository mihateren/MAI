def f(n):
    ans = ""
    for i in range(n):
        s = 0
        c = input()
        for j in c:
            s = max(s, int(j))
        ans += str(s)
    print(ans)
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
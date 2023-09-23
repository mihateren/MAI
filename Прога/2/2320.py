def f(n):
    ans = -1
    p = 0
    for i in range(n):
        b = int(input())
        h, r, m = b % 256, (b // 256) % 256, b // 256 ** 2
        t = ((m + r + p) * 37) % 256
        if t != h or h >= 100:
            ans = i
            break
        p = h
    print(ans)
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
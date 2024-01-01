def f(s):
    ans = ""
    for i in s:
        if int(i) % 2 != 0:
            ans += i
    print(ans)
    

def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
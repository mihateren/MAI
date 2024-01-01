def f(s):
    flag = "YES"
    for i in range(round(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            flag = "NO"
            break
    print(flag)
    

def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
def f(n):
    k = 0
    for i in range(n):
        s = ""
        flag = False
        while s != "ВСЁ":
            s = input()
            if (s == "зайка") and (not flag):
                k += 1
                flag = True
    print(k)
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
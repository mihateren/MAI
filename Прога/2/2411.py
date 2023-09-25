def f(n):
    k = 0
    for i in range(n):
        flag = False
        c = int(input())
        if (c != 1):
            for j in range(2, int(c ** 0.5) + 1):
                if (c % j == 0):
                    flag = True
            if not flag:
                k += 1
    print(k)
        

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
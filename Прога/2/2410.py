def f(n):
    print("А Б В")
    for i in range(1, n - 2 + 1):
        for j in range(1, n - 1 + 1):
            for k in range(1, n + 1):
                if (i + j + k == n):
                    print(i, j, k)
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
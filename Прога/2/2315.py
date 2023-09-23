def f(n):
    k = 0
    for i in range(n):
        s = input()
        if "зайка" in s:
            k += 1
    print(k)
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
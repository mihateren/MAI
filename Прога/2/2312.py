def f(n):
    maxim = -1
    for i in n:
        maxim = int(i) if int(i) > maxim else maxim
    print(maxim)
    

def main():
    n = input()
    f(n)


if __name__ == '__main__':
    main()
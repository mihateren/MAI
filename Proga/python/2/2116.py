def f(a, b, c):
    x = (b - a) / c
    print(f"{x:.2f}")
    

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    f(a, b, c)


if __name__ == '__main__':
    main()
def f(a, b, c):
    m1 = max(a, b, c)
    m2 = min(a, b, c)
    m3 = a + b + c - m1 - m2
    cos = round((m3 * m3 + m2 * m2 - m1 * m1) / (2 * m3 * m2), 2)
    if cos == 0:
        print("100%")
    elif cos > 0:
        print("крайне мала")
    else:
        print("велика")
    

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    f(a, b, c)


if __name__ == '__main__':
    main()
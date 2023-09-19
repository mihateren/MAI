def f(n, m, k1, k2):
    # пусть x - вес первой партии, y - второй
    # x + y = n. по сутии имеем уравнение (x+y)m = xk1 + yk2
    # xm+ym=xk1+yk2
    # x(m-k1)=y(k2-m)
    # x + y = n
    # x = n - y
    # (n-y)(m-k1)=y(k2-m)
    # (nm-nk1-ym+yk1)=yk2-ym
    # nm-nk1=yk2-ym-yk1+ym
    # nm-nk1=y(k2-m-k1+m)
    # nm-nk1=y(k2-k1)
    # y = (nm-nk1)/(k2-k1)
    y = (n * m - n * k1) / (k2 - k1)
    x = n - y
    print(int(x), int(y))
    

def main():
    n = int(input())
    m = int(input())
    k1 = int(input())
    k2 = int(input())
    f(n, m, k1, k2)


if __name__ == '__main__':
    main()
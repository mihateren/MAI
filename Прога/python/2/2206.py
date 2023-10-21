def f(year):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print("YES")
    else:
        print("NO") 


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
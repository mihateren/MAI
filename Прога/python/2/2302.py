def f(s):
    i = 0
    while s != "Приехали!":
        if "зайка" in s:
            i += 1
        s = input()
    print(i)
    

def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
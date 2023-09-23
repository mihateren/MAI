def f():
    left = 0
    right = 1000
    mid = (right + left) // 2
    print(mid)
    s = input()
    while s != "Угадал!":
        if s == "Больше":
            left = mid
        if s == "Меньше":
            right = mid
        if s == "Угадал!":
            break
        mid = (right + left) // 2
        print(mid)
        s = input()
    

def main():
    f()


if __name__ == '__main__':
    main()
def f():
    x = input()
    y = input()
    z = input()
    s1, s2, s3 = sorted((x, y, z))
    if "зайка" in s1:
        print(s1, len(s1))
    elif "зайка" in s2:
        print(s2, len(s2))
    elif "зайка" in s3:
        print(s3, len(s3))

    
def main():
    f()


if __name__ == '__main__':
    main()
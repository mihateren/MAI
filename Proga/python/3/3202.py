def f(s1, s2):
    union = set(s1) & set(s2)
    ans = "".join(union)
    print(ans)


def main():
    s1 = input()
    s2 = input()
    f(s1, s2)


if __name__ == '__main__':
    main()
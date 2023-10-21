def f():
    s = input()
    near = set()
    while s != "":
        text = list(map(str, s.split()))
        for i in range(len(text)):
            if text[i] == 'зайка':
                if (i - 1) >= 0:
                    near.add(text[i - 1])
                if (i + 1) <= (len(text) - 1):
                    near.add(text[i + 1])
        s = input()
    for i in near:
        print(i)


def main():
    f()


if __name__ == '__main__':
    main()
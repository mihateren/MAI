def f():
    d = {}
    s = input()
    while s != "":
        text = list(s.split())
        for i in range(len(text)):
            if text[i] not in d.keys():
                d[text[i]] = 1
            else:
                d[text[i]] += 1
        s = input()
    for key, value in d.items():
        print(key, value)


def main():
    f()


if __name__ == '__main__':
    main()
from sys import stdin


def f():
    lines = []
    for line in stdin:
        lines += line.rstrip("\n").split()
    s = 0
    for x in lines:
        s += int(x)
    print(s)


def main():
    f()


if __name__ == '__main__':
    main()
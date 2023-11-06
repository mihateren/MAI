from sys import stdin


def f():
    k = 0
    s = 0
    for line in stdin:
        line = line.rstrip("\n").split()
        dif = int(line[2]) - int(line[1])
        k += 1
        s += dif
    print(round(s / k))


def main():
    f()


if __name__ == '__main__':
    main()
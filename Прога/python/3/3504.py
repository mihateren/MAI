from sys import stdin


def f():
    lines = []
    for line in stdin:
        lines.append(line.rstrip("\n"))
        request = line.rstrip("\n")
    for i in range(len(lines) - 1):
        if request.upper() in lines[i].upper():
            print(lines[i].rstrip("\n"))


def main():
    f()


if __name__ == '__main__':
    main()
from sys import stdin


def f():
    for line in stdin:
        if not line.startswith("#"):
            print(line[:line.find("#")])


def main():
    f()


if __name__ == "__main__":
    main()

def f(file1, n):
    with open(file1) as file_in:
        lines = file_in.readlines()
    k = len(lines) - n
    for i in range(k, len(lines)):
        print(lines[i], end="")


def main():
    file = input()
    n = int(input())
    f(file, n)


if __name__ == "__main__":
    main()

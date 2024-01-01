def f(file1, file2, file_ans):
    set1 = set()
    set2 = set()
    with open(file1) as file_in:
        for line in file_in:
            boof = set(line.split())
            set1 = set1 | boof
    with open(file2) as file_in:
        for line in file_in:
            boof = set(line.split())
            set2 = set2 | boof
    ans = sorted(list(set1 ^ set2))
    with open(file_ans, "w", encoding="UTF-8") as file_out:
        for x in ans:
            file_out.write(x + "\n")


def main():
    file1 = input()
    file2 = input()
    file_ans = input()
    f(file1, file2, file_ans)


if __name__ == "__main__":
    main()

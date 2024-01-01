import json
from sys import stdin


def f(file):
    with open(file, encoding="UTF-8") as f:
        records = json.load(f)
    d = {}
    for line in stdin:
        arr = line.rstrip("\n").split(" == ")
        d[arr[0]] = arr[1]
    records.update(d)
    with open(file, "w", encoding="UTF-8") as file_out:
        json.dump(records, file_out, ensure_ascii=False, indent=2)


def main():
    file = input()
    f(file)


if __name__ == "__main__":
    main()
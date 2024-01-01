import json


def f(file1, file2):
    numbers = []
    with open(file1) as file_in:
        for line in file_in:
            numbers += list(map(int, line.split()))
    positive = 0
    for x in numbers:
        if x > 0:
            positive += 1
    records = {"count": len(numbers),
               "positive_count": positive,
               "min": min(numbers),
               "max": max(numbers),
               "sum": sum(numbers),
               "average": "%.2f" % (sum(numbers) / len(numbers))}
    with open(file2, "w", encoding="UTF-8") as file_out:
        json.dump(records, file_out, ensure_ascii=False, indent=2)


def main():
    file1 = input()
    file2 = input()
    f(file1, file2)


if __name__ == "__main__":
    main()
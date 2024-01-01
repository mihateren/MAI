def f(s):
    numbers = []
    with open(s) as file_in:
        for line in file_in:
            numbers += list(map(int, line.split()))
    positive = 0
    for x in numbers:
        if x > 0:
            positive += 1
    print(len(numbers))
    print(positive)
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))
    print("%.2f" % (sum(numbers) / len(numbers)))


def main():
    s = input()
    f(s)


if __name__ == "__main__":
    main()

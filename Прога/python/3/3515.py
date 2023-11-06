import json
from sys import stdin


def f():
    with open("scoring.json", encoding="UTF-8") as file:
        records = json.load(file)
    userAnswers = []
    for line in stdin:
        userAnswers.append(line.rstrip("\n"))
    score = 0
    for i in range(len(userAnswers)):
        for d in records:
            price = d["points"]
            for x in d["tests"]:
                if userAnswers[i] == x["pattern"]:
                    score += price // len(d["tests"])
    print(score)


def main():
    f()


if __name__ == "__main__":
    main()
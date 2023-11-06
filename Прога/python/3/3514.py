import json
from sys import stdin


def f(file1, file2):
    with open(file1, encoding="UTF-8") as users:
        usersRec = json.load(users)
    with open(file2, encoding="UTF-8") as updates:
        updatesRec = json.load(updates)
    d = {}
    for x in usersRec:
        for key, value in x.items():
            if key == "name":
                d[value] = {}
                name = value
            else:
                d[name][key] = value
    for x in updatesRec:
        for key, value in x.items():
            if key == "name":
                name = value
                if (value not in d.keys()):
                    d[value] = {}
            if key != "name":
                if key not in d[name].keys():
                    d[name][key] = value
                elif value > d[name][key]:
                    d[name][key] = value
    with open(file1, "w", encoding="UTF-8") as file_out:
        json.dump(d, file_out, ensure_ascii=False, indent=4)


def main():
    file1 = input()
    file2 = input()
    f(file1, file2)


if __name__ == "__main__":
    main()
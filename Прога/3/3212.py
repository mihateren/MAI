def f(n):
    people = []
    for i in range(n):
        people.append(input())
    ans = 0
    namesakes = {}
    for i in set(people):
        counter = 0
        for name in people:
            if name == i:
                counter += 1
        if counter > 1:
            ans += counter
            namesakes[i] = counter
    if ans == 0:
        print("Однофамильцев нет")
    else:
        namesakes = dict(sorted(namesakes.items()))
        for key, value in namesakes.items():
            print(f"{key} - {value}")


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
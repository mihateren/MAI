def f(n):
    people = []
    for i in range(n):
        people.append(input())
    ans = 0
    for i in set(people):
        counter = 0
        for name in people:
            if name == i:
                counter += 1
        if counter > 1:
            ans += counter
    print(ans)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
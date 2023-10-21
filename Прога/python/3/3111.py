def f(n):
    results = []
    for i in range(n):
        results.append(input())
    request = input()
    for res in results:
        if request.lower() in res.lower():
            print(res)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
def f(n):
    arr = []
    for i in range(n):
        boofer = list(input().split())
        for j in range(len(boofer)):
            if boofer[j][-1] != ":":
                arr.append(boofer[j])
    arr2 = []
    for x in arr:
        if x[-1] == ",":
            arr2.append(x[:-1:])
        else:
            arr2.append(x)
    print(arr2)
    ans = []
    for x in sorted(arr2):
        ans.append(x)
    for x in ans:
        print(x)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
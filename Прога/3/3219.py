def f(n):
    arr = []
    for i in range(n):
        boofer = set(input().split())
        for x in boofer:
            if x[-1] == ",":
                arr.append(x[:-1:])
            elif x[-1] != ":":
                arr.append(x)
    ans = []
    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            ans.append(arr[i])
    for x in sorted(ans):
        if x[-1] == ",":
            print(x[:-1:])
        else:
            print(x)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
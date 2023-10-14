def f(n):
    arr = []
    for i in range(n):
        arr.append(list(input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            xi, yi = arr[i][0], arr[i][1]
            xj, yj = arr[j][0], arr[j][1]
            if (len(xi) == len(xj)) and (len(xi) == 2) and (len(yi) == len(yj)) and (len(yi) == 2):
                if (xi[0] == xj[0]) and (xi[1] != xj[1]) and (yi[0] == yj[0]) and (yi[1] != yj[1]):
                    ans += 1
    print(ans)


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
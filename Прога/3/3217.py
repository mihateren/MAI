def f():
    arr = []
    s = input()
    while s != "":
        arr.append(s.split())
        s = input()
    man = set()
    for i in range(len(arr)):
        for j in range(2):
            man.add(arr[i][j])
    d = {}
    for x in man:
        fr1 = g(x, arr)
        fr2 = set()
        for y in fr1:
            ans = g(y, arr)
            for f in ans:
                fr2 = fr2 | set(ans)
        d[x] = []
        for i in fr2:
            if (i != x) and (i not in fr1):
                d[x].append(i)
    d = dict(sorted(d.items()))
    for key, value in d.items():
        print(key + ":", ", ".join(sorted(value)))


def g(name, arr):
    ans = []
    for i in range(len(arr)):
        if name == arr[i][0]:
            ans.append(arr[i][1])
        elif name == arr[i][1]:
            ans.append(arr[i][0])
    return ans     


def main():
    f()


if __name__ == '__main__':
    main()
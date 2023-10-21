def f(n):
    d = {}
    for i in range(n):
        arr = list(input().split())
        name = arr[0]
        for i in range(1, len(arr)):
            if not arr[i] in d.keys():
                d[arr[i]] = [name]
            else:
                d[arr[i]].append(name) 
    kasha = input()
    if kasha in d.keys():
        for x in sorted(d[kasha]):
            print(x)
    else:
        print("Таких нет")
    

def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
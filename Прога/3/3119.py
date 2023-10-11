def f(s):
    arr = list(map(str, s.split()))
    op = "*-+"
    numberOfCalc = 0
    operators = 0
    for i in range(len(arr)):
        if not arr[i].isdigit():
            operators += 1
    while numberOfCalc != operators:
        for i in range(len(arr)):
            if str(arr[i]) in op:
                x = int(arr[i - 1])
                arr.pop(i - 1)
                y = int(arr[i - 2])
                if arr[i - 1] == "*":
                    arr[i - 2] = y * x
                elif arr[i - 1] == "+":
                    arr[i - 2] = y + x
                elif arr[i - 1] == "-":
                    arr[i - 2] = y - x
                arr.pop(i - 1)
                numberOfCalc += 1
                break
    print(arr[0])


def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
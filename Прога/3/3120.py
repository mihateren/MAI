def f(s):
    arr = list(map(str, s.split()))
    op = "*-+/~!#@"
    stack = []
    x, y, z = 0, 0, 0
    for i in range(len(arr)):
        if not str(arr[i]) in op:
            stack.append(int(arr[i]))
        else:
            lastIndex = len(stack) - 1
            if arr[i] == "*":
                x = int(stack[lastIndex - 1])
                y = int(stack[lastIndex])
                stack.pop(lastIndex)
                stack[lastIndex - 1] = x * y
            elif arr[i] == "+":
                x = int(stack[lastIndex - 1])
                y = int(stack[lastIndex])
                stack.pop(lastIndex)
                stack[lastIndex - 1] = x + y
            elif arr[i] == "-":
                x = int(stack[lastIndex - 1])
                y = int(stack[lastIndex])
                stack.pop(lastIndex)
                stack[lastIndex - 1] = x - y
            elif arr[i] == "/":
                x = int(stack[lastIndex - 1])
                y = int(stack[lastIndex])
                stack.pop(lastIndex)
                stack[lastIndex - 1] = x // y
            elif arr[i] == "~":
                y = int(stack[lastIndex])
                stack[lastIndex] = -y
            elif arr[i] == "!":
                y = stack[lastIndex]
                fact = 1
                for j in range(1, y + 1):
                    fact *= j
                stack[lastIndex] = fact
            elif arr[i] == "#":
                y = stack[lastIndex]
                stack.append(y)
            elif arr[i] == "@":
                x = int(stack[lastIndex])
                y = int(stack[lastIndex - 1])
                z = int(stack[lastIndex - 2])
                stack[lastIndex] = z
                stack[lastIndex - 1] = x
                stack[lastIndex - 2] = y
    print(stack[0])


def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
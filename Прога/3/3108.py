def f(n):
    for i in range(n):
        s = input()
        a = s.split()
        zaikaPos = 0
        currentPos = 1
        for j in range(len(a)):
            word = a[j]
            if (word == "зайка") and (zaikaPos == 0):
                zaikaPos = currentPos + j
            currentPos += len(word)
        if zaikaPos != 0:
            print(zaikaPos)
        else:
            print("Заек нет =(")


def main():
    n = int(input())
    f(n)


if __name__ == '__main__':
    main()
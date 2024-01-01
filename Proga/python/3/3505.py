from sys import stdin


def f():
    words = []
    for line in stdin:
        for x in line.rstrip("\n").split():
            if (x.upper() == x[::-1].upper()):
                flag = True
                for i in range(len(words)):
                    if x == words[i]:
                        flag = False
                if flag:
                    words.append(x)
    for x in sorted(words):
        print(x)



def main():
    f()


if __name__ == '__main__':
    main()
from sys import stdin


def mySplit(s):
    k, t = 0, 0
    boof = ""
    for i in range(len(s)):
        if s[i] == " " or s[i] == "\t" or s[i] == "\n":
            if s[i] == "\t":
                t += 1
            k += 1
            if boof != "" and k == 1 and t != k:
                boof += " "
        else:
            boof += s[i]
            k = 0
            t = 0
    return boof


def f():
    req = input()
    files = []
    for file in stdin:
        files.append(file.rstrip("\n"))
    validFiles = []
    for file in files:
        flag = True
        with open(file) as file_in:
            boof = mySplit(file_in.read())
            for word in req.split():
                if word.lower() not in boof.lower():
                    flag = False
                    break
        if flag:
            validFiles.append(file)
    if len(validFiles) > 0:
        [print(i) for i in validFiles]
    else:
        print("404. Not Found")
            

def main():
    f()


if __name__ == "__main__":
    main()

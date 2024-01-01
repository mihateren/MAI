def f(file1, file2):
    with open(file1) as file_in:
        for line in file_in:
            k = 0
            t = 0
            boof = ""
            for i in range(len(line)):
                if line[i] == " " or line[i] == "\t" or line[i] == "\n":
                    if line[i] == "\t":
                        t += 1
                    k += 1
                    if boof != "" and k == 1 and t != k:
                        boof += " "
                else:
                    boof += line[i]
                    k = 0
                    t = 0
            if boof != "":
                with open(file2, "a", encoding="UTF-8") as file_out:
                    file_out.write(boof + "\n")


def main():
    file1 = input()
    file2 = input()
    f(file1, file2)


if __name__ == "__main__":
    main()

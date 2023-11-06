def f(file1, file2, file3, file4):
    file_out2 = open(file2, "w", encoding="UTF-8")
    file_out3 = open(file3, "w", encoding="UTF-8")
    file_out4 = open(file4, "w", encoding="UTF-8")
    with open(file1) as file_in:
        for line in file_in:
            numbers = []
            numbers += list(map(int, line.split()))
            evenStr, oddStr, eqStr = "", "", ""
            for x in numbers:
                even, odd = 0, 0
                t = x
                while t > 0:
                    if (t % 10) % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                    t //= 10
                if even > odd:
                    evenStr += str(x) + " "
                elif odd > even:
                    oddStr += str(x) + " "
                else:
                    eqStr += str(x) + " "
            file_out2.write(evenStr + "\r")
            file_out3.write(oddStr + "\r")
            file_out4.write(eqStr + "\r")
    file_out2.close()
    file_out3.close()
    file_out4.close()


def main():
    file1 = input()
    file2 = input()
    file3 = input()
    file4 = input()
    f(file1, file2, file3, file4)


if __name__ == "__main__":
    main()
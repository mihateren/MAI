def f():
    shift = int(input())
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open("public.txt") as file_in:
        s = file_in.read().rstrip("\n")
    ans = ""
    for i in s:
        if i.isalpha():
            newInd = (alph.find(i.upper()) + shift) % len(alph)
            if alph[alph.find(i)] == i:
                ans += alph[newInd]
            else:
                ans += alph[newInd].lower()
        else:
            ans += i
    with open("private.txt", "w", encoding="UTF-8") as file_out:
        file_out.write(ans)


def main():
    f()


if __name__ == "__main__":
    main()

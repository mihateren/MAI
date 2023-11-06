def f():
    with open("secret.txt") as file_in:
        s = file_in.read().rstrip("\n")
    ans = ""
    for i in s:
        ans += chr(ord(i) % 128)
    print(ans)


def main():
    f()


if __name__ == "__main__":
    main()

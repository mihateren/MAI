def f():
    with open("numbers.num", "rb") as file_in:
        s = file_in.read()
    ans = 0
    for i in range(0, len(s), 2):
        hex = s[i:i + 2]
        ans += int.from_bytes(hex, "big") % 2 ** 16
    print(ans)
    

def main():
    f()


if __name__ == "__main__":
    main()

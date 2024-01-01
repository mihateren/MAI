def f():
    with open("numbers.num", "rb") as file_in:
        s = file_in.read()
    hexSum = sum([int.from_bytes(s[i:i + 2], "big") for i in range(0, len(s), 2)])
    print(hexSum % (4 ** 8))
    

def main():
    f()


if __name__ == "__main__":
    main()

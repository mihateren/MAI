def f(s):
    while s != "Три!":
        print("Режим ожидания...")
        s = input()
    print("Ёлочка, гори!")
    

def main():
    s = input()
    f(s)


if __name__ == '__main__':
    main()
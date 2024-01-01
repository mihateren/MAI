from os import path
from math import ceil


def f():
    file = input()
    size = path.getsize(file)
    unit = ""
    if size < 1024:
        unit = "Б"
    elif size < 1024**2:
        unit = "КБ"
        size = ceil(size / 1024)
    elif size < 1024**3:
        unit = "МБ"
        size = ceil(size / 1024 ** 2)
    else:
        unit = "ГБ"
        size = ceil(size / 1024 ** 3)
    print(str(size) + unit)


def main():
    f()


if __name__ == "__main__":
    main()

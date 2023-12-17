numbers = []


def proizv(numbers):
    n = 1
    for i in numbers:
        n *= i
    return n


def add_number(number):
    numbers.append(number)


def get_prod():
    s = ""
    for x in numbers:
        s += str(x) + " * "
    s = s[:-2]
    s += "= " + str(proizv(numbers))
    return s
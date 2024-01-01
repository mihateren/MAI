numbers = []


def add_number(number):
    numbers.append(number)


def get_sum():
    s = ""
    for x in numbers:
        s += str(x) + " + "
    s = s[:-2]
    s += "= " + str(sum(numbers))
    return s


add_number(1)
add_number(2)
add_number(3)
print(get_sum())
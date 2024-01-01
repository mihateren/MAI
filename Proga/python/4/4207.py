numbers = []


def enter_results(*keys):
    global numbers
    numbers += keys


def get_sum():
    sum1, sum2 = 0, 0
    for i in range(len(numbers)):
        sum1 += numbers[i] * (i % 2 != 0)
        sum2 += numbers[i] * (i % 2 == 0)
    return (round(sum2, 2), round(sum1, 2))


def get_average():
    av1, av2 = round(get_sum()[0] / (len(numbers) / 2), 2), round(get_sum()[1] / (len(numbers) / 2), 2)
    return av1, av2



enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
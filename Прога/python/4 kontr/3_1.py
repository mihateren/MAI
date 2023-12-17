from itertools import combinations


def count_pairs(*numbers, div=10):
    count = 0
    for x in combinations(numbers, 2):
        if (sum(x) % div == 0):
            count += 1
    return count

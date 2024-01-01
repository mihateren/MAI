from itertools import combinations


def multiple_sum(*numbers, div=2):
    maxSum = -1
    terms = 2
    while terms != len(numbers) + 1:
        for x in combinations(numbers, terms):
            if (sum(x) > maxSum) and (sum(x) % div == 0):
                maxSum = sum(x)
        terms += 1
    return maxSum


numbers = [10, 5, 2, 3, 4] 
print(multiple_sum(*numbers, div=5))


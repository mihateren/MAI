from itertools import product


n = int(input())
arr = []
for i in range(n):
    arr.append(set())
    s = input().split("-")
    for letter in s:
        arr[i].add(letter)
    arr[i] = sorted(list(arr[i]))
for x in product(*arr):
    for y in x:
        print(y, end='')
    print()


# from itertools import product

# n = int(input())
# letters = []
# for i in range(n):
#     letters.append(set())
#     for letter in input().split(sep='-'):
#         letters[i].add(letter)
#     letters[i] = sorted(list(letters[i]))
# for comb in product(*letters):
#     for letter in comb:
#         print(letter, end='')
#     print()
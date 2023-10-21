children = int(input())
toys_all = []
for i in range(children):
    information = input().split(': ')
    toys = information[1]
    toys_all.extend(set(toys.split(', ')))
toys_all.sort()
for x in toys_all:
    if toys_all.count(x) == 1:
        print(x)
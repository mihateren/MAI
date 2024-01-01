ints = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1]
print([x for x in [i for i in ints if (abs(i) % 10 > 3)] + [j for j in ints if (abs(j) % 10 <= 3)]])
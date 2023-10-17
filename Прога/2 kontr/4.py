n = int(input())
x = int(input())
maxim = -10000000000000000000000000
for i in range(n - 1):
    y = int(input())
    if (y < x) and (y > maxim):
        maxim = y
    x = y
print(maxim)
n = int(input())
maxim = -1000000000000000
for i in range(n):
    s = input()
    summa = 0
    k = 0
    while s != "next":
        summa += int(s)
        k += 1
        s = input()
    sr = summa / k
    if sr > maxim:
        maxim = sr
print("%.2f" % maxim)

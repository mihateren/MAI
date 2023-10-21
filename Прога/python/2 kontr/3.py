m = int(input())
n = int(input())
s = ""
for i in range(n, m + 1, (n - m) % 10):
    s += str(i) + ", "
print(s[:-2:])
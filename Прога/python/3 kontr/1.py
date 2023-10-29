n = int(input())
for i in range(n):
    s = input().split(sep='%')
    print(s[1][int(s[0])::-3][:int(s[-1])][::-1])
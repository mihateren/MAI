import gc

a = []

i = 0
s = '1'
a.append(id(s))
while i not in a:
    s = '1'
    i = id(s)
    a.append(id(s))
    print(a)
    i = 0
    del(s)
    gc.collect()
print('ura')
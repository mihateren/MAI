dict = {}
s = input()
while s != "":
    boof = s.split()
    for x in boof:
        if len(x) not in dict.keys():
            dict[len(x)] = [x.upper()]
        elif x.upper() not in dict[len(x)]:
            dict[len(x)].append(x.upper())
    s = input()
for key, value in dict.items():
    i = "; ".join(reversed(sorted(value)))
    print(f"{key}: {i.upper()}")
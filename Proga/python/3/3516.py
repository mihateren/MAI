from sys import stdin

data = [line.strip() for line in stdin]
query = data[0].lower()
D = {}
for file in data[1:]:
    with open(file, "r", encoding="UTF-8") as f:
        D[file] = f.read()
        if query in ' '.join(D[file].replace('&nbsp;', ' ').lower().split()):
            print(file)
        else:
            del D[file]
if not D:
    print('404. Not Found')
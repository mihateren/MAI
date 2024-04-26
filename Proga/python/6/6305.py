from requests import get
from sys import stdin


server = 'http://' + input()
ways = [i.strip() for i in stdin]
ans = 0
for x in ways:
    ans += sum(get(server + x).json())
print(ans)
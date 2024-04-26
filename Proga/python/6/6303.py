from requests import get

server = 'http://' + input()
response = get(server).json()
summ = 0
for x in response:
    if isinstance(x, int):
        summ += x
print(summ)

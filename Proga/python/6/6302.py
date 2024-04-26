from requests import get

server = 'http://' + input()
result = 0
response = get(server)
while response.text != '0':
    result += int(response.text)
    response = get(server)
print(result)

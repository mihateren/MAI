from requests import get


server = 'http://' + input()
result = 0
response = get(server).content
while response.content != '0':
    result += int(response.content)
    response = get(server).content
print(result)

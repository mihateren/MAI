from requests import get

server = 'http://' + input()
response = get(server).json()
key = input()
print(response.get(key, "No data"))
from requests import get
from sys import stdin

server = 'http://' + input()
userId = input()
msg = ''.join(i for i in stdin)
try:
    response = get(server + "/users/" + userId).json()
except ValueError:
    print("Пользователь не найден")
if response:
    for key in response:
        msg = msg.replace('{' + key + '}', str(response[key]))
    print(msg)

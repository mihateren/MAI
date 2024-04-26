from requests import get

server = 'http://' + input()
response = get(server + "/users")
users = []
for user in response.json():
    users.append(user["last_name"] + ' ' + user["first_name"])
users = sorted(users)
for user in users:
    print(user)

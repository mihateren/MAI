from requests import post
from json import dumps


server = 'http://' + input() + '/users'
dataFrame = {}
dataFrame["username"] = input()
dataFrame["last_name"] = input()
dataFrame["first_name"] = input()
dataFrame["email"] = input()
post(server, data=dumps(dataFrame))

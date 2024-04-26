from requests import put
from json import dumps
from sys import stdin


server = 'http://' + input() + '/users/' + input()
replaces = [i.strip().split('=') for i in stdin]
dataFrame = {}
for x in replaces:
    dataFrame[x[0]] = x[1]
put(server, data=dumps(dataFrame))

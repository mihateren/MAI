from requests import delete

server = 'http://' + input() + '/users/' + input()
delete(server)
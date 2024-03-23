class Checkers:
    def __init__(self):
        self.desk = {
            'A': {
                '8': 'X',
                '7': 'B',
                '6': 'X',
                '5': 'X',
                '4': 'X',
                '3': 'W',
                '2': 'X',
                '1': 'W',
            },
            'B': {
                '8': 'B',
                '7': 'X',
                '6': 'B',
                '5': 'X',
                '4': 'X',
                '3': 'X',
                '2': 'W',
                '1': 'X',
            },
            'C': {
                '8': 'X',
                '7': 'B',
                '6': 'X',
                '5': 'X',
                '4': 'X',
                '3': 'W',
                '2': 'X',
                '1': 'W',
            },
            'D': {
                '8': 'B',
                '7': 'X',
                '6': 'B',
                '5': 'X',
                '4': 'X',
                '3': 'X',
                '2': 'W',
                '1': 'X',
            },
            'E': {
                '8': 'X',
                '7': 'B',
                '6': 'X',
                '5': 'X',
                '4': 'X',
                '3': 'W',
                '2': 'X',
                '1': 'W',
            },
            'F': {
                '8': 'B',
                '7': 'X',
                '6': 'B',
                '5': 'X',
                '4': 'X',
                '3': 'X',
                '2': 'W',
                '1': 'X',
            },
            'G': {
                '8': 'X',
                '7': 'B',
                '6': 'X',
                '5': 'X',
                '4': 'X',
                '3': 'W',
                '2': 'X',
                '1': 'W',
            },
            'H': {
                '8': 'B',
                '7': 'X',
                '6': 'B',
                '5': 'X',
                '4': 'X',
                '3': 'X',
                '2': 'W',
                '1': 'X',
            },
        }

    def move(self, f, t):
        self.desk[f[0]][f[1]], self.desk[t[0]][t[1]] = self.desk[t[0]][t[1]], self.desk[f[0]][f[1]]

    def get_cell(self, p):
        return Cell(self.desk[p[0]][p[1]])
    

class Cell:
    def __init__(self, coords):
        self.coords = coords

    def status(self):
        return self.coords
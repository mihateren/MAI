class Rectangle:
    def __init__(self, a, b):
        self.width = abs(a[0] - b[0])
        self.height = abs(a[1] - b[1])
        self.S = 0
        self.P = 0
    
    def area(self):
        self.S = self.width * self.height
        return round(self.S, 2)
    
    def perimeter(self):
        self.P = 2 * self.width + 2 * self.height
        return round(self.P, 2)

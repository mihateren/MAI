class Rectangle:
    def __init__(self, a, b):
        self.upper_left_x = round(min(a[0], b[0]), 2)
        self.upper_left_y = round(max(a[1], b[1]), 2)
        self.lower_right_x = round(max(a[0], b[0]), 2)
        self.lower_right_y = round(min(a[1], b[1]), 2)
        self.width = abs(self.lower_right_x - self.upper_left_x)
        self.height = abs(self.upper_left_y - self.lower_right_y)
        self.S = 0
        self.P = 0
        self.flag = False

    def area(self):
        self.S = self.width * self.height
        return round(self.S, 2)
    
    def perimeter(self):
        self.P = 2 * self.width + 2 * self.height
        return round(self.P, 2)
    
    def get_pos(self):
        return (round(self.upper_left_x, 2), round(self.upper_left_y, 2))
    
    def get_size(self):
        if self.flag:
            return (round(self.width, 2), round(self.height, 2))
        return ((round(abs(self.upper_left_x - self.lower_right_x), 2), 
                 round(abs(self.upper_left_y - self.lower_right_y), 2)))
    
    def move(self, dx, dy):
        self.upper_left_x += dx
        self.upper_left_y += dy
        self.lower_right_x += dx
        self.lower_right_y += dy

    def resize(self, new_width, new_height):
        self.flag = False
        self.lower_right_x = self.upper_left_x + new_width 
        self.lower_right_y = self.upper_left_y - new_height
        self.width = abs(self.lower_right_x - self.upper_left_x)
        self.height = abs(self.upper_left_y - self.lower_right_y)

    def turn(self):
        self.flag = False
        d = (self.width - self.height) / 2
        self.lower_right_x = round(self.lower_right_x - d, 2)
        self.lower_right_y = round(self.lower_right_y - d, 2)
        self.upper_left_x = round(self.upper_left_x + d, 2)
        self.upper_left_y = round(self.upper_left_y + d, 2)
        self.width, self.height = self.height, self.width
    
    def scale(self, factor):
        self.flag = False
        width, height = self.get_size()
        self.flag = False
        if abs(width - self.width) <= 0.01:
            width = self.width
        if abs(height - self.height) <= 0.02:
            height = self.height
        self.upper_left_x = round(self.upper_left_x - (factor * width - width) / 2, 2)
        self.upper_left_y = round(self.upper_left_y + (factor * height - height) / 2, 2)
        width = round(width * factor, 2)
        height = round(height * factor, 2)
        self.lower_right_x = round(self.upper_left_x + width, 2)
        self.lower_right_y = round(self.upper_left_y - height, 2)
        self.width = round(self.width * factor, 2)
        self.height = round(self.height * factor, 2)
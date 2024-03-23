class Stack:
    def __init__(self):
        self.top = 0
        self.data = [0]
    
    def push(self, item):
        self.data.append(item)
        self.top += 1
    
    def pop(self):
        self.top -= 1
        return self.data.pop()

    def is_empty(self):
        return self.top == 0

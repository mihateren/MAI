class Queue():
    def __init__(self):
        self.start = 0
        self.data = []
        self.length = 0
    
    def push(self, item):
        self.data.append(item)
        self.length += 1
    
    def pop(self):
        k = self.data[self.start]
        self.length -= 1
        self.start += 1
        return k

    def is_empty(self):
        return self.length == 0

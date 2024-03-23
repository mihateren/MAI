class RedButton:
    def __init__(self):
        self.clicked = 0

    def click(self):
        self.clicked += 1
        print("Тревога!")

    def count(self):
        return self.clicked

    
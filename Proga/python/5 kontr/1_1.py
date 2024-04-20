class Comment:
    def __init__(self, name, date, text):
        self.author = name
        self.date, self.time = date.split()
        self.text = text

    def get_author(self):
        return self.author
    
    def get_date(self):
        return self.date
    
    def get_time(self):
        return self.time
    
    def get_text(self):
        return self.text
    

# a = Comment('Вася', '23-02-2023 12:43', 'первый')
# print(a.get_author())
# print(a.get_date())
# print(a.get_time())
# print(a.get_text())
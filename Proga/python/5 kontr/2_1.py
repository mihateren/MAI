class Comment:
    def __init__(self, name, date, text):
        self.author = name
        self.date, self.time = date.split()
        self.text = text
        self.approved = False
        self.edited = False

    def get_author(self):
        return self.author

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_text(self):
        return self.text

    def approve(self):
        self.approved = True

    def is_approved(self):
        return self.approved

    def set_text(self, newText):
        self.text = newText
        self.approved = False
        self.edited = True

    def is_edited(self):
        return self.edited

    def __str__(self):
        return f"{self.text}\n" f"[{self.author} ({self.date} {self.time})]\n"


# a = Comment('Вася', '23-02-2023 12:43', 'первый')
# print(a)
# print(a.is_approved(), a.is_edited())
# a.approve()
# a.set_text('Первый!!!')
# print(a.is_approved(), a.is_edited())
# a.approve()
# print(a.is_approved(), a.is_edited())
# print(a)

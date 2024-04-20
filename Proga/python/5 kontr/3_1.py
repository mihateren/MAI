class Comment:
    def __init__(self, name, date, text):
        self.author = name
        self.date, self.time = date.split()
        self.text = text
        self.approved = False
        self.edited = False
        self.childs = []

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

    def get_sub_comments(self):
        return self.childs

    def __iadd__(self, sub_comment):
        sub_comment.parent = self
        self.childs.append(sub_comment)
        return self

    def __lt__(self, other):
        return other in self.childs or any(other in comment.get_sub_comments() for comment in self.childs)

    def __gt__(self, other):
        return self in other.childs or any(self in comment.get_sub_comments() for comment in other.childs)

    def __repr__(self):
        return f"Comment({self.author}, {self.date}, {self.time})"


class SubComment(Comment):
    def __init__(self, name, date, text, parent=None):
        super().__init__(name, date, text)
        self.parent = parent
        if parent:
            parent += self

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        if self.parent:
            self.parent.childs.remove(self)
        parent += self

    def __repr__(self):
        return f"SubComment({self.author}, {self.date}, {self.time}, {self.parent.__repr__()})"


# a = Comment('Вася', '23-02-2023 12:43', 'первый')
# print(repr(a))
# b = SubComment('Миша', '23-02-2023 12:44', 'второй', parent=a)
# print(a.get_sub_comments())
# print(a < b, a > b, b < a, b > a)
# c = SubComment('Петя', '23-02-2023 12:54', 'третий')
# print(repr(c))
# b += c
# print(a < b, a < c, b < c, c > a)
# print(repr(c))
# c.set_parent(a)
# print(a < b, a < c, b < c, c > a)
# print(*map(repr, a.get_sub_comments()), sep='\n')

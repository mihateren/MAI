class ParentTypeError(TypeError):
    pass


class ParentRecursionError(RecursionError):
    pass


class Comment:
    def __init__(self, name, date, text):
        if not isinstance(name, str) or not isinstance(date, str) or not isinstance(text, str):
            raise TypeError
        if date[1] == '02' and date[0] > '29':
            raise ValueError
        if date[1] > '12' or date[0] > '31':
            raise ValueError

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
        if self > sub_comment:
            raise ParentRecursionError
        if not isinstance(sub_comment.parent, Comment) or (isinstance(sub_comment.parent, SubComment) and sub_comment.parent == None):
            raise ParentTypeError
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


try:
    a = Comment(123, 123, 123)
except TypeError:
    print('TypeError raised')

try:
    a = SubComment('user', 'hello', 'hello')
except ValueError:
    print('ValueError raised')

try:
    a = SubComment('first', '01-05-2023 00:00', 'hello')
    b = SubComment('second', '01-05-2023 00:00', 'hello', parent=a)
    a.set_parent(b)
except ParentRecursionError:
    print('ParentRecursionError raised')

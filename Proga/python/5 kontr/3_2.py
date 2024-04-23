class File:
    def __init__(self, name, date, content):
        self.name = name
        self.date, self.time = date.split()
        self.content = content
        self.published = False
        self.edited = False
        self.parent = None
        self.childs = []

    def get_name(self):
        return self.name

    def get_creation_datetime(self):
        return f"{self.date} {self.time}"

    def get_content(self):
        return self.content

    def publish(self):
        self.published = True

    def is_published(self):
        return self.published

    def edit(self, newContent):
        self.content = newContent
        self.edited = True
        self.published = False

    def is_edited(self):
        return self.edited

    def __str__(self):
        return f"[{self.name} ({self.date} {self.time})]\n{self.content}\n"

    def extract(self):
        if self.parent:
            self.parent.childs.remove(self)
        self.parent = None

    def __lt__(self, file):
        return not (self in file.childs or any(file in arch.get_files() for arch in self.childs))

    def __gt__(self, file):
        return not (file in self.childs or any(file in self.get_files() for arch in file.childs))

    def __repr__(self):
        return f"File({self.name}, {self.date} {self.time}, {self.parent.__repr__()})"


class ZipFile(File):
    def __init__(self, name, date, content=""):
        super().__init__(name, date, content)
        self.childs = []

    def wrap(self, file):
        self.childs.append(file)
        file.parent = self

    def get_files(self):
        return self.childs

    def __ilshift__(self, file):
        if isinstance(self, ZipFile):
            self.wrap(file)
            return self

    def __repr__(self):
        return f"ZipFile({self.name}, {self.date} {self.time})"


a = File('hello.txt', '01-06-2023 12:03', 'Hello, world!')
print(repr(a))
b = ZipFile('hello.zip', '02-06-2023 10:50')
b <<= a
c = File('hello2.txt', '02-06-2023 10:53', 'Привет, мир!')
b.wrap(c)
print(b.get_files())
a.extract()
print(b.get_files())
print(repr(b))
d = ZipFile('hello2.zip', '02-06-2023 11:07')
d <<= b
print(c < d, c > d, d < c, d > c)
d.wrap(c)
print(b.get_files(), d.get_files())
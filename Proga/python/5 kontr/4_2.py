class FileTypeError(TypeError):
    pass


class FileRecursionError(RecursionError):
    pass


class File():
    def __init__(self, name, creation_datetime, contents):
        if (not isinstance(name, str)) or (not isinstance(creation_datetime, str)) or (not isinstance(contents, str)):
            raise TypeError
        if creation_datetime[1] == '02' and creation_datetime[0] > '29':
            raise ValueError
        if creation_datetime[1] > '12' or creation_datetime[0] > '31':
            raise ValueError
        self.name = name
        self.creation_datetime = creation_datetime
        self.content = contents
        self.public = False
        self.edited = False
        self.zip = None

    def get_name(self):
        return self.name

    def get_creation_datetime(self):
        return self.creation_datetime

    def get_content(self):
        return self.content

    def publish(self):
        self.public = True

    def is_published(self):
        return self.public

    def edit(self, content):
        self.content = content
        self.edited = True
        self.public = False

    def is_edited(self):
        return self.edited

    def extract(self):
        if self.zip is not None:
            self.zip.files.remove(self)
        else:
            pass

    def __lt__(self, file):
        return not (self in file.files or any(file in arch.get_files() for arch in self.files))

    def __gt__(self, file):
        return not (file in self.files or any(file in self.get_files() for arch in file.files))

    def __repr__(self):
        return f"File({self.name}, {self.creation_datetime}, {repr(self.zip)})"

    def __str__(self):
        return f"[{self.name} ({self.creation_datetime})]\n{self.content}\n"


class ZipFile(File):
    def __init__(self, name, creation_datetime, contents=''):
        super().__init__(name, creation_datetime, contents)
        self.files = []

    def wrap(self, file):
        if not isinstance(file, File) or not isinstance(file, ZipFile):
            raise FileTypeError
        if self < self:
            raise FileRecursionError
        self.files.append(file)
        file.extract()
        file.zip = self

    def __ilshift__(self, other):
        self.wrap(other)
        return self

    def get_files(self):
        return self.files

    def __repr__(self):
        return f"ZipFile({self.name}, {self.creation_datetime})"
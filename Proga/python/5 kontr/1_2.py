class File:
    def __init__(self, name, date, content):
        self.name = name
        self.date, self.time = date.split()
        self.content = content

    def get_name(self):
        return self.name

    def get_creation_datetime(self):
        return f"{self.date} {self.time}"

    def get_content(self):
        return self.content

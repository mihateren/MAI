class File:
    def __init__(self, name, date, content):
        self.name = name
        self.date, self.time = date.split()
        self.content = content
        self.published = False
        self.edited = False

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
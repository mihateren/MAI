class User:
    def __init__(self, name, birth, info):
        self.name = name
        self.birth = birth
        self.info = info
        self.confirmed = False
        self.updated = False

    def get_login(self):
        return self.name

    def get_birth(self):
        return self.birth

    def get_info(self):
        return self.info

    def confirm(self):
        self.confirmed = True

    def is_confirmed(self):
        return self.confirmed

    def edit_info(self, newInfo):
        self.info = newInfo
        self.updated = True

    def is_updated(self):
        return self.updated

    def __str__(self):
        return f"{self.name} ({self.birth}): \n" f"{self.info} \n"

    

# a = User('vasya', '09-04-1983', 'Люблю читать')
# print(a.is_confirmed(), a.is_updated())
# print(a.get_info())
# a.confirm()
# a.edit_info(a.get_info() + ' и компьютерные игры')
# print(a)
# print(a.is_confirmed(), a.is_updated())


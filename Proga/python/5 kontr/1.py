class User:
    def __init__(self, name, birth, info):
        self.name = name
        self.birth = birth
        self.info = info

    def get_login(self):
        return self.name

    def get_birth(self):
        return self.birth

    def get_info(self):
        return self.info


# a = User('vasya', '09-04-1983', 'Люблю читать')
# print(a.is_confirmed(), a.is_updated())
# print(a.get_info())
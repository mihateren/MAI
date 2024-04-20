class UserTypeError(TypeError):
    pass


class UserRecursionError(RecursionError):
    pass


class User:
    def __init__(self, name, birth, info):
        if not isinstance(name, str) or not isinstance(birth, str) or not isinstance(info, str):
            raise TypeError
        date = birth.split('-')
        if date[1] == '02' and date[0] > '29':
            raise ValueError
        if date[1] > '12' or date[0] > '31':
            raise ValueError
        if not isinstance(self, User) or not isinstance(self, StaffUser):
            raise UserTypeError
        self.name = name
        self.birth = birth
        self.info = info
        self.confirmed = False
        self.updated = False
        self.staff = None

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

    def get_staff(self):
        return self.staff

    def __rshift__(self, user):
        if not isinstance(user, StaffUser):
            raise UserTypeError
        if self < user:
            raise UserRecursionError
        user.add_ward(self)

    def __gt__(self, user):
        if self.staff:
            return self in user.wards or any(user in ward.get_wards() for ward in self.wards)
        return False

    def __lt__(self, user):
        return user in self.wards or any(user in ward.get_wards() for ward in self.wards)

    def __repr__(self):
        if self.staff:
            return f"User({self.name}, {self.birth}, {self.staff.__repr__()})"
        else:
            return f"User({self.name}, {self.birth})"


class StaffUser(User):
    def __init__(self, name, birth):
        super().__init__(name, birth, "Staff User")
        self.wards = []

    def add_ward(self, user):
        if user not in self.wards:
            oldStaff = user.staff
            if oldStaff:
                oldStaff.wards.remove(user)
            self.wards.append(user)
            user.staff = self

    def get_wards(self):
        return self.wards

    def __repr__(self):
        return f"StaffUser({self.name}, {self.birth})"


# try:
#     a = User(123, '01-01-1970', 'test')
# except TypeError:
#     print('TypeError raised')
# try:
#     a = StaffUser('Admin', '45-13-2001')
# except ValueError:
#     print('ValueError raised')
# try:
#     a = StaffUser('vasya', '09-04-1983')
#     b = StaffUser('misha', '05-06-1991')
#     c = StaffUser('vanya', '19-02-1995')
#     a >> b
#     b >> c
#     c >> a
# except UserRecursionError:
#     print('UserRecursionError raised')

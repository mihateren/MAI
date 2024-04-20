class User:
    def __init__(self, name, birth, info):
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
        user.add_ward(self)

    def __gt__(self, user):
        if self.staff:
            return self in user.wards or any(
                user in ward.get_wards() for ward in self.wards
            )
        return False

    def __lt__(self, user):
        return user in self.wards or any(
            user in ward.get_wards() for ward in self.wards
        )

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


# a = User('vasya', '09-04-1983', 'Люблю читать')
# b = StaffUser('misha', '05-06-1991')
# b.add_ward(a)
# print(repr(a))
# print(repr(b))
# print(a < b, a > b, b < a, b > a)
# c = StaffUser('vanya', '19-02-1995')
# a >> c
# print(a > b, a > c)
# c >> b
# print(a > b, a > c, c > b)
# print(repr(a))

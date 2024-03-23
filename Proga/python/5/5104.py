class Programmer:
    def __init__(self, name, status="Junior"):
        self.name = name
        self.status = status
        self.time = 0
        self.money = 0
        self.premio = 0
        if self.status == "Junior":
            self.rate = 10
        elif self.status == "Middle":
            self.rate = 15
        elif self.status == "Senior":
            self.rate = 20

    def work(self, time):
        self.time += time
        self.money += time * (self.rate + self.premio)

    def rise(self):
        if self.status == "Junior":
            self.status = "Middle"
            self.rate += 5
        elif self.status == "Middle":
            self.status = "Senior"
            self.rate += 5
        elif self.status == "Senior":
            self.premio += 1
    
    def info(self):
        return f"{self.name} {self.time}ч. {self.money}тгр."
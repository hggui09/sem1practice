class Student:
    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group
    def get_Info(self):
        return f"Имя: {self.name}\nВозраст: {self.age}\nГруппа: {self.group}"

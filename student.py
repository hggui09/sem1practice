class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_Info(self):
        return f"Имя: {self.name}\nВозраст: {self.age}"
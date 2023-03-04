'''
Определите класс Person. При создании объекта
p = Person('Иванов','Михаил','Федорович')

При печати должно выводится перевернутое полное имя.

'''

class Person:
    def __init__(self, name, surname, fathername):
        self.name = name
        self.surname = surname
        self.fathername = fathername

    def __repr__(self):
        s = f'{self.name}{self.surname}{self.fathername}'
        return s[::-1]




p = Person('Иванов','Михаил','Федорович')
print(p)

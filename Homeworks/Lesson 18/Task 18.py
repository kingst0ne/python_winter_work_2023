'''
Разработать систему учета решения задач учениками курса
Разработчик на Python

Проблема. Преподаватель каждый урок задает некоторое кол-во
задач в качестве домашнего задания
Каждый ученик решает каждую задачу. Переводит ее статус в
решенную
Преподаватель проверяет каждую задачу каждого ученика и либо
подтверждает ее статус как решенную, либо меняет ее статус на
нерешенную.
Вопрос. Как спроектировать систему классов на Питоне для решения задачи
учета.
Разработайте систему классов (Teacher, Pupil, Lesson, Task)
Разработайте систему атрибутов для каждого состояния каждого
объекта.
'''
import time
import random


class Course:
    def __init__(self,*info):
        self.info = list(info)

class Teacher:
    def __init__(self):
        self.work = 0
    def teach(self,info,*pupil):
        pass
    def check(self):
        time.sleep(2)
        if random.randint(0,1) == 1:
            return 'GOOD'
        else:
            return 'BAD'
    def set_homework(self, *pupil, theme):
        for i in pupil:
            i.homework_to_do(theme)
    def check_homework(self, *pupil):
        for i in pupil:
            if i.homework.check_status() == 'CHECKING':
                if self.check() == 'GOOD':
                    i.homework.upgrade_status()
                else: i.homework.degrade_status()
            else:
                return 'Homework not done'



class Pupil:
    def __init__(self):
        self.study_ = None
    def homework_to_do(self, task):
        self.homework = Homework(task)
        self.homework.set_status(0)
    def study(self):
        self.homework.upgrade_status()



class Homework:
    def __init__(self, task):
        self.name = task
        self.status = 0
    def set_status(self, i):
        self.status = i
    def upgrade_status(self):
        self.status += 1
    def degrade_status(self):
        self.status -= 1
    def check_status(self):
        if self.status == 0:
            return 'TODO'
        elif self.status == 1:
            return 'CHECKING'
        elif self.status ==2:
            return 'DONE'
        else: raise ValueError('Incorrect status!')


Nikolay = Teacher()
Vasya = Pupil()
Petya = Pupil()



Nikolay.set_homework(Vasya, Petya, theme= 'OOP')

print(Vasya.homework.check_status())
print(Petya.homework.check_status())
Vasya.study()
Petya.study()
print(Vasya.homework.check_status())
print(Petya.homework.check_status())

Nikolay.check_homework(Vasya, Petya)
print(Vasya.homework.check_status())
print(Petya.homework.check_status())


pass




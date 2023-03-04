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
    def __init__(self, name):
        self.name = name
    def teach(self,info,*pupil):
        pass
    def check(self):
        time.sleep(1)
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
                    i.homework.status_done()
                else: i.homework.status_incorrect()
            else:
                print(f'Homework from {i} is not done!')



class Pupil:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'{self.name}'
    def homework_to_do(self, task):
        self.homework = Homework(task)

    def send_hw_to_check(self, teacher):
        teacher.check_homework(self)

    def study(self):
        self.homework.status_checking()



class Homework:
    def __init__(self, task):
        self.name = task
        self.status_list = ['TODO', 'CHECKING', 'INCORRECT', 'DONE']
        self.status = self.status_list[0]
    def status_new(self):
        self.status = self.status_list[0]
    def status_checking(self):
        self.status = self.status_list[1]
    def status_incorrect(self):
        self.status = self.status_list[2]
    def status_done(self):
        self.status = self.status_list[3]
    def check_status(self):
        return self.status


Nikolay = Teacher('Nikolay')
Vasya = Pupil('Vasya')
Petya = Pupil('Petya')



Nikolay.set_homework(Vasya, Petya, theme= 'OOP')

print(Vasya.homework.check_status())
print(Petya.homework.check_status())
Vasya.study()
print(Vasya.homework.check_status())
Vasya.send_hw_to_check(Nikolay)
# Petya.study()
print(Vasya.homework.check_status())
print(Petya.homework.check_status())
#
# Nikolay.check_homework(Vasya, Petya)
# print(Vasya.homework.check_status())
# print(Petya.homework.check_status())


pass




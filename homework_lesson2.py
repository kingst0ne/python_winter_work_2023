#Задание 2-1
#Введите число n. Напечатайте "таблицу умножения" на число n

n = int(input('Введите число n для вывода таблицы умножения:\n'))
for i in range(1,n+1):
    print(f'{i} X {n} = {n*i}')

#Задание 2-2
#Введите список lst, состоящий из чисел
# Найдите и напечатйате наименьшее число из списка lst
# В Python есть функция min, которая решает эту задачу.
# Но напишите свою программу, которая не использует min

from random import randint
lst = [randint(-50,50) for i in range(20)] #Для создания листа с разными рандомы числами для проверки программы,
# наполним лист рандомными числами от -50, до 50 в кол-ве 20 штук, при помощи библиотеки random

minim = lst[0] #Обозначаю первое число минимальным, в теле цикла - сравниваю другия числа с ним
for i in lst:
    if i < minim: minim = i #Если число меньше минимального, обновляю значения минимума

print(*lst,'\nМинимальное число:\t', minim) #Печатаю лист, и значение минимального.


#Задание 2-3.
# Введите число n.
# Сосчитайте и напечатаейте факториал числа n!

n = int(input('Введите число для нахождения факториала:'))
mult = 1 #Переменная для хранения произведения
for i in range(1,n+1):
    mult *= i

print(f'Факториал {n}: {mult}')








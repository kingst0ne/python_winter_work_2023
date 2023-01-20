#Задачи 1-4 и 1-5
#import random

#Задачи 1-4 и 1-5. Ввести два числа x и y
#Найти наибольшее из 5 чисел (x+y, x*y, x-y, x/y, x//y), и вывести его на экран
#Найти второе во величине число из этих чисел, вывести на экран

#ВВодим числа
x = int(input('Введите х\n'))
y = int(input('Введите y\n'))

#Выполним проверку на 0:

if y == 0:
    print('Деление на 0! Выберете другой у')
    y = int(input())


num1 = x+y
num2 = x*y
num3 = x-y
num4 = x/y
num5 = x//y

#Вывод чисел на экран, для дальнейшего анализа
print('Получившиеся числа:',num1,num2,num3,num4,num5)


#При нахождении маскимального числа, заменяем его на любое другое, таким образом
#исключая его из поиска при поиске 2-ого наибольшего
print('Наибольшее число:')
if (num1 >= num2) and (num1 >= num3) and (num1 >= num4) and (num1 >= num5):
    print (num1)
    num1 = num5
elif (num2 >= num1) and (num2 >= num3) and (num2 >=num4) and (num2 >= num5):
    print (num2)
    num2 = num5
elif (num3 >= num1) and (num3 >= num2) and (num3 >=num4) and (num3 >= num5):
    print (num3)
    num3 = num5
elif (num4 >= num1) and (num4 >= num2) and (num4 >=num3) and (num4 >= num5):
    print (num4)
    num4 = num5
else:
    print (num5)
    num5 = num4

#Повторяем поиск максимального, только теперь максимальное число

print('Второе наибольшее число:')
if (num1 >= num2) and (num1 >= num3) and (num1 >= num4) and (num1 >= num5):
    print (num1)
elif (num2 >= num1) and (num2 >= num3) and (num2 >=num4) and (num2 >= num5):
    print (num2)
elif (num3 >= num1) and (num3 >= num2) and (num3 >=num4) and (num3 >= num5):
    print (num3)
elif (num4 >= num1) and (num4 >= num2) and (num4 >=num3) and (num4 >= num5):
    print (num4)
else:
    print (num5)





# Здесь закоментирована часть кода, которая была использована при проверке правильности кода
# for i in range(40):
#     x = random.randint(-10,10)
#     y = random.randint(-10,10)
#
#     # x = int(input())
#     # y = int(input())
#     if y == 0:
#         print('Деление на ноль!')
#         continue
#
#     num1 = x+y
#     num2 = x*y
#     num3 = x-y
#     num4 = x/y
#     num5 = x//y
#
#     print(num1,num2,num3,num4,num5)
#
#     print('Первое максимальное число:')
#     if (num1 >= num2) and (num1 >= num3) and (num1 >= num4) and (num1 >= num5):
#         print (num1)
#         num1 = num5
#     elif (num2 >= num1) and (num2 >= num3) and (num2 >=num4) and (num2 >= num5):
#         print (num2)
#         num2 = num5
#     elif (num3 >= num1) and (num3 >= num2) and (num3 >=num4) and (num3 >= num5):
#         print (num3)
#         num3 = num5
#     elif (num4 >= num1) and (num4 >= num2) and (num4 >=num3) and (num4 >= num5):
#         print (num4)
#         num4 = num5
#     else:
#         print (num5)
#         num5 = num4
#
#     print('Второе максимальное число:')
#     if (num1 >= num2) and (num1 >= num3) and (num1 >= num4) and (num1 >= num5):
#         print (num1)
#     elif (num2 >= num1) and (num2 >= num3) and (num2 >=num4) and (num2 >= num5):
#         print (num2)
#     elif (num3 >= num1) and (num3 >= num2) and (num3 >=num4) and (num3 >= num5):
#         print (num3)
#     elif (num4 >= num1) and (num4 >= num2) and (num4 >=num3) and (num4 >= num5):
#         print (num4)
#     else:
#         print (num5)

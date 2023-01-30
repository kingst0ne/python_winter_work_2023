#задача 4-1
'''
Ввод - 2 слова разделенных пробелами
для ввода используется функция s = input().split()
Определить, являются ли эти слова анаграммами(слова с одинаковым набором букв)
Если да - True, если нет - False

# '''

# dct = {}
# line = input().split()
# for num, word in enumerate(line):
#     dct[num] = {}
#     for letter in word:
#         if letter not in dct[num]:
#             dct[num][letter] = 0
#         dct[num][letter]+=1
#
# if dct[0] == dct[1]:
#     print(True)
# else: print(False)

'''
задание 4-1
Напишите калькулятор (простой)
На вход подается строка: 1 + 2 или 5 - 1 или 6 / 3 или 3 * 4
Вывод: сосчитать и напечатать результат операции
Гарантируется что оба операнда и операция есть в каждой строчке и разделены пробелом
'''
#
# dct = {}
# dct['num']=[]
# st = input('Введите выражение:').split()
# for i in st:
#     if i.isdigit():
#         dct['num'].append(int(i))
#     else:
#         dct['oper'] = i
# if dct['oper'] == '+':
#     print(sum(dct['num']))
# elif dct['oper'] == '-':
#     print(dct['num'][0] - dct['num'][1])
# elif dct['oper'] == '*':
#     print(dct['num'][0] * dct['num'][1])
# elif dct['oper'] == '/':
#     print(dct['num'][0] / dct['num'][1])
# else:
#     print('Unknown operation')

'''
Задача 4-2 
Вводим натуральное число n
Напечатайте спираль из чисел 1,2,3...n*n
Например для числа n = 4:
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
Пока не выполнено
'''
#
# d= {}
# n = 4
# x = 0
# y = 0
# k = 0
# for i in range(n*n):
#     if (x,y) not in d.keys() and y < n-1:
#         d[x, y] = i
#         y += 1
#     elif y == n-1 and (x,y) not in d.keys():
#         d[x, y] = i
#         x+=1
#     elif x == n-1 and (x,y) not in d.keys():
#         d[x, y] = i
#         y -=1
#     else:
#         d[x, y] = i
#         x -=1
#
#
#
#     #Растем
#     #print(d)
#     k = k + 1
#
#
# print('\n')
# print(d)

'''
Задача 4-3
Ввод 2 предложения, содержащие пробелы, знаки препинания
Определить, являются ли предложения анаграммами.
Если да, то True, если нет, то False
'''

dct = {}
line1 = input('Введите предложение 1')
line2 = input('Введите предложение 2')
line = line1
for i in range(2):
    dct[i]={}
    for letter in line:
        if letter.isalpha():
            if letter not in dct[i]:
                dct[i][letter] = 0
            dct[i][letter]+=1
    line = line2


if dct[0] == dct[1]:
    print(True)
else: print(False)
pass


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
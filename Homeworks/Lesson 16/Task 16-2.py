'''
Вводится двухзначное число, например 45
Напишите такой шаблон, чтобы функция re:findall находила только
положительные числа, которые не больше, чем это число

'''


import re

s = '40 12 4 1 100 300 400 -400 -3000 40 145 146 54 145'
num = int(input('Введите число:'))
res2 = ''
for i in str(num):
    if i == '0':
        res2+='[0-9]?'
    else: res2 += '[0-'+i+']?'
res2 = "\\b"+res2[:-1]+"\\b|"+"\\b\s"+res2[:-1]+"\\b"


print(re.findall(fr'{res2}', s))

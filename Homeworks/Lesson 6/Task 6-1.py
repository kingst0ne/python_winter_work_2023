'''
Написать функцию, которая переводит строку из римских цифр в десятичное число
Римские цифры:
I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000, IV = 4, IX = 9, XC = 90,
XL = 40, CD = 400, CM = 900

Например:
MMXXIII = 2023
MDCCCLXII = 1862

'''

def rim_to_10number(s):
    number = 0
    dct = {'I' : 1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000, 'IV' : 4, 'IX' : 9, 'XC' : 90,
'XL' : 40, 'CD' : 400, 'CM' : 900}
    i = 0
    while True:
        if i == len(s)-1:
            number += dct[s[i]]
            break
        elif (s[i]+s[i+1]) in dct:
            number += dct[s[i]+s[i+1]]
            i += 2
        elif s[i] in dct:
            number += dct[s[i]]
            i+=1
        else:
            print('Incorrect number', end='')
            return ' '
    return number


print(rim_to_10number('MMXXIII'))#2023
print(rim_to_10number('MDCCCLXII'))#1862
print(rim_to_10number('MCMLXI'))#1961
print(rim_to_10number('MDCCLXI'))#1761
print(rim_to_10number('MDUCCLXI'))#Incorrect number


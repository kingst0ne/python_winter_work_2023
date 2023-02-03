'''
Напишите программу, которая расчитывает НОК для списка натуральных чисел
'''
import math

def nok(lst):
    if len(lst) == 1: return 'Одно число'
    nok = 1
    for i in lst:
        nok = int(nok * i / math.gcd(nok,i))
    return nok

print(nok([94, 67,8, 5,2]))

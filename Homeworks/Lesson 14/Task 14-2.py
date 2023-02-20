'''
Напишите рекурсивную функцию, которая вычисляет сумму цифр
натурального числа
'''

summa = 0


def num_sum(n):
    #Базовый случай
    if n%10 == n:
        return n
    #Рекурсивный случай
    else: return n%10 + num_sum(n//10)

print(num_sum(1000000001000001))
print(num_sum(123456789))
print(num_sum(1))
print(num_sum(0))
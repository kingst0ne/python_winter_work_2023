'''
Напишите рекурсивную функцию, которая вычисляет кол-во
цифр введенного натурального числа
'''

def len_req(s):
    # Базовый случай
    if s % 10 == s:
        return 1
    # Рекурсивный случай
    else:
        return 1 + len_req(s // 10)

print(len_req(1000000001000001))
print(len_req(123456789))
print(len_req(1))
print(len_req(0))
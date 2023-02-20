'''
Создайте функцию-генератор, который принимает в качестве аргумента список целых чисел,
а в качестве результатов формирует последовательность
нечетных чисел из этого списка
'''

def odd_numbers(lst):
    for i in lst:
        if i%2:
            print('До yield')
            yield i
            print('После yield')

gen = odd_numbers(lst= [1,2,3,4,5,6,7,8,9,10])

while True:
    try:
        print('До next')
        print(next(gen))
        print('После next')
    except StopIteration:
        print('Список закончен')
        break





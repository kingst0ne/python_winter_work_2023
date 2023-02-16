'''
Создайте функцию - генератор, которая создает бесконечную последовательность
1 -2 3 -4 5 -6...
'''

def infinite_cycle():
    i = 0
    while True:
        i += 1
        yield i if i%2 else -i

g = infinite_cycle()

for i in range(6):
    print(next(g))

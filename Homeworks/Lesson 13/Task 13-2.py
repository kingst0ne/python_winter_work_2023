'''
Содзайте функцию генератор, которая создает последовательность числовых палиндромов:
1 2 3 4 5 6 7 8 9
11 22 33 44 55 66 77 88 99
101 111 121 131 141 151 161 171 181 191
'''

def polyndrom_generator():
    chislo = 0
    while True:
        chislo += 1
        if str(chislo) == str(chislo)[::-1]:
            yield chislo

gen = polyndrom_generator()

for i in range(30):
    print(next(gen))


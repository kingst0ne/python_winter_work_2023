'''
Task 5-2.
Ввести число. Напечатать все его делители.
Например: 12
Вывод:
1 2 3 4 6 12
'''

number = int(input('введите число:'))
dividers = []
for i in range(1, number//2 + 1):
    if number%i == 0:
        dividers.append(i)
if dividers == [1]:
    dividers.append(number)
print(*dividers)

'''
Напечатать только его простые делители
'''
dct = {}
init_number = number
for i in range(2, (number//2)+1):
    ammount = 1
    while number%i == 0:
        dct[i] = ammount
        ammount +=1
        number /= i
    if number == 1:
        break
if dct == {}:
    dct[number] = 1

s = f'{init_number} = '
for i in dct:
    s+=f'({i} ** {dct[i]})*'
print(s[:-1])


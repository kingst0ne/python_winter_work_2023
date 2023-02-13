'''
Напишите функцию которая переводит арабские числа в римские
'''

dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XC': 90,
       'XL': 40, 'CD': 400, 'CM': 900}


def droblenue(number, key, drob, s):
    s += key * (int(number)//drob)
    number = int(number)%drob
    return number, s


def num_to_rim(number):
    s = ''
    for key,val in sorted(dct.items(), key= lambda x:-x[1]):
        number,s = droblenue(number, key, val, s)
    return s



print(num_to_rim(2022))
print(num_to_rim(1893))
print(num_to_rim(309))
print(num_to_rim(402))
print(num_to_rim(60))
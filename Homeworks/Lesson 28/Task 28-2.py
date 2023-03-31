'''
Напишите функцию, результатом которой является расстояние
Хемминга двух строк одинаковой длины, равное кол-ву
несовпадающих букв на одинаковых позициях

abc и abc = 0
abc и abd = 1
abc и xyz = 3
'''

#fun = (lambda s: )
# str1 = 'abc'
# str2 = 'abd'
# str1 = 'abc'
# str2 = 'abc'
str1 = 'abc'
str2 = 'xyz'


print(sum(list(map(lambda x: 0 if x[0] == x[1] else 1, [(str1[x], str2[x]) for x in range(len(str1))]))))


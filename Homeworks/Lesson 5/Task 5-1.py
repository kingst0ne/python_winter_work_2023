'''
Задача 5 - 1.
Ввести число n.
Напечатать треуголльник Паскаля.

1
11
121
1331
14641

и т.д., вплоть до n
'''

n = int(input('Введите n:'))
dct = {}
for i in range(1, n+1):
    dct[i] = []
    for j in range(1,i+1):
        if j == 1 or j == i:
            dct[i].append(1)
        else:
            dct[i].append(dct[i-1][j-2] + dct[i-1][j-1])

for i in range(1,n+1):
    print(' '.join(str(j) for j in dct[i]))
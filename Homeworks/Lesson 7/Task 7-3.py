'''
Дан X - двумерный массив в виде списка содержащего строки в виде списков
Размер массива n-строк и m-столбцов

Напишите функцию, которая принимает этот массив как аргумент и в качестве результата выдает отсортированный
список 3-х самых больших чисел

Пример:
n=2
m=3
x = [[1,6,3],[4,5,4]]
Результат: [4,5,6]
'''
import math
x = [[1,6,3],[4,5,4],[20,4,5],[80,75,3]]


#Это мой вариант, достаточно топорный
def lst_max(lst):
    lst_max = []
    for i in range(3):
        maxim = -math.inf
        for mass in lst:
            if max(mass)>maxim and max(mass) not in lst_max:
                maxim = max(mass)
                index1,index2 = lst.index(mass),mass.index(maxim)

        lst_max.append(maxim)
        lst[index1][index2] = -math.inf
    return(sorted(lst_max))

#Вариант, который я нашел на просторах, более лакончиный

def lst_max_notmine(x):
    lst_max = []
    for i in range(3):
        m = max(x, key=max) # ищем по самому маленькому значению
        i = x.index(m)      # берём индекс по ряду
        j = m.index(max(m)) # берём индекс по колонке
        lst_max.append(x[i][j])
        x[i][j] = -math.inf

    return (sorted(lst_max))




print(lst_max_notmine(x))
print(lst_max(x))
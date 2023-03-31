'''
Дан список чисел А. Назовем пару чисел а[i], a[j] - инверсией,
если а[i] > a[j].

Напишите ф-ию, которая возвращает кол-во инверсий в списке.
например: [1,2,3,4,5] -> 0
[5,4,3,2,1] -> 10
'''

def inverstion_count(lst):
    count = 0

    for num,val in enumerate(lst):
        for num2, val2 in enumerate(lst):
            if val > val2 and num < num2:
                count +=1

    return count


#lst = [5,4,3,2,1]
lst = [1,2,3,4,5]
print(inverstion_count(lst))
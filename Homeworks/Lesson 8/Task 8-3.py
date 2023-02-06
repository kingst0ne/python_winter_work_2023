'''
Дан список слов. Отсортируйте его по количеству уникальных букв
в каждом слове в обратном порядке. Если уникальных букв одинаковое кол-во - в алфавитном порядке

'''

lst = ['ababa', 'xx', 'asdnsad','aaaaa','Aoioianiuina', 'xyy', 'abb','aab']

print(sorted(lst, key=lambda x: (-len(set(x.lower())), x.lower())))
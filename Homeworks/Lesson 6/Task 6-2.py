'''
программа получает на вход 2 строки, с перечислением книг, которые прочитали 2 ученика
Выводит количество книг, которые прочитали оба ученика

'''

def books_in_common(s1,s2):
    tes1 = set(s1.split())
    tes2 = set(s2.split())
    return len(tes1.intersection(tes2))


str1 = 'njnefcioj eiiim fiooj book1 book2'
str2 = 'nhebnrioch pirje pfhu book1 book2'

print(books_in_common(str1, str2))


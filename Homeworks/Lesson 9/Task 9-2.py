'''
Похожие слова - программа, определяет, являются ли слова похожими.
Похожими слова считаются, если его гласные буквы находятся там же, где и в первом слове.
Например, слова дорога и пароход - похожи
ввод - первое слово, например, питон

n - количество слов для сравнения, например 6
Дальше вводятся 6 слов

Вывод: слова, похожие на питон

'''

def vowels_pos(word):
    lst = []
    vowels = 'ауоыиэяюеё'
    for pos,letter in enumerate(word):
        if letter in vowels:
            lst.append(pos)
    return lst

def similarity_check(word1):
    n = int(input('Введите количество слов для сравнения'))
    lst = []
    for w in range(n):
        s = input(f'Слово {w + 1}')
        if vowels_pos(word1) == vowels_pos(s):
            lst.append(s)
    return ''.join(lst)



print(similarity_check(input('Введите слово для сравнения:')))


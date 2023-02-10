'''
Произвести частотный анализ текста из файла
Сосчитать сколько раз встречается каждый символ в тексте(буквы, цифры, и служебные символы),
не учитывая регистр
Отсортровать по убыванию и напечатать первые 10 символов и их частоты
При равенстве частот отсортировать символы в алфавитном порядке

'''
import collections
s = ''
f = open('test.txt','r', encoding='utf-8')
for line in f:
    s+=line.split('\n')[0]
f.close()

dct = collections.Counter(s.lower())

# Первый вариант, через обычный дикт
# dct = {}
# for i in s.lower():
#     if dct.get(i):
#         dct[i] += 1
#     else:
#         dct[i] = 1

srt_lst = sorted(list(dct.items()), key=lambda x:(-x[1],x[0]))

for i in range(len(srt_lst)):
    print(srt_lst[i][0],'-',srt_lst[i][1])
    if i > 8:
        break






#import this
import keyword


# name = input('Как тебя зовут?')
# # print(name)
# surname = input('Как твоя фамилия?')
# # print(surname)
# print(f"Привет, {name} {surname}")
#
# # print(f"Привет, {s}")
# # x = int(input("Сколько тебе лет?"))
# # print(f"Мне {x} лет")
#
# name1 = input('Имя1')
# name2 = input('Имя2')
# name3 = input('Имя3')
# print(f"{name3}:{name2}:{name1}")

#print(keyword.kwlist)

# x = int(input('chislo'))
# if x > 0:
#     print('positive')
# elif x == 0:
#     print('null')
# else:
#     print('negative')

#
# x = input()
# y = input()
# if x>y: print(x)
# else: print(y)
#
# x = int(input())
# y = int(input())
# print(x+y, x*y)
#
# x = int(input())
# y = int(input())
#
# #На дом - найти наибольшее из 5 чисел, и вывести его на экран, 2 задача - найти 2 по
# num1 = x+y
# num2 = x*y
# num3 = x**y
# num4 = x/y
# num5 = x//y
#
# print(num1,num2,num3,num4,num5)

#if num1 > num2

#Занятие 2

#for i in "Hello world":
    #print(i)

# #print(1,2,3, sep='_')
# print(1,2,3,end='\n\n')
# print()
# print(1,2,3,4)
#
# print(help())
#
# for i in "Hello world":
#     print(i,end='  ')
#     # print(i,sep='_')
#     # print(i,sep='\n')


# print(len(range(1,10,3)))
# for i in range(0,10,3):
#     print(i)

# print(list(range(5))) #этот вариант лучше т.к. не ест память
# x = [0,1,2,3,4]
# print(x)
#
# print(list(range(5,-5,-2)))
# print(list(range(5,-5)))

# for i in range(10):
#     print(i,i*i) #лучше писать через умножение, т.к это быстрее
#
# for i in range(10):
#     if i%2 == 0:
#         print(i,'четное')
#     else:
#         print(i,'нечетное')

#FizzBuzz

# x = int(input())
# мое решение, не очень красивое
# for i in range(1, x+1):
#     if i%3 == 0:
#         if i%5 == 0:
#             print('FizzBuzz')
#         else:
#             print('Fizz')
#     elif i%5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# #более красивое решение
# for i in range(1, x+1):
#     if i%15 == 0:
#         print('FizzBuzz')
#     elif i%3 == 0:
#         print('Fizz')
#     elif i%5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# for i in 'hello world':
#     if i =='o':
#         break
#     print(i*2, end='')

# for i in 'hello world':
#     if i =='o':
#         continue
#     print(i*2, end='')
#
# for i in 'hello world':
#     if i =='a':
#         break
# else:
#     print('буквы в слове нет')
#
# n = int(input())
# for i in range(n):
#     if i > 10:
#         break
#     elif i%2 == 0:
#         continue
#     #else:
#     print(i)

#s = 'hello world!'
# print(len(s))
# print(s[::-3])
# print(s[0])
# print(s[:4])
#
# for i in range(12):
#     print(s[:i])

# n = int(input())
# for i in range(1,n+1):
#     print(i*'+')

# lst = list((1,4,5)) - тут кортеж внутри, если что
# lst2 = list()
# lst3 = list(s)
# s = ['hello']
# print(lst)
# #
# in_list = ['11',12,'23',24,'10',13]
# for i in in_list:
#     if type(i) == str:
#         print(i*2)
#     elif type(i) == int:
#         print(i**2)
#
# for i,k in enumerate(in_list):
#     print(i,k)
#
# lst = []
# for _ in range(5):
#     x = input()
#     lst.append(x)
#     print(lst)

# sett = set(in_list)
# print('22' in sett)
# print(sett)
#
# a = [1,2,3,4]
# b = a #ссылка на другой объект
# b2 = a[:]#создание нового объекта
# a.append(5)
# print(a,b,b2)

#урок 3
#
# msg = "Hello world!"
# for i in range(-12,12):
#     print(msg[i], end='\n')
#
# w = "Abra cad abra"
# print('ad' in w)
# print(w.find('cad'))
# print((len(s)))
# print(w.count('br'))
# print(s.upper())
# print(s)
# print(s.lower())
# print(s.islower())
# print(s)
# print('123'.isdigit())
# print('[1, 2, 3]')

# #Полиндром
# s = str(input())
# s_check = ''
# for i in range(len(s)):
#     if s[i] != s[len(s) - 1 - i]:
#         print(False)
#         break
# else:
#     print(True)
#
# lst = ['Я', 'пишу', 'программы', 'на', 'питоне']
# print(''.join(lst))
# print(' '.join(lst))
# print('\n'.join(lst))
# print(', '.join(lst))
#

#
# s = "Don't   worry   be   happy"
# print(s.split())
# print(s.split(' '))
# print(s.split(maxsplit=1))
#
# s = '1 2 3 4 5'
# strok = s.split()
# #Как перевести целый массив строк в инт?
# mass = list(map(int, strok))
# print(mass)
#
# print(list('popopoxh'))
# print(list('1,2,3'))
# print(list([1,2,3]))

# lst = [10,True, [1,2], 'abcdg']
#
# for i in range(-len(lst), len(lst)):
#     print(lst[i])
#

# lst = []
# add = []
# n = 5
# for i in range(1, n+1):
#     for j in range (i):
#         lst.append(i)
# print(lst)
#
# add = []
# n = 5
# add.append(n)
# print(add*n)
#
# lst = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
# print(max(lst), min(lst), sum(lst))
#
# print(min(lst,key=abs))

# a = [-2, 4, -8, 3, 34]

# a.sort()
# print(a)

# a.sort(key=abs)
# print(a)
#
# b = sorted(a, reverse=True)
# print(a)
# print(b)
#
# ab = 'abcdefghijklmnopqrstuvwxyz'
# alph = []
#
# for i in range(len(ab)):
#     alph.append(ab[i]*(i+1))
#
# print(alph)
#
# s = 0
# sum = 0
# while s >= 0:
#     sum += s
#     s = int(input())
# print(sum)

#
# x,y = 10,20
# x,y = y,x
#
# (x,y)=(100,200)
#
# tpl = (123,234,345,456,567,678,789,890)
# n = int(input())
# for i in range(len(tpl)):
#     if n < tpl[i]:
#         tpl = tpl[:i]+(n,)+tpl[i:]
#         break
# else:
#     tpl = tpl + (n,)
# print(tpl)
#


# #Урок 4
# d = '4'
# e = 'hi'
# d,e = e, int(d)
# print(d,e)


# #Словарь
# person = {
#     'name':'Masha',
#     'login': 'Masha',
#     'age':25,
# }
# print(type(person))
#
# dict_sample = {
#     1: 'Masha',
#     2: 'loh',
#     True: 'True',
#     False: 3,
#     'True': 4,
#     None: 'error',
#     None: 'mango'
# }
# print(dict_sample)
#
# month_dict = {
#     1:31,
#     2:28,
#     3:31,
#     4:30,
#     5:31,
#     6:30,
#     7:31,
#     8:31,
#     9:30,
#     10:31,
#     11:30,
#     12:31
# }
#
# while True:
#     year = int(input('Введите год'))
#     month = int(input('Введите месяц'))
#     if year == month == 0:
#         break
#     else:
#         if year % 4 == 0 and month == 2:
#             print(year, 29)
#         else:
#             print(year, month_dict[month])
#
#


#
# x = dict(name = 'masha',name2 = 'petya')
# print(x)
# letters = ['a', 'b', 'c', 'd','e']
# numbers = [1,2,3,4]
# d = dict(zip(letters, numbers))
# d2 = dict(zip(numbers,letters))
#
# print(d,d2)
#
# chisla = {1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',
#           0:'ноль'}
# x = int(input())
# for i in list(str(x)):
#     print(chisla[int(i)], end=' ')
#
# Хэш - таблицы
#
# sort_dict = {'a':1, 'n':2, 'k':90, 'e':3}
# for key in sorted(sort_dict):
#     print(key)
# for key, val in sort_dict.items():
#     print(val)
#
# line = 'abracadabra'
# abd = {}
# for i in line:
#     if i in abd:
#         abd[i]+=1
#     else:
#         abd[i] = 1
# print(abd)

#
# abd.clear() #чистим
# print(abd)
#
# defc = abd
# print(defc)
# abd['e']=3
# print(defc)
#
# print(abd.get('a'))
# print(abd.get('f',0))
# print(abd.get('f'))
# print(abd.setdefault('f',0))
# print(abd)
# #
# words = {}
# line = 'abjb ;j ij perofj pojr fwefj wf jld-kme f0ik ij jmdmsodkmpsd'
# for i in line.split():
#     if i not in words.keys():
#         words[i]=0
#     words[i] += 1
#
# print(words)

#fromitems
#items - выедает пары - кортежи - для всех элементов словаря
#
# line = '2 4 6 4 3 6 6 4 20 49 4309 503 3 305 943 404 45'
# lst = list(map(int, line.split()))
# dct = {}
# #for i in range(len(lst)):
# for pos, num in enumerate(lst):
#     if num not in dct:
#         dct[num] = []
#     dct[num].append(pos)
# print(dct)

#update - соединение словарей
#pop и popitem

#Анаграммы
# line = 'monopolo oloponodm'
# dct = {}
#
#
#
# for word in line.split():
#     dct[word] = {}
#     for letter in word:
#         if letter not in dct[word]:
#             dct[word][letter] = 0
#         dct[word][letter]+=1
#
# a = {}
# for i in dct.values():
#     if i == a:
#         print('Aмаграмма!')
#         break
#     a = i



# Урок 5
# n = int(input('Введите число n:'))
# dct = {}
# for i in range(n):
#     sinonim1, sinonim2 = input().split()
#     dct[sinonim1] = sinonim2
#     dct[sinonim2] = sinonim1
#     pass
#
# while True:
#     slovo = input()
#     if slovo == 'stop':
#         break
#     print(dct.get(slovo,'нет синонима в словаре'))
#
# print(round(1,1))
# print(round(1,5))
# print(round(2,5))
# print(divmod(15,6))
#
# print(0b10 + 0b10)
# print(bin(4))
#
# print(0o7 + 0o7)
# print(oct(14))
#
# for i in range(20):
#     print(hex(i))
#
#
#
# sec = int(input())
#
# sec_to_print = sec%60
# min = sec % 3600 // 60
# min_to_print = min%60
# hours = min // 60
# hours_to_print = hours%24
# days = hours // 24
# print(f'days:{days}, H:{hours_to_print}, M:{min_to_print}, S:{sec_to_print}')

#
# n = int(input())
# for i in range(2, int((n)**0.5)+1):
#     if n % i == 0:
#         print('Составное')
#         break
# else:
#     print('Простое')
#
# print(int(True))
# print(True+True)
# print(chr(1025))
# for i in range(1102, 1200):
#     print(chr(i))
#
# start = ord('A')
# end = ord('Z')
# for i in range(start,end+1):
#     print(i, chr(i))

#not - самый главный
#потом and
#потом or
#
# year = int(input())
# if year % 4 == 0 and year%100 != 0 or year%400 == 0:
#     print('Vis')
# else:
#     print('not vis')
#
# s = input()
# word_vowels = []
# word_conson = []
# vowels = ['a','e','i','o','u']
#
# #Создание массивов по глассным/согласным
# for i in s:
#     if i in vowels:
#         word_vowels.append(i)
#     else:
#         word_conson.append(i)
#
# word = []
# if abs(len(word_vowels) - len(word_conson)) <= 1: #Проверка на длину массивов,
#     # можно ли поставить гласные между согласными?
#     if len(word_conson) > len(word_vowels): #Проверка, какой из массивов больше - в зависимости от того,
#         # какой больше, копируем в разные массивы для переноса
#         word_transfer1,word_transfer2 = word_conson.copy(),word_vowels.copy()
#     else:
#         word_transfer1,word_transfer2 = word_vowels.copy(),word_conson.copy()
#     for i in range(len(s)):
#         if i % 2 == 0:
#             word.append(word_transfer1.pop())
#         else:
#             word.append(word_transfer2.pop())
#     print(s, '->', ''.join(word))
# else:
#     print(s, '->', 'Impossible')
#
# #Урок 6.
# a = 256
# b = 256
# a1 = 257
# b2 = 257
#если в консоли написать а1 + 1 is b2 выдаст False
#
# tes = set([1,2,3,2.0])
# #Множества не содержат копий
#
# tes = set([1,  (123,123),'abs'])
# print(tes)
#
# lst = [1,2,2,3,3,3,4,4,4,4]
# print(len(lst))
# tes = set(lst)
# print(len(tes))

# month = ['Jan','Feb','Mar','Apr','May','June', 'Jul', 'Aug', 'Sept', 'OCT','nov', 'dec']
# tes = set(month)
# print(tes)
#
# tes = set([1,2,3,4,5,6,7,8,9,10])
# sred = sum(tes)/len(tes)
# print(sred)
#
# month = ['Jan','Mar','Apr','May','June', 'Jul', 'Aug', 'Sept', 'OCT','nov', 'dec']
# tes = set(month)
# tes.add('Feb')
# tes.discard('May')
# print(tes)

#
# month1 = ['Jan','Mar','Apr','May','June',]
# month2 = [ 'Jan','Jul', 'Aug', 'Sept', 'OCT','nov', 'dec']
# tes1 = set(month1)
# tes2 = set(month2)
# tes = tes1.union(tes2)
# print(tes)
#
# s = input()
# alph = 'abcdefghijklmnopqrstuvwxyz'
# if set(s) == set(alph):
#     print('Панграммная строка')
# else:
#     print('Не панграмная')
#
# x = set([1,2,3])
# y = set([1,2,3,4,5,6])
#
# print(x | y) #Тоже самое что union
# print(x - y)
# print(x ^ y)
#
# print(x.issubset(y))
# print(y.issubset(x))
#
# s = input()
# tes = set()
# for i in s.split():
#     tes = (tes | set(i))
# print(len(tes))
#Неизменные множнства - frozenset
# fro = frozenset((1,2,3))
# print(fro)
#
# def convert_to_celsius(temp):
#     return 5/9* (temp-32)
#
# print(convert_to_celsius(100))
#
# def convert_to_farh(temp):
#     return (temp*9/5)+32
#
# print(convert_to_farh(37.7777776))
#
# def nalog (dohod):
#     return dohod*0.13
#
# s = 0
# summa = 1
# while summa!= 0:
#     summa = int(input())
#     s+= summa
#     print(nalog(s))

# def pprriinntt(var1, *args, **kwargs):
#     print(var1)
#     print(*args)
#     print(**kwargs)
#
# a = pprriinntt(11, [11,2323,345,'ammsd'], [0.0,0.2], '00oo12')
#
# def nalog (dohod, stavka=0.13):
#     return dohod*stavka
#
# s = 0
# while True:
#     summa = int(input())
#     if summa == 0:
#         break
#     s+= summa
#     print(nalog(s))
#
# def uni_let(lst):
#     tes = set()
#     for i in lst:
#         tes = (tes | set(i.lower()))
#     s = ''.join(sorted(tes))
#     return s,len(s)
#
# print(uni_let(['ABcd','uerKHGuhf','eirvfPIOONeoinv____12']))
#
# def check2(n):
#     def chet(n):
#         print (f'{n} - четное')
#     def nechet(n):
#         print(f'{n} - нечетное')
#     if n%2:
#         nechet(n)
#     else:
#         chet(n)
#
# for i in range(10):
#     check2(i)
#
# def fizzbuzz(n):
#     def fb3():
#         print('fizz')
#     def fb5():
#         print('buzz')
#     def fb15():
#         print('fizzbuzz')
#     def fb_none(n):
#         print(f'{n}')
#     if n%15 == 0:
#         fb15()
#     elif n%5 == 0:
#         fb5()
#     elif n%3 == 0:
#         fb3()
#     else: fb_none(n)
#
#
# for i in range(20):
#     fizzbuzz(i)
#
# print(list(zip((1,2,3,4),[4,5],{7:8,9:10,11:12})))
#
# for x in reversed([1,2,3,4,5]):
#     print(x)
#
# def chet(n):
#     if n%2==0: return True
#     return False
#
#
# print(list(filter(chet, [0,1,2,3,4,5,6,7])))

#print(all([[[]]]))
#
# print(sum(map(int, list(str(123)))))
#
# def tros(x):
#     return -abs(x)
#
# print(sorted([1,-2,5,-3,6], key=tros))
# print(max([1,-2,5,-3,6], key=tros))
#
# def kvad(lst, x):
#     rez = []
#     for i in lst:
#         if i**2 > x:
#             rez.append(i)
#     return rez
#
# print(kvad([1,2,3,4,5,6,7,8,-9], 20))
#
# def kvad2(n,x=20):
#     if n**2 > x:
#         return True
#
# print(list(filter(kvad2,[1,2,3,4,5,6,7,8,-9])))

import math
#
# print(math.gcd(12,24))
#
#
# def nok(int1, int2):
#     return int1 * int2 / math.gcd(int1,int2)
#
#
# print(nok(12,4567))
#
# def krug_area (r):
#     return (math.pi*r**2)


#
# lst = [41,26,3,4,55,7,4,65,15, 6784, 3984]
# def last_cifra(lst):
#     return (-lst%10, -lst)
#
#
# print(sorted(lst, key=last_cifra))

# #Lesson8
# print('-'.join('abc-bcd-cde'.split('-')))
# print('abc-bcd-cde'.partition('abc'))
#
#
# s = 'AGAACCCCGGTATGTCGATGTTAGGCAACT'
# n = 2
# #print(s.partition('A'*n).count('A'*n))
# dct = {}
# for i in range(len(s) - n +1):
#     dct[s[i:i + n]] = dct.get(s[i:i + n],0) +1
#
# print(dct.items())
#
# for i in dct:
#     if dct[i]==max(dct.values()):
#         print(i)
#
# def fun1(x): return x%10
# def fun2(x): return x%10,x
#
# spi = [222,21,1,11,12,322]
# print(sorted(spi, key=fun1))
# print(sorted(spi, key=lambda x:x%10))
# print(sorted(spi, key=fun2))
# print(sorted(spi, key=lambda x:(x%10,x)))
# for i in range(1,10):
#     print((lambda x:x**x)(i))
#
# aa = (lambda x:x**x)
# print(aa(8))
#
# st = (lambda s: ''.join(list(reversed(s.lower()))))
# sts = (lambda s: s.lower()[::-1])
#
# #s[-i].lower for i in range(len(s)
#
# print(st('UNojsdhweYYU'))
# print(sts('UNojsdhweYYU'))
# lst = [2,3,4,5,6,7,8,2,1]
#
# print(sorted(lst, key=lambda x:(x%2!=0,x))) #Сортирует сначала там, где в кортеже первое - 0
#
# lst = ['b', 'A', 'Z', 'x']
# print(sorted(lst, key=lambda x: x.lower()))
# lst = [1,10,21,30]
# print(min(lst, key= lambda x: abs(16-x)))
#
# #
# lst = [123,234,345]
# print(list(map(lambda x:sum(map(int,(str(x)))),lst))) #2 map чтобы сделать жестко сумму цифр числа, уф

#
# lst = [('Иванов',100),('Петров',200),('Сидоров',200),('Лунин',200), ('Воробьев',100)]
# print(sorted(lst, key=lambda x:(-x[1], x[0])))
# print(sorted(lst, key=lambda x:(x[1], -ord(x[0][0].upper()))))

#print(sorted([1, -5, 2, -4, 3, float('inf')], key= lambda x:abs(x)))
#print(sorted([1, 2,3,111,222,333], key= lambda x:str(x)))
#print(sorted([1, 0, [],[0],(),(0,), (0)], key= lambda x:bool(x)))
#print(sorted(['Hello', 'This', 'Crazy', 'World'], key= lambda x:x[::-1]))
#
# spi = [222,21,1,111,12,322]
#
# print(sorted(spi, key=lambda x: x%10))
# print(sorted(spi, key=lambda x: (x%10, x)))
# print(sorted(spi, key=lambda x: (x%10, (x//10)%10)))
#
# from functools import reduce
# print(reduce(lambda x,y:x+y, [1,2,3,4,5]))
# print(reduce(lambda x,y:x+y, [1,2,3,4,5], 100))


#
# import collections
#
# a = collections.Counter('aaaaaaaaabbbbbbbbccccccddddeeedffffffabcdef')
# print(a)
# b = dict(a)
# print(b)
# print(a.keys())

#
# f = open("test.txt","r")
# print(f.read(5))
# print(f.read(4))
# print(f.read(5))
# print(f.read())
#
# f.close()
#
# f = open("test.txt", "rt")
# print(f.readlines())
# f.close()
#
# f = open("test.txt", "rt")
# print(f.readline())
# print(f.readline())
#
# f.close()
#
# f = open('test.txt','r')
#
# f.seek(3)
# print(f.read())
# f.close()
#
# import openpyxl
# #
# # wb = openpyxl.load_workbook('test1.xlsx')
# #
# # for listname in wb.sheetnames:
# #     ws = wb[listname]
# #     print('\n',ws.title,'-----------------------')
# #     for i in range(ws.max_row):
# #         for j in range(ws.max_column):
# #             print(i+1,j+1, ws.cell(i+1,j+1).value, end=' ')
#
# wb = openpyxl.load_workbook('test1.xlsx')
#
# ws = wb['Лист1']
#
# lst = [1,2,3,4,5,6]
#
# ws.append(lst)
# ws.append({'A':'tyui',2:'ioiuyyw'})
#
# wb.save('test1.xlsx')

import math
import time
#
# t0 = time.time()
# tes = set()
# for i in range(10000000):
#     tes.add(i**0.5)
# t1 = time.time()
# print(t1 - t0,t0,t1)

#
# t0 = time.time()
# print(time.ctime())
# print(time.ctime(t0))
# time.sleep(5)
# t1 = time.time()
# print(time.ctime(t1))
# print(t1-t0)
#
# def two_sec():
#     t0 = time.time()
#     time.sleep(2)
#     t1 = time.time()
#     return t1-t0
#
#
# def three_sec():
#     t0 = time.time()
#     time.sleep(3)
#     t1 = time.time()
#     return t1-t0
#
# total_time_2 = 0
# total_time_3 = 0
# for i in range(11):
#     if i%2:
#         total_time_3 += three_sec()
#     else:
#         total_time_2 += two_sec()
#
# print(total_time_2,total_time_3)
#
# import datetime
# b= datetime.datetime.today()
# c = datetime.datetime.now()
# print(b.year)
# print(b.month)
# print(b.time())
# print(b.second)
# print(b,c)
#
# d1 = datetime.datetime.strptime('22 04 2022 19:33','%d %m %Y %H:%M')
# # d2 = datetime.datetime.strptime('22 04 2022 20:33','%d %m %Y %H:%M')
# import datetime
# import locale
# print(locale.getlocale())
# locale.setlocale(locale.LC_ALL,'ru')
# print(locale.getlocale())
# # d = datetime.date(2023, 2, 23)
# # print(d.strftime('%a %d, %b %Y'))
# # print(d)
#
# birthday = datetime.date(1994, 6, 18)
# print(birthday.strftime('%B'))
# print(birthday.strftime('%D'))
# print(birthday.strftime('%m'))
# print(birthday.strftime('%d'))
#
# import calendar
# #
# # print(calendar.isleap(1900))
#
# def day_count(n):
#     dct = {}
#     for month in range(1,13):
#         for day in range(1, calendar.monthrange(2023,month)[1] +1):
#             day_num = calendar.weekday(n,month,day)
#             # if day_num in dct.keys():
#             #     dct[day_num] += 1
#             # else: dct[day_num] = 1
#             dct[day_num] = dct.get(day_num, 0) + 1
#     print(dct)
#
# day_count(2004)
#
# lst = [x for x in range(1, 10) if x%3==0]
# print(lst)
#
# orig = [1.25, -9.25, 10.22, 3.78, -5.2, 1.3]
# prices = [i if i > 0 else 0 for i in orig]
# print(prices)

from string import ascii_letters
# ru_letters = 'аеиуюяэыaieyu'
# letters = 'njnlшгиывжщср;sdbc;jb'
#
# lst = [x+'- YES' if x in ru_letters else x+'- NO' for x in letters]
# # print(lst)
# orig = [1.25, -9.25, 10.22, 3.78, -5.2, 1.3]
#
# def get_price(price):
#     return price if price>0 else 0
# prices = [get_price(i) for i in orig ]
# print(prices)
#
# prices = [(lambda x:x if x>0 else 0)(i) for i in orig ]
# print(prices)
# prices = (list(map(get_price, orig)))
# print(prices)
#
# def fizz_buzz(num):
#     return 'FizzBuzz' if num%15==0 else 'Fizz' if num%3==0 else 'Buzz' if num%5==0 else num
#
# lst = [fizz_buzz(i) for i in range(1,20)]
# print(lst)
#
# words = ['я', 'изучаю', 'Питон']
#
# res = [letter for word in words for letter in word]
# print(res)
#
# key = ['name', 'age', 'weight']
# value = ['lilu', 25, 100]
#
# for
#
# lst = [[i*j for i in range(1,10)] for j in range(1,10)]
# print(lst)
#
# flat = [num for row in lst for num in row]
# print(flat)
#
# dct ={}
# for num in range(1,10):
#     dct[num] = num**2
#
# print(dct)
#
# dct2 = {num:num**2 for num in range(1,10)}
# print(dct2)
#
# rus_let = 'фдылижщфёшврlkabs;kabs'
# dct = {i: ord(i)           for i in rus_let}
# print(dct)
#
# items = [(1,2),(3,4),(5,6),(7,8)]
# dct = {key:value for (key,value) in items}
# print(dct)
#
# def fizz_buzz(num):
#     return 'FizzBuzz' if num%15==0 else 'Fizz' if num%3==0 else 'Buzz' if num%5==0 else num
#
# fizzbuzz = {i:fizz_buzz(i) for i in range(1,20)}
# print(fizzbuzz)
#
# from calendar import monthrange as mr
#
# def month_dates(month, year):
#     return [(x,month,year) for x in range(1,mr(year,month)[1]+1)]
#
# def year_dates(year):
#     return [[(x,month,year) for x in range(1,mr(year,month)[1]+1)] for month in range(1,13)]
#
#
# print(month_dates(2,2023))
# print(month_dates(2,2024))
# print(year_dates(2024))
# #
# print([x**2 if x%2==0 else x**3 for x in range (1,11)])

import math
#
# math.sqrt(1)
# s = (-1)**0.5
# s = complex(2,4)
# s = complex(input())
# print(s)
#
# try:
#     s = int(input())
# except Exception:
#     print('Ошибка Exception')
# except ValueError:
#     print('val_err')
# else:
#     print('нет ошибки')
# finally:
#     print('finally')
#
# try:
#     a = 1/0
# except ZeroDivisionError:
#     print('Деление на 0')
#     a = 0
# except ValueError:
#     print('val_err')
# else:
#     print('нет ошибки')
# finally:
#     print('finally')
#
#
# while True:
#     val = (input('число'))
#     try:
#         val = int(val)
#     except ValueError:
#         val = float(val)
#     else:
#         print(val)
#         break
#
# def fun(n):
#     for x in range (n):
#         return x*x
#
# g = fun(3)
# print(g)
#
# def fun(n):
#     for x in range (n):
#         print('До yield',x)
#         yield x*x
#         print('После yield',x)
#
# g = fun(3)
# for k in g:
#     print('До печати', k)
#     print(k)
#     print('После печати', k)
#
# print(g)
#
# def fun(n):
#     for x in range(n):
#         yield x*x if x%2==0 else x**3
#
#
# g = fun(10)
# for k in g:
#     print(k, end=' ')
# for k in g:
#     print(k, end=' ')
#
# def fun(n):
#     for x in range(n):
#         yield x*x if x%2==0 else x**3
# g = fun(3)
# #
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
#
# for k in range(10):
#     try:
#         print(next(g))
#     except StopIteration:
#         print('Stop')
#         break


#
# def factorial():
#     f,k = 1,1
#     while True:
#         yield f
#         k +=1
#         f*=k
#
# gf = factorial()
#
# for m in gf:
#     print(m)
#     input()
#
# def factorial():
#     f,k = 1,1
#     while True:
#         yield f
#         k +=1
#         f+=k
#
# n = int(input())
# gf = factorial()
#
# for m in range(n):
#     print(next(gf))
#
# lst = [1,10,100,2,20,200]
#
# def summa_lst():
#     summa = 0
#     for i in lst:
#         summa+=i
#         yield summa
#
#
#
# summa = summa_lst()
# for i in range(len(lst)):
#     print(next(summa))
#
# try:
#     file = open('tester.txt', 'r')
# except Exception as err:
#     print(Exception, err)
# except FileNotFoundError as err:
#     print(FileNotFoundError, err)

#
# try:
#     file = open('tester.txt', 'r')
# except FileNotFoundError as err:
#     print(FileNotFoundError, err)
# except Exception as err:
#     print(Exception, err)
#
# def devide(x,y):
#     try:
#         out = x/y
#     except:
#         try:
#             import math
#             out = math.inf*x/abs(x)
#         except:
#             out = None
#     finally:
#         return out
#
# print(devide(15,0))
# print(devide(0,0))

#
# try:
#     raise Exception('Что-то не так')
# except Exception as err:
#     print("messege: "+ str(err))
#
# def validate(name):
#     if len(name)<10:
#         raise ValueError
#
# try:
#     name = 'nnnono'
#     validate(name)
# except ValueError:
#     print('ohohoh')
#
# class NameShortError(ValueError):
#     pass
#
# def validate(name):
#     if len(name)<10:
#         raise NameShortError
#
# validate('name')
#
# class Positive(ValueError):
#     pass
#
# class Negative(ValueError):
#     pass
#
# def pos_neg(lst):
#     for num in lst:
#         try:
#             if num<0:
#                 raise Negative
#             elif num:
#                 raise Positive
#             else:
#                 print(num)
#         except Positive: (print('+'))
#         except Negative: (print('-'))
#
# pos_neg([1,0,-7,8,0])
#
#
# def gen(n):
#     for x in range(n):
#         yield x
# g = gen(3)
# print(*g)
#
# #
# def gen2():
#     # yield from 'abcdef'
#     # yield from [3, 4, 5, 6, 7, 8]
#     yield from (67896789, 9,1, 4,0, 5, 6, 7,8, 444,444444)
# g = gen2()
# print(*g)
#
# def fun_gen1():
#     yield from 'red'
#     yield from 'green'
#     yield from 'blue'
#
# def fun_gen2():
#     yield from 'round'
#     yield from fun_gen1()
#     yield from 'square'
#
# print(*fun_gen2())
#
# list_comp = [x for x in range(10)]
# gen_comp = (x for x in range(10))
#
# print(list_comp)
# print(gen_comp)

#
# def integ(n):
#     for i in range(1, n+1):
#         yield i
#
# def evens(iterable):
#     for i in iterable:
#         if not i%2:
#             yield i
#
# def squared(iterable):
#     for i in iterable:
#         yield i*i
#
# chain = squared(evens(integ(10)))
# chain_lst = [x for x in squared(evens(integ(10)))]
# print(*chain)
# print(chain_lst)

#
# def num_from_65():
#     for i in range(ord('а'),ord('а')+32):
#         yield i
#
# def chr_num(iter):
#     for i in iter:
#         yield chr(i).lower()
#
# chain = chr_num(num_from_65())
# print(*chain)
# pass
#
# def fun(n):
#     print('fun', n)
#     input()
#     n -= 1
#     if n > 0:
#         fun(n)
#
# fun(6)

#
# def fun(n):
#     print('fun', n)
#     n -= 1
#     if n > 0:
#         fun(n)
#     print('fun2',n)
#     return
#
# fun(6)
#
# def fact(n):
#     return n*fact(n-1) if n-1 else 1


#
# def triangle(n):
#     print(n * '*')
#     if n==1:
#         pass
#     else:
#         n-=1
#         triangle(n)
#
#         # print(n*'*')
#         # n -=1
#         # triangle(n)
#
#
# triangle(5)
#
#
# def triangle(n):
#
#     if n>0:
#         triangle(n-1)
#     print(n * '*')
#     return
#
#
# triangle(5)
#
#
# def triangle(n):
#     lentot = n
#     if n>0:
#         triangle(n-2)
#     print(f'{(2*lentot-n)*" "}{n * "*"}{(2*lentot-n)*" "}')
#     return
#
#
# triangle(5)
#
#
# def summa(n):
#
#     return n+summa(n-1) if n-1 else 1
# print(summa(3))
#
# def fiba(n):
#
#     #Базовый случай
#     if n == 1 or n == 2:
#         return 1
#     #Рексурсивный случай
#     else:
#         return fiba(n-2)+fiba(n-1)
#
# print(fiba(5))
#
# lst = [1,2,[3,4,5,[6,7,8,9,[10,111]],234,[23,2]],0]
#
# res = []
#
# def lst_transform(lst):
#     for a in lst:
#         if type(a) == int:
#             res.append(a)
#         else:
#             lst_transform(a)
#     return res
#
# print(lst_transform(lst))
#
# import sys
#
# sys.getrecursionlimit()

import re
#
# str = 'Числа 99б 72б 81 и 999 делятся на 9'
# print(re.findall(r"[8-9]",str))
# print(re.findall(r"[6-9]",str))
# print(re.findall(r"\d",str))
# print(re.findall(r"\d\d",str))
# print(re.findall(r"\d{1,3}",str))
# print(re.findall(r"\d+",str))
# print(re.findall(r"\d*",str))
# print(re.findall(r"\dб",str))
# print(set(re.findall(r"\w",str)))
#
# print("\\\"")
# print(r"\\\"")
# print(re.findall(r".",str))
# print(re.findall(r"..",str))
# print(re.findall(r"\b\w*и",str))
'''
\d - любая цифра
\w - любая буква
\b - начало или конеч слова
+ - 1 или больше
* - 0 или больше
? - 0 или 1
'''

# str = 'abracadabra112'
# regex = r".a"
# regex = r"\da\w"
# regex = r"a\d"
# regex = r".a?"
#
# str = 'Числа 99б 72б 81 и 999 100 200 199 1999 19a 1098 делятся на 1'
# print(re.findall(r"\b1\d\d\b",str))
#
#
# str = 'ПоКосой косой коса косить косилка 123'
# print(re.findall(r"\b\w+\b",str))
# print(re.findall(r"\b\w*[Кк]ос\w*\b",str)) #все кос-ы
# print(re.findall(r"\b\w*кос\w*\b|\b\w*Кос\w*\b",str)) #все кос-ы
#
# str = 'cat cet cit c00t cut coot c)t c_t c.t nkn.dfv 8-933-654789 nkn.dfv F123BC78 F123BC788  F123BC178 123.456 d .ddd'
#
# print(re.findall(r"\bc.t\b",str))
# print(re.findall(r"\bc..t\b",str))
# print(re.findall(r"\bc[aui]t\b",str))
# print(re.findall(r"\bc[^aui]t\b",str))
# print(re.findall(r"\bc[^a-c]t\b",str))
# print(re.findall(r"\w[a,5]",str))
#
# print(re.findall(r"\b\w{3}\.\w{3}\b", str)) #xxx.xxx - любой
# print(re.findall(r"\b\d\-\d{3}\-\d{6}\b", str)) #телефон
# print(re.findall(r"\b[A-Z]\d{3}[A-Z]{2}\d{2,3}\b", str)) #автономер
# print(re.findall(r"\b[A-Z]\d{3}[A-Z]{2}1?[7,9]8\b", str)) #автономер СПБ
import math
# str = 'cat cet cit c00t cut coot c)t 8888 888 c_t c.t nkn.dfv 8-933-654789 nkn.dfv F123BC78 F123BC788  F123BC178 123.456 d .ddd'
#
# print(re.sub('cat','ass',str))
# print(re.sub(r'\d{3}','***',str))
# print(re.subn('cat','ass',str,3))
# print(re.subn(r'\d{3}','***',str,3))
# print(re.subn(r'\d','*',str, 10000))
#
# str = "https://www.python.ru/"
#
# print(re.sub(r'\.\w*\.','.rbc.',str))
#
#
#
# str = "(095)-8982-348 095-8923 0 (095)8873234"
#
#
# print(re.sub(r'\(095\)','(812)',str))


import re
#
# text = 'fizzbuzz123.fizz_buzz6578'
# res1 = re.sub(r"\d+",r"#",text)
# print(res1)
# res2 = re.sub(r"[a-z]+",r"(*)",text)
# print(res2)
#
# def fullname(x):
#     s = x.group()
#     print(x.group(),x.start(),x.end())
#
#     match s:
#         case "Коля": return "Николай"
#         case "Миша": return "Михаил"
#
# text = 'Здравствуй Коля, привет Миша'
# print(re.sub(r"\b\w{4}\b", fullname, text))
#
# def airport(x):
#     s = x.group()
#     match s:
#         case "SVO": return "Sheremetevo"
#         case "LED": return "Санкт-Петербург"
#
#
# text2 = 'Самолет из LED прилетел в SVO'
# print(re.sub(r"\b\w{3}\b", airport, text2))
#
# text = "first second"
# print(re.sub(r"(first) (second)", r'\2 \1',text))
#
# text = "Орлов Игорьь Дмитриевич"
# print(re.sub(r"(\w{5}) (\w{6}) (Дмитриевич)", r'\2 \3 \1',text))
#
# txt = '123 first 456 second'
#
# print(re.findall(r"(\d+) (\w+)",txt))
#
# txt2 = 'www.imto.ru 3 www.spbpu.ru 5 www.loh.de www.lohi.by'
#
# print(re.findall(r"www\.(\w+)\.[ru|by]",txt2))
#
# res = re.finditer(r"o",txt2)
#
# for i in res:
#     print(i.group(), i.start(), i.end())
# print(re.split(r"[^\d]",txt2))
#
# txt2 = 'www.imto.ru :3 www.spbpu.ru ;..5 www.loh.de www.l???ohi.by?'
# print(re.split(r"[\.|\ |\:|\;|\?]+", txt2))
#
#
# def squear(x):
#     return str(int(x.group())**2)
#
# txt3 = ' 1 2 3 4 5 6 7 8 9 10 '
# print(re.sub(r"\d+", squear, txt3))
# print(re.sub(r"\d+", lambda x: str(int(x.group())**2), txt3))
#
# x = 5
# print(re.findall(fr"{x}", '12345555666'))
#
# res = '|'.join(str(i) for i in range(x))
# print(re.findall(fr"{res}", '012345555666'))
#
# def func(f):
#     return f
#
# def hello():
#     print('Hello')
# #hello()
# func(hello)()
#
# def speak(txt):
#     def whisper(t):
#         return t.lower()
#     return whisper(txt)
#
# print(speak('HohohohHohoh PPPPPaa'))


#
# def null_decorator(func):
#     return func
#
# def hello():
#     print('hello')
#
# hello = null_decorator(hello)
# hello()
#
# def sample_decorator(func):
#     def wrapper():
#         print('start')
#         func()
#         print('end')
#     return wrapper
#
# def say():
#     print('Привет Мир')
#
# def prop():
#     return 'loh'
#
# say = sample_decorator(say)
# say()
# prop = sample_decorator(prop)
# print(prop())
#
#
#
# def upper_decorator(func):
#     def wrapper():
#         or_res = func()
#         res2 = or_res.upper()
#         return res2
#     return wrapper
#
# @upper_decorator
# def h():
#     return 'Hello'
#
# print(h())
#


def lower_decorator(func):
    def wrapper():
        or_res = func()
        res2 = or_res.lower()
        return res2
    return wrapper

@lower_decorator
def h():
    return 'Hello'

print(h())

@lower_decorator
def l():
    return 'LOH'

print(l())












pass
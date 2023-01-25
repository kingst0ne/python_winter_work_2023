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

s = 'hello world!'
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






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

a = [1,2,3,4]
b = a #ссылка на другой объект
b2 = a[:]#создание нового объекта
a.append(5)
print(a,b,b2)



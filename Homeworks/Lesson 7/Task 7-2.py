'''
Шифр Цезаря
Написать функцию, шифрующую строку шифром Цезаря, со сдвигом буквы вправо

'''
#Способ через 1 ф-ию и словарь
def cesar_through_dict(s,t):
    dct = {}
    for i in range(ord('z') - ord('a')+1):
        if ord('a') + t + i <= ord('z'):
            dct[chr(i+ord('a'))] = chr(i+t+ord('a'))
        else:
            dct[chr(i + ord('a'))] = chr(i + t + ord('a') - 26)
    for i in range(ord('Z') - ord('A')+1):
        if ord('A') + t + i <= ord('Z'):
            dct[chr(i + ord('A'))] = chr(i + t + ord('A'))
        else:
            dct[chr(i + ord('A'))] = chr(i + t + ord('A') - 26)

    s1=''
    for i in s:
        if i in dct.keys():
            s1+=dct[i]
        else:
            s1+=i
    return s1

#Способ через цикл и 2 функции
def check(letter, t):
    if (ord(letter) >= ord('a') and ord(letter) <= ord('z')) or (ord(letter) >= ord('A') and ord(letter) <= ord('Z')):
        if (ord(letter)+t <= ord('z') and ord(letter) >= ord('a')) or (ord(letter)+t <= ord('Z') and ord(letter) >= ord('A')):
            return chr(ord(letter)+t)
        else: return chr(ord(letter) - 26 + t)
    return letter


def cesar_through_cycle(s,t):
    s_new = ''
    for i in s:
        s_new += check(i,t)
    return s_new



print(cesar_through_dict('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTUVWXYZ',t=2))
print(cesar_through_dict("It's been a hard day's night And I've been working like a dog! "
      "It's been a hard day's night I should be sleeping like a log",t=2))

print(cesar_through_cycle('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTUVWXYZ',t=2))
print(cesar_through_cycle("It's been a hard day's night And I've been working like a dog! "
      "It's been a hard day's night I should be sleeping like a log",t=2))
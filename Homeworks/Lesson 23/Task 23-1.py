'''
Найдите длину наибольшей подстроки данной строки, которая
является полиндромом

В строке 'aabbccddcc' длиной подстроки с наибольшим
полиндромом является 6 ('ccddcc')

'''

s = 'aba'

def define_polindrom(s):
    for i in range(len(s)):
        for j in range(i+1):
            s_check = s[j:len(s)-i+j]
            if s_check == s_check[::-1]:
                return len(s_check)

print(define_polindrom(s))


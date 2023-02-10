'''
Дан генетический код ДНК (строка, состоящая из букв G,C,T,A)

Постройте РНК, используя принцип замены букв
G - C
C - G
T - A
A - T

'''


def DNA_transfer(s):
    transfer = {'G': 'C', 'C':'G', 'T':'A', 'A':'T'}
    s1 = ''
    for letter in s:
        s1+= transfer[letter]
    return s1

s = 'GGCTAA'
print(DNA_transfer(s))
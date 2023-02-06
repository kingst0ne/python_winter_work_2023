'''
На вход подается строка генетического кода
состоящая из букв А, Г, Ц, Т
Подкорректируйте код -
1. если рядом стоят буквы А и Г, то поменяйте их местами
2. если рядом стоят Ц и Т, то поставьте АГ между ними
'''

def CT_and_AG_transform(s):
    s = s.replace('ЦТ', 'ЦАГТ')
    s = s.replace('ТЦ', 'ТАГЦ')
    return s

def A_and_G_transform(s):
    s_to_return = ''
    while 'А' in s:
        if s.partition('А')[0].endswith('Г'):
            s_to_return += (s.partition('ГА')[0]+'АГ')
            s = s.partition('ГА')[2]
        elif s.partition('А')[2].startswith('Г'):
            s_to_return += (s.partition('АГ')[0]+'ГА')
            s = s.partition('АГ')[2]
        else:
            s_to_return += (s.partition('А')[0]+'А')
            s = s.partition('А')[2]
    return s_to_return + s

s = 'ГААТЦТЦТЦТЦАГТААГАГАААА'

s = A_and_G_transform(s)
s = CT_and_AG_transform(s)

print(s)

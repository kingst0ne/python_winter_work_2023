'''
Программа принимает на вход строку, после выдает 1 строку из букв, 2 из цифр, 3-ью из символов.

'''

def string_decomposition(s):
    lst_alpha, lst_digit, lst_other = [],[],[]

    for item in set(s):
        if str(item).isalpha():
            lst_alpha.append(item)
        elif str(item).isdigit():
            lst_digit.append(item)
        else:
            lst_other.append(item)

    return ' '.join(lst_alpha), ' '.join(lst_digit), ' '.join(lst_other)


print(string_decomposition('lkjnkdjcn eoijcr poiejr c&HOUHn 120378923y9e84y :":":">>?>>?>>'))

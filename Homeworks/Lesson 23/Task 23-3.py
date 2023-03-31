'''
Создайте функцию, на вход которой подается список из
целых положительных чисел, и которая в качестве результата
возвращает самое большое число, которое можно составить из этих чисел

'''

def max_number_from_list(lst):
    res = ''
    while len(lst) > 0:
        max_1st = 0
        for i in lst:
            if int(str(i)[0]) > max_1st:
                max_1st = int(str(i)[0])
                val = i
            elif int(str(i)[0]) == max_1st:
                pass

        res += str(val)
        lst.remove(val)
    return res

def max_from_list_through_sorted(lst):
    return ''.join(str(i) for i in sorted(lst,key=lambda x:-int(str(x))))




lst1 = [1,21,3]
lst2 = [9,81,25]
lst3 = [3000,9,121,88888]
lst3 = [7,71,72]

# print(max_number_from_list(lst1))
#print(max_number_from_list(lst3))
# print(max_from_list_through_sorted(lst1))
print(max_from_list_through_sorted(lst3))




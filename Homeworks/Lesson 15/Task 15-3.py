'''
Напишите функцию , которая находит в строке все телефонные номера,
которые удовлетворяют следующим условиям:

+7(812)DDD-DDDD +7(812)DDD-DD-DD +7(921)DDD-DDDD +7(921)DDD-DD-DD
'''

import re

def num_find(str):
      return re.findall(r"\+7\(812\)\d{3}\-\d{2}\-?\d{2}|\+7\(921\)\d{3}\-\d{2}\-?\d{2}", str)


str = ' A123BC178+7(812)654-7896  +7(812)6547896A123BC78 А888АА198 А888АА178 A777AA78 A888AA178 +7(812)654-7896 +7(812)654-78-96 +7(921)654-7896 765+98129-2390'

print(num_find(str))
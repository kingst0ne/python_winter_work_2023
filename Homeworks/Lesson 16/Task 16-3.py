'''
Создайте декоратор, который переводит все слова к следующему
виду, первая буква в верхнем регистре, остальные - в нижнем
'''


def title_decorator(func):
    def wrapper():
        or_res = func()
        res2 = or_res.title()
        return res2
    return wrapper

@title_decorator
def say():
    return 'hello my dear friend. nice to meet you'

print(say())
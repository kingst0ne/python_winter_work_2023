'''
каждый 3-ий четверг в Эрмитаже посещение - бесплатно

выведете на экран все даты бесплатных посещений в Эрмитаже в этом году
'''
import calendar
import datetime
import locale

locale.setlocale(locale.LC_ALL,'ru')

def day_count(n):
    lst = []
    for month in range(1,13):
        for day in range(1, calendar.monthrange(2023,month)[1] +1):
            day_num = calendar.weekday(n,month,day)
            if day_num == 3 and (day >= 15 and day < 22):
                day = datetime.datetime.strptime(f'{day} {month} {n}','%d %m %Y')
                lst.append(f'{day.strftime("%d")}'+' '+ f'{day.strftime("%B")},')
    return lst

print(*day_count(2023))

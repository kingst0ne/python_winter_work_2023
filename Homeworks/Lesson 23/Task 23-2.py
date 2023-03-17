'''
Напишите программу, которая считывает информацию из таблицы book1
и формирует DataFrame, полностью соответствующий этой таблице

Нарисуйте графики количеств книг и цен

'''

import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password = "1111",
    host="127.0.0.1",
    port="5432"
)
cur = con.cursor()
cur.execute("SELECT * from book2")

df = pd.DataFrame(cur.fetchall(), columns=['book_id','book_name','author','price','amount'])
df.plot(kind='bar',x='price',y='amount')
plt.show()

pass
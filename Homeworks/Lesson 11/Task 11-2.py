'''
Дан файл с расширением .csv, содержащий в каждой строчке
следующую информацию - номер, фамилия, имя, компания, зп

Создать excel-файл, в который перенесите эту информацию,
предварительно отсортировав этот список по компании,
фамилии и имени

В конце списка добавьте строку ИТОГО и суммарное значение зарплат
'''

import csv
import openpyxl


lst = []
with open('data.csv', newline='', encoding='utf-8') as file:
    rows = csv.reader(file)
    for i, row in enumerate (rows):
        lst.append(tuple(row[0].split(';')))

lst_sorted = sorted(lst, key= lambda x: (x[3],x[1],x[2]))



wb = openpyxl.Workbook()
wb.save('salary.xlsx')
ws = wb.active
for i in range(1, len(lst_sorted)+1):
    for j in range(1, len(lst_sorted[0])):
        ws.cell(row=i, column=j).value = lst_sorted[i-1][j-1]

wb.save('salary.xlsx')



pass

# Берет данные из базы в формате vowpal_wabbit, преобразует 
# в один текстовый файл в формате vowpal_wabbit

import sqlite3

# Количество записей обрабатываемых за один проход
LIMIT = -1      # -1 -> лимит выключен;
# Адрес БД с иходными данными
DB_ADRESS = 'application/data_raw/spider.sqlite'
# Адрес файла для сохарнения результата
FILE_ADRESS = 'application/data_clean/result_clean/news_in_vowpal_wabbit_ria_1kk.txt'

conn = sqlite3.connect(DB_ADRESS)
cur = conn.cursor()

print()

query_str = (
    "SELECT url, vowpal_wabbit FROM Pages " 
    + "WHERE vowpal_wabbit_date is not NULL and source is \'ria\'"
)
# Добавление ограничение запроса, если LIMIT > 0
if LIMIT > 0:
    query_str = query_str + ' LIMIT ' + str(LIMIT)

# Получение данных из базы
cur.execute(query_str)
data = cur.fetchall()

print("Данные выгружены из базы")

# Опустошение файла, если он существует
open(FILE_ADRESS, 'w').close()
for i in range(len(data)):
    
    # Удаление слишком коротких документов
    if data[i][1] != None and len(data[i][1]) > 30:
        # Добавление строки в файл
        line = data[i][0] + ' ' + data[i][1]

        # TODO Удаление названия модальности для эксперимента
        line = line.replace('|text ', '')
        
        with open(FILE_ADRESS, 'a') as f:
            f.write(line + "\n")

        if i % 10000 == 0:
            print("Запись номер", i, "добавлена в файл")

print('Запись в файл ' + FILE_ADRESS + ' окончена')
print()

# Берет данные из базы в формате vowpal_wabbit, преобразует 
# в один текстовый файл в формате vowpal_wabbit

import sqlite3

# Количество записей обрабатываемых за один проход
LIMIT = -1      # -1 -> лимит выключен;
# Адрес БД с иходными данными
DB_ADRESS = 'application/data_raw/spider.sqlite'
# Адрес файла для сохарнения результата
FILE_ADRESS = 'application/data_clean/result_clean/news_in_vowpal_wabbit.txt'

conn = sqlite3.connect(DB_ADRESS)
cur = conn.cursor()

print()

query_str = (
    "SELECT url, vowpal_wabbit FROM Pages " 
    + "WHERE vowpal_wabbit_date is not NULL and vowpal_wabbit is not NULL"
)
# Добавление ограничение запроса, если LIMIT > 0
if LIMIT > 0:
    query_str = query_str + ' LIMIT ' + str(LIMIT)

# Получение данных из базы
cur.execute(query_str)
data = cur.fetchall()

# Опустошение файла, если он существует
open(FILE_ADRESS, 'w').close()
for i in range(len(data)):
    
    # Добавление строки в файл
    line = data[i][0] + ' ' + data[i][1]

    # Удаление названия модальности для эксперимента (после надо поправить)
    line = line.replace('|text ', '')
    
    with open(FILE_ADRESS, 'a') as f:
        f.write(line + "\n")

print('Запись в файл ' + FILE_ADRESS + ' окончена')
print()

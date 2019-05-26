import sqlite3

# Количество записей обрабатываемых за один проход
PART_LIMIT = 50
FILE_ADRESS = 'application/data_clean/news_in_vowpal_wabbit.txt'
DB_ADRESS = 'application/data_raw/spider.sqlite'

conn = sqlite3.connect(DB_ADRESS)
cur = conn.cursor()

print()

# Получение данных из базы
cur.execute(
    "SELECT url, vowpal_wabbit FROM Pages "
    + "WHERE vowpal_wabbit_date is not NULL and vowpal_wabbit is not NULL "
    + "LIMIT "
    + str(PART_LIMIT)
)
data = cur.fetchall()

# Опустошение файла, если он существует
open(FILE_ADRESS, 'w').close()
for i in range(len(data)):
    
    # Вставка строки в файл
    line = data[i][0] + ' ' + data[i][1]
    with open(FILE_ADRESS, 'a') as f:
        f.write(line + "\n")

print('Запись в файл ' + FILE_ADRESS + ' окончена')


print()

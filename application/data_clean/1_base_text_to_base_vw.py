import sqlite3
import datetime

import libs.my_vw_lib as vw

DB_ADRESS = 'application/data_raw/spider.sqlite'
# Количество записей обрабатываемых за один проход
PART_LIMIT = 50

try:
	conn = sqlite3.connect(DB_ADRESS)
	cur = conn.cursor()

	data = [0]
	while len(data) != 0:
		print()
		print("Обработка идет по", PART_LIMIT, "записей")
		print()
		print("Начало обработки...")
		print()

		# Получение данных из базы
		cur.execute(
			"SELECT url, body_text, vowpal_wabbit, vowpal_wabbit_date FROM Pages "
			+ "WHERE vowpal_wabbit_date is NULL and body_text is not NULL "
			# Сделано так, что бы быстрее работал RANDOM()
			+ "and id IN (SELECT id FROM Pages ORDER BY RANDOM() LIMIT " 
			+ str(PART_LIMIT) 
			+ ")"
		)
		data = cur.fetchall()

		for i in range(len(data)):
			# Преобразовываем tuple в list
			data[i] = list(data[i])

			# body_text
			text = data[i][1]

			if len(text) > 30:
				# Форматирование текста
				vw_text = vw.text_to_vowpal_wabbit(text)

				# vowpal_wabbit
				data[i][2] = vw_text

				# vowpal_wabbit_date
				data[i][3] = int((datetime.datetime.utcnow() -
							datetime.datetime(1970, 1, 1)).total_seconds())
			
			if i % 10 == 0:
				print("Подготовлена запись номер", i)
		
		# Запись результатов в базу
		for i in range(len(data)):
			cur.execute("UPDATE Pages SET vowpal_wabbit=?, vowpal_wabbit_date=? WHERE url=?",(
				data[i][2],		# vowpal_wabbit
				data[i][3],		# vowpal_wabbit_date
				data[i][0],		# url
			))
			if i % 50 == 0:
				conn.commit()
		conn.commit()
		
		print()
		cur.execute("SELECT count() FROM Pages")
		print('{0:30}'.format("Записей в базе:"), 
			'{0:7}'.format(cur.fetchone()[0]))
		cur.execute("SELECT count() FROM Pages WHERE vowpal_wabbit_date is not NULL")
		print('{0:30}'.format("Обработано записей:"),
			'{0:7}'.format(cur.fetchone()[0]))

	print()
	print("Все записи обработаны")

except KeyboardInterrupt:	# Ctrl+C
    pass

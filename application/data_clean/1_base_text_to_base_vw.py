# Берет из базы текст на русском языке, проводит леммирование, преобразование 
# к vowpal_wabbit формату и сохраняет обратно в базу построчно

import sqlite3
import datetime
import multiprocessing as mp

import libs.my_vw_lib as vw

WORKER_NUM = 16

#MODE = 'body_text'
MODE = 'html'

# Адрес БД с иходными данными и для сохранения результата
#DB_ADRESS = 'application/data_raw/spider.sqlite'
DB_ADRESS = 'spider.sqlite'
# Количество записей обрабатываемых за один проход
PART_LIMIT = 50

def clean_one_part(i):
    	
	# Соединение с БД
	conn = sqlite3.connect(DB_ADRESS)
	cur = conn.cursor()

	# Работа пока пользователь не нажмет Ctrl+C
	# или пока не закончатся необработанные даныные в базе
	data = [0]
	while len(data) != 0:

		# Вывод текущей ситуации обработки данных в базе
		#print()
		cur.execute("SELECT count() FROM Pages")
		print("Процесс_{0:0>3}: ".format(num) + '{0:30}'.format("Записей в базе:"),
					'{0:7}'.format(cur.fetchone()[0]))
		cur.execute("SELECT count() FROM Pages WHERE vowpal_wabbit_date is not NULL")
		print("Процесс_{0:0>3}: ".format(num) + '{0:30}'.format("Обработано записей:"),
					'{0:7}'.format(cur.fetchone()[0]))
		#print()

		# Получение данных из базы по PART_LIMIT штук
		cur.execute(
			"SELECT url, "+MODE+", vowpal_wabbit, vowpal_wabbit_date, title_text FROM Pages "
			+ "WHERE vowpal_wabbit_date is NULL and "+MODE+" is not NULL "
			# Сделано так, что бы быстрее работал RANDOM()
			+ "and id IN (SELECT id FROM Pages ORDER BY RANDOM() "
			+ "LIMIT "
			+ str(PART_LIMIT)
			+ ")"
		)
		data = cur.fetchall()

		# Построчная обработка полученных данных
		for i in range(len(data)):

			# Преобразование tuple в list
			data[i] = list(data[i])

			if MODE == 'html':
				mode_text = data[i][1].decode()
			else:
				mode_text = data[i][1]

			# body_text/html + title_text
			text = mode_text + ' ' + data[i][4]

			if len(text) > 30:

				# Леммирование текста, переработка в формат vowpal_wabbit
				vw_text = vw.text_to_vowpal_wabbit(text)

				# Запись результатов в столбец vowpal_wabbit
				data[i][2] = vw_text

				# Запись даты и времени обработки в столбец vowpal_wabbit_date
				data[i][3] = int((datetime.datetime.utcnow() -
									datetime.datetime(1970, 1, 1)).total_seconds())
			# Периодический вывод id, что бы пользователь понимал, что все ОК
			if i % 10 == 0:
				print("Процесс_{0:0>3}: ".format(num) + "подготовлена запись номер", i)

		# Запись результатов в базу
		for i in range(len(data)):
			cur.execute("UPDATE Pages SET vowpal_wabbit=?, vowpal_wabbit_date=? WHERE url=?", (
				data[i][2],		# Столбец: vowpal_wabbit
				data[i][3],		# Столбец: vowpal_wabbit_date
				data[i][0],		# Столбец: url
			))
			if i % 50 == 0:
					# Периодический коммит, что бы не потерять
				# слишком много данных при остановке программы
				conn.commit()
		conn.commit()

	print("Процесс{0:0>3}: ".format(num) + "Все записи обработаны")

try:

	print()
	print("Обработка идет по", PART_LIMIT, "записей")
	print()
	print("Начало обработки...")
	
	for num in range(WORKER_NUM):
		mp.Process(target=clean_one_part, args=(
			num,
		)).start()

except KeyboardInterrupt:	# Ctrl+C
	print()
	pass

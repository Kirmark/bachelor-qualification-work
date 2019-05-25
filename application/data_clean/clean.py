import text_to_vowpal_wabbit
import sqlite3

db_adress = 'application/data_raw/spider.sqlite'

conn = sqlite3.connect(db_adress)
cur = conn.cursor()

cur.execute("SELECT url, html, title_text, body_text, date_clean FROM Pages LIMIT 3")
data = cur.fetchall()



'''
data = [0]
while len(data) != 0:
    print()
	print("Работаю...")

	cur.execute("SELECT url, html, title_text, body_text, date_clean FROM Pages WHERE date_clean is NULL and html is not NULL ORDER BY RANDOM() LIMIT 300")
	data = cur.fetchall()

	for i in range(len(data)):
	    data[i] = list(data[i])
	    
	    html = data[i][1]
	    soup = BeautifulSoup(html, "html.parser")
	    
	    hader_parts = soup.find(attrs={'class': re.compile(r"^mz-publish__title$")})
	    if hader_parts is None:
	        hader_parts = soup.find(attrs={'class': re.compile(r"^mz-feature-item mz-feature-item_type-digit")})
	    if hader_parts is None:
	        hader_parts = soup.find(attrs={'class': re.compile(r"^mz-feature-item mz-feature-item_chronic")})
	    if hader_parts is None:
	        hader_parts = soup.find(attrs={'class': re.compile(r"^mz-feature-item mz-feature-item_photo")})
	    data[i][2] = tags_to_text(hader_parts, use_strip=True).strip()

	    text_parts = soup.find(attrs={'class': re.compile(r"^mz-publish__text$")})
	    if text_parts is None:
	        text_parts = soup.find(attrs={'class': re.compile(r"^card-list$")})
	    data[i][3] = tags_to_text(text_parts, use_strip=True) \
	        .strip() \
	        .replace("\xa0", "\n") \
	        .replace("  ", " ") \
	        .replace("\n ", "\n") \
	        .replace(" \n", "\n")

	    data[i][4] = int((datetime.datetime.utcnow()-datetime.datetime(1970,1,1)).total_seconds())

	for i in range(len(data)):
	    cur.execute("UPDATE Pages SET title_text=?, body_text=?, date_clean=? WHERE url=?", (data[i][2], data[i][3], data[i][4], data[i][0] ) )
	    if i % 50 == 0:
	        conn.commit()
	conn.commit()

	cur.execute("SELECT count() FROM Pages")
	print('{0:30}'.format("Записей в базе:"), '{0:7}'.format(cur.fetchone()[0]))
	cur.execute("SELECT count() FROM Pages WHERE date_clean is not NULL")
	print('{0:30}'.format("Обработано записей:"), '{0:7}'.format(cur.fetchone()[0]))

'''

print()
print("Все записи обработаны")

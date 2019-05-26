# Берет текстовый файл в формате vowpal_wabbit, преобразует данные 
# в формат batches и сохраняет в указанной папке

import artm

# Адрес файла с исходными данными
FILE_ADRESS = 'application/data_clean/result_clean/news_in_vowpal_wabbit.txt'
# Адрес папки для сохранения результата
BATCH_ADRESS = 'application/models/batches_news'

# Преобразование в формат для bigartm
batch_vectorizer = artm.BatchVectorizer(
    data_path=FILE_ADRESS, data_format='vowpal_wabbit', collection_name='news', target_folder=BATCH_ADRESS)


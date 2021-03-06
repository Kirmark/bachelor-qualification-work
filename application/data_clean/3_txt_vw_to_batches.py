# Берет текстовый файл в формате vowpal_wabbit, преобразует данные 
# в формат batches и сохраняет в указанной папке

import artm

# Адрес файла с исходными данными
FILE_ADDRESS = 'application/data_clean/result_clean/news_in_vowpal_wabbit_ria_1kk.txt'
# Адрес папки для сохранения результата
BATCH_ADDRESS = 'application/models/batches_news_ria_1kk'

# Преобразование в формат для bigartm
batch_vectorizer = artm.BatchVectorizer(
    data_path=FILE_ADDRESS, 
    data_format='vowpal_wabbit', 
    collection_name='news', 
    target_folder=BATCH_ADDRESS
)

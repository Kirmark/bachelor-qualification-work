import artm

FILE_ADRESS = 'application/data_clean/test.txt'
BATCH_ADRESS = 'application/models/batches_news'

batch_vectorizer = artm.BatchVectorizer(
    data_path=FILE_ADRESS, data_format='vowpal_wabbit', collection_name='news', target_folder=BATCH_ADRESS)


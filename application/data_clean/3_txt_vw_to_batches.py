import artm

FILE_ADRESS = 'application/data_clean/test.txt'


#print(artm.version())



#model = artm.ARTM()

batch_vectorizer = artm.BatchVectorizer(
    data_path=FILE_ADRESS, 
    data_format="vowpal_wabbit", 
    target_folder="test",
    batch_size=100,
)

'''
batch_vectorizer = artm.BatchVectorizer(
    data_path=FILE_ADRESS,
    data_format='vowpal_wabbit',
    collection_name='test',
    target_folder='test'
)
'''

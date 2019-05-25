import artm

FILE_ADRESS = 'application/data_clean/test.txt'

batch_vectorizer = artm.BatchVectorizer(
    data_path=FILE_ADRESS, 
    data_format="vowpal_wabbit", 
    target_folder="school_batches",
    batch_size=100,
)

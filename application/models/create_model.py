import artm

BATCH_ADRESS = 'application/models/batches_news'

batch_vectorizer = artm.BatchVectorizer(
    data_path=BATCH_ADRESS, data_format='batches')

# Создаем словарь и инициализируем модель с его помощью
dictionary = batch_vectorizer.dictionary
topic_names = ['topic_{}'.format(i) for i in range(15)]

model_plsa = artm.ARTM(topic_names=topic_names, cache_theta=True,
                       scores=[artm.PerplexityScore(name='PerplexityScore',
                                                    dictionary=dictionary)])

model_artm = artm.ARTM(topic_names=topic_names, cache_theta=True,
                       scores=[artm.PerplexityScore(name='PerplexityScore',
                                                    dictionary=dictionary)],
                       regularizers=[artm.SmoothSparseThetaRegularizer(name='SparseTheta',
                                                                       tau=-0.15)])

model_artm.regularizers.add(
    artm.SmoothSparsePhiRegularizer(name='SparsePhi', tau=-0.1))
model_artm.regularizers.add(artm.DecorrelatorPhiRegularizer(
    name='DecorrelatorPhi', tau=1.5e+5))

model_plsa.num_document_passes = 1
model_artm.num_document_passes = 1

model_plsa.fit_offline(batch_vectorizer=batch_vectorizer,
                       num_collection_passes=15)
model_artm.fit_offline(batch_vectorizer=batch_vectorizer,
                       num_collection_passes=15)

'''
model_artm.regularizers['SparsePhi'].tau = -0.2
model_artm.regularizers['SparseTheta'].tau = -0.2
model_artm.regularizers['DecorrelatorPhi'].tau = 2.5e+5

model_plsa.scores.add(artm.TopTokensScore(name='TopTokensScore', num_tokens=6))
model_artm.scores.add(artm.TopTokensScore(name='TopTokensScore', num_tokens=6))


model_plsa.fit_offline(batch_vectorizer=batch_vectorizer,
                       num_collection_passes=25)
model_artm.fit_offline(batch_vectorizer=batch_vectorizer,
                       num_collection_passes=25)

print_measures(model_plsa, model_artm)
'''

for topic_name in model_plsa.topic_names:
    print(topic_name + ': ',)
    print(model_plsa.score_tracker['TopTokensScore'].last_tokens[topic_name])

for topic_name in model_artm.topic_names:
    print(topic_name + ': ',)
    print(model_artm.score_tracker['TopTokensScore'].last_tokens[topic_name])

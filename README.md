# sentiment-analysis-imdb

## Learning Methods
### Averaging Vectors + Random Forest
Word Embedding | Details | Score
--- | --- | ---
Bag of Words | Tutorial. Remove stop words, numbers. | 0.84644
Word2Vec skip-gram | Tutorial. Spell out digits 0-9. | 0.83104
FastText skip-gram | Spell out digits 0-9. | 0.83688
FastText skip-gram | Spell out digits 0-10. | 0.8323
FastText skip-gram | Spell out digits 0-9. Supervised on pretrained vectors cc.en.300. | 0.8290
FastText skip-gram | Spell out digits 0-10. Supervised on pretrained vectors wiki-news-300d-1M. | 0.8276
FastText skip-gram | Spell out digits 0-9. Supervised on pretrained wiki-news-300d-1M.| 0.8260
FastText skip-gram | Spell out digits 0-9. Directly uses pretrained vectors cc.en.300. | 0.7582
FastText cbow | Preserve stop words, numbers. | 0.80956

### RNN
#### BiLSTM
Word Embedding | Unit | Dropout | Epoch | Details | Score
--- | --- | --- | --- | --- | ---
Word2Vec skip-gram | 100 | 0.2 | 10 | Spell out digits 0-9. | 0.8918
Word2Vec skip-gram | 32 | 0.2 | 6 |  Spell out digits 0-9. | 0.8802


## Things to think about
### Text Preprocessing
Canonicalization? (I've -> I have)
Lemmatization?
Removing stop words? (Discouraged by Kaggle)

### Model
Ensemble Learning? Combining SVN, Random Forest with RNN and average them (paper needed)
LSTM

### Visualization
T-SNE
WordCloud

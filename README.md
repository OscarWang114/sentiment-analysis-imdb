# sentiment-analysis-imdb

## Scores

Word Embedding | Learning Method | Details | Score
--- | --- | --- | ---
Bag of Words | Random Forest | Tutorial. Remove stop words, numbers. | 0.84644
Word2Vec skip-gram| Random Forest | Tutorial. Spell out digits 0-9. Avg Vectors.| 0.83104
FastText skip-gram| Random Forest | Spell out digits 0-9. Avg Vectors. | 0.83688
FastText skip-gram| Random Forest | Spell out digits 0-10. Supervised on pretrained vectors wiki-news-300d-1M. Avg Vectors. | 0.8276
FastText skip-gram| Random Forest | Spell out digits 0-9. Supervised on pretrained wiki-news-300d-1M.vec. Avg Vectors. | 0.8260
FastText skip-gram| Random Forest | Spell out digits 0-9. Directly uses pretrained vectors cc.en.300. Avg Vectors. | 0.7582
FastText cbow | Random Forest | Preserve stop words, numbers. Avg Vectors. | 0.80956


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

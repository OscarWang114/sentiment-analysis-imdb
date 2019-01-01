# sentiment-analysis-imdb

## Scores

Word Embedding | Learning Method | Details | Score 
--- | --- | --- | ---
Bag of Words | Random Forest | Tutorial. Remove stop words, numbers. | 0.84644
Word2Vec skip-gram| Random Forest | Tutorial. Preserve stop words, numbers. Avg Vectors.| 0.83104
FastText skip-gram| Random Forest | Preserve stop words, numbers. Avg Vectors. | 0.83688


## Things to think about
### Text Preprocessing
Canonicalization? (I've -> I have)
Lemmatization?
Removing stop words? (Discouraged by Kaggle)

### Model
Ensemble Learning? Combining SVN, Random Forest with RNN and average them (paper needed)
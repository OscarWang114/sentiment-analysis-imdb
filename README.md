# sentiment-analysis-imdb

## Scores

Model | Details | Score 
--- | --- | ---
Bag of Words (tutorial) | Remove stop words. Random Forest. | 0.84644
Word2Vec Avg Vectors(tutorial) | Preserve stop words, numbers. Random Forest | 0.83104

## Things to think about
### Text Preprocessing
Canonicalization? (I've -> I have)
Lemmatization?
Removing stop words? (Discouraged by Kaggle)

### Model
Ensemble Learning? Combining SVN, Random Forest with RNN and average them (paper needed)
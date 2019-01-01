#!/usr/bin/env bash

# Set values for various parameters.
# Use the same values as Word2Vec tutorial.
num_features=300  # Word vector dimensionality
min_word_count=40  # Minimum word count
num_workers=4  # Number of threads to run in parallel
context=10  # Context window size
downsampling=$(echo $(bc <<< 'scale=3; 1/1000') ) # Downsample setting for frequent words

../../fastText/fasttext skipgram -input corpus.txt \
    -output "${num_features}features_${min_word_count}minwords_${context}context" \
    -dim ${num_features} -minCount ${min_word_count} -thread ${num_workers} -ws ${context} -t ${downsampling}
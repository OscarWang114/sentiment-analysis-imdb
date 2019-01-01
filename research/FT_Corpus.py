#  Author: Oscar Wang
#  Date: 01/01/2019
#
#  This file uses some code from the Kaggle tutorial for pre-processing and random forest algorithm
#
# *************************************** #


# ****** Read the two training sets and the test set
#
import pandas as pd
import os
from nltk.corpus import stopwords
import nltk.data

from Utility import Utility


if __name__ == '__main__':

    # Read data from files
    train = pd.read_csv(os.path.join(os.path.dirname(__file__), '../', 'data-set', 'labeledTrainData.tsv'), header=0,
                        delimiter="\t", quoting=3)
    test = pd.read_csv(os.path.join(os.path.dirname(__file__), '../', 'data-set', 'testData.tsv'), header=0, delimiter="\t",
                       quoting=3)
    unlabeled_train = pd.read_csv(os.path.join(os.path.dirname(__file__), '../', 'data-set', "unlabeledTrainData.tsv"), header=0,
                                  delimiter="\t", quoting=3)

    # Verify the number of reviews that were read (100,000 in total)
    print "Read %d labeled train reviews, %d labeled test reviews, " \
          "and %d unlabeled reviews\n" % (train["review"].size,
                                          test["review"].size, unlabeled_train["review"].size)

    # Load the punkt tokenizer
    # nltk data package includes a pre-trained Punkt tokenizer for English.
    # pickle in nltk is a serialized python object, stored using the python pickle module.
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # ****** Split the labeled and unlabeled training sets into clean sentences
    #
    sentences = []  # Initialize an empty list of sentences

    print "Parsing sentences from training set"
    for review in train["review"]:
        sentences += Utility.review_to_sentences(review, tokenizer, remove_numbers=False)

    print "Parsing sentences from unlabeled set"
    for review in unlabeled_train["review"]:
        sentences += Utility.review_to_sentences(review, tokenizer, remove_numbers=False)

    # Saving the sentences in a corpus.
    # Separate each sentence using line breaks.
    # See https://github.com/facebookresearch/fastText/issues/518 and 441
    corpus = open('fasttext_corpus.txt', 'w')
    for sentence in sentences:
        text = ' '.join(sentence) + '\n'
        corpus.write(text)
    corpus.close()

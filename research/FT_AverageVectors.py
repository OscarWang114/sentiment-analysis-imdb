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
import logging
import numpy as np  # Make sure that numpy is imported
import fastText

from sklearn.ensemble import RandomForestClassifier
from Utility import Utility


# ****** Define functions to create average word vectors
#

def makeFeatureVec(words, model, num_features):
    # Function to average all of the word vectors in a given
    # paragraph
    #
    # Pre-initialize an empty numpy array (for speed)
    featureVec = np.zeros((num_features,), dtype="float32")
    #
    nwords = 0.
    #
    # Loop over each word in the review and, if it is in the model's
    # vocaublary, add its feature vector to the total
    for word in words:
        nwords = nwords + 1.
        featureVec = np.add(featureVec, model.get_word_vector(word))
    #
    # Divide the result by the number of words to get the average
    featureVec = np.divide(featureVec, nwords)
    return featureVec


def getAvgFeatureVecs(reviews, model, num_features):
    # Given a set of reviews (each one a list of words), calculate
    # the average feature vector for each one and return a 2D numpy array
    #
    # Initialize a counter
    counter = 0.
    #
    # Preallocate a 2D numpy array, for speed
    reviewFeatureVecs = np.zeros((len(reviews), num_features), dtype="float32")
    #
    # Loop through the reviews
    for review in reviews:
        #
        # Print a status message every 1000th review
        if counter % 1000. == 0.:
            print "Review %d of %d" % (counter, len(reviews))
        #
        # Call the function (defined above) that makes average feature vectors
        reviewFeatureVecs[int(counter)] = makeFeatureVec(review, model, num_features)
        #
        # Increment the counter
        counter = counter + 1.
    return reviewFeatureVecs


def getCleanReviews(reviews):
    clean_reviews = []
    for review in reviews["review"]:
        # Don't remove numbers
        clean_reviews.append(Utility.review_to_wordlist(review, remove_stopwords=True, remove_numbers=False))
    return clean_reviews


if __name__ == '__main__':

    # Read data from files
    train = pd.read_csv(os.path.join(os.path.dirname(__file__), '../', 'data-set', 'labeledTrainData.tsv'), header=0,
                        delimiter="\t", quoting=3)
    test = pd.read_csv(os.path.join(os.path.dirname(__file__), '../', 'data-set', 'testData.tsv'), header=0, delimiter="\t",
                       quoting=3)

    # Verify the number of test reviews that were read
    print "Read %d labeled train reviews, %d labeled test reviews\n" % (train["review"].size, test["review"].size)

    # Import the built-in logging module and configure it so that Word2Vec
    # creates nice output messages
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # Using the trained model from FastText
    print "Using FastText model..."
    num_features = 300
    model = fastText.load_model('300features_40minwords_10context.bin')

    # ****** Create average vectors for the training and test sets
    #
    print "Creating average feature vecs for training reviews"

    trainDataVecs = getAvgFeatureVecs(getCleanReviews(train), model, num_features)

    print "Creating average feature vecs for test reviews"

    testDataVecs = getAvgFeatureVecs(getCleanReviews(test), model, num_features)

    # ****** Fit a random forest to the training set, then make predictions
    #
    # Fit a random forest to the training data, using 100 trees
    forest = RandomForestClassifier(n_estimators=100)

    print "Fitting a random forest to labeled training data..."
    forest = forest.fit(trainDataVecs, train["sentiment"])

    # Test & extract results
    result = forest.predict(testDataVecs)

    # Write the test results
    output = pd.DataFrame(data={"id": test["id"], "sentiment": result})
    output.to_csv(os.path.join(os.path.dirname(__file__), '../', 'output', "FT_AverageVectors.csv"), index=False, quoting=3)
    print "Wrote FT_AverageVectors.csv"

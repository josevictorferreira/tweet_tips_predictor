""" Predictor module for predicting if a tweet is a tip or a not. """

import os
import pandas
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from tweet_tips_predictor.models.tweet import Tweet
from tweet_tips_predictor.utils import get_env


class TipPredictor():
    """ TipPredictor, predict tweets using Machine Learning, SGDC classifier. """

    def __init__(self):
        self.dataset = pandas.DataFrame(Tweet.all())
        self.pipeline = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            (('clf-svm', SGDClassifier(
                loss='hinge',
                penalty='l2',
                alpha=1e-3,
                random_state=42)))
            ])
        print(self.dataset.head())
        self.pipeline = self.pipeline.fit(
            self.dataset['text'],
            self.dataset['is_tip'])

    def predict(self, text):
        """ Predicts if a given text param is a tip or not. Returns a boolean value. """
        prediction = self.pipeline.predict([text])
        return bool(prediction[0])

    @classmethod
    def dataset_path(cls):
        """ Returns the full path for the dataset file. """
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(
            os.path.join(basepath, "..", "datasets", get_env('DATA_FILENAME')))
        return filepath

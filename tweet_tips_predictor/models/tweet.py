""" Model responsible for the Tweet model class. """

from datetime import datetime
from dateutil.parser import parse
from tweet_tips_predictor.database import DB
from tweet_tips_predictor.predictor import TipPredictor

class Tweet:
    """ Class responsible for the Tweet class model. """

    COLLECTION = 'tweets'

    def __init__(self, text, tipster, is_tip=False, created_at=None):
        self._id = None
        self.created_at = None
        self.text = text
        self.tipster = tipster
        self.is_tip = is_tip
        self.prediction = False
        self.is_evaluated = False
        self._set_created_at(created_at)

    def predict(self):
        """ Predict using the TipPredictor model if the text is a tip or not. """
        predictor = TipPredictor(Tweet.all())
        prediction = predictor.predict(self.text)
        self.prediction = prediction

    def _set_created_at(self, created_at):
        if created_at is None:
            self.created_at = datetime.utcnow()
        else:
            if isinstance(created_at, str):
                self.created_at = parse(created_at)
            elif isinstance(created_at, datetime):
                self.created_at = created_at

    def insert(self):
        """ Insert data into tweets collection. """
        result = DB.insert(collection=Tweet.COLLECTION, data=self.dict())
        self._id = result.inserted_id
        if self._id:
            return result
        return False

    def update(self):
        """ Update the tweet data.  """
        if self._id:
            result = DB.find_one_and_update(
                collection=Tweet.COLLECTION,
                _id=self._id,
                data=self.dict())
            return result
        return False

    def delete(self):
        """ Delete the tweet. """
        if self._id:
            result = DB.delete_one(collection=Tweet.COLLECTION, _id=self._id)
            self._id = None
            return result
        return False


    def dict(self):
        """ Return the dict representation of the Tweet. """
        return {
            'created_at': self.created_at,
            'text': self.text,
            'tipster': self.tipster,
            'is_tip': self.is_tip,
            'prediction': self.prediction,
            'is_evaluated': self.is_evaluated
        }

    def get_id(self):
        """ Return the protected attribute _id """
        return self._id

    @staticmethod
    def all():
        """ Return all data from tweets. """
        return list(DB.get_all(Tweet.COLLECTION))

    @staticmethod
    def delete_all():
        """ Delete all from model collection. """
        return DB.clean_data(Tweet.COLLECTION)

    @staticmethod
    def last():
        """ Get the last tweet inserted on database. """
        return DB.get_last(Tweet.COLLECTION)

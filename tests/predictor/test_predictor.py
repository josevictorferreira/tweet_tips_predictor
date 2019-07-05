""" Test module responsible for testing the Predictor module. """

import pandas
from tweet_tips_predictor.models.tweet import Tweet
from tweet_tips_predictor.database import DB
from tweet_tips_predictor.predictor import TipPredictor
from tweet_tips_predictor.seed import seed_collection_with_csv
from tweet_tips_predictor import utils

class TestPredictor():
    """ Class module responsible for testing the Predictor module. """

    @classmethod
    def setup_class(cls):
        """ Setups the TipPredictor object for using in the test methods. """
        DB.init(utils.get_env('MONGODB_DATABASE_TEST'))
        seed_collection_with_csv(utils.get_env('DATA_FILENAME'))
        cls.predictor = TipPredictor(Tweet.all())

    def test_predictor_is_initialized(self):
        """ Tests if the predictor is instance of TipPredictor class. """
        assert isinstance(self.predictor, TipPredictor)

    def test_dataframe_loaded(self):
        """ Tests if the predictor dataset is a panda DataFrame. """
        assert isinstance(self.predictor.dataset, pandas.DataFrame)

    def test_dataset_has_data(self):
        """ Tests if the text is a string. """
        assert isinstance(self.predictor.dataset.iloc[0]['text'], str)

    def test_prediction_is_boolean(self):
        """ Tests if the predict is a boolean value. """
        assert isinstance(self.predictor.predict("Blá Blá"), bool)

    def test_prediction_with_normal_text(self):
        """ Tests if a random text is predicted accordingly as false. """
        assert self.predictor.predict("A simple text with no meaning.") is False

    def test_prediction_with_tip_text(self):
        """ Tests if a tip text is predicted as true. """
        assert self.predictor.predict(
            "Single ✔ Estonia 🇪🇪 Esiliiga B 5pm Keila JK" + \
            " vs Viimsi JK 📍Over 2.5 Goals") is True

    @classmethod
    def teardown_class(cls):
        """
        Clear all data in test collection.
        """
        Tweet.delete_all()

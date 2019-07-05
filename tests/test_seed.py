""" Test the seed database to MongoDB collection. """

from tweet_tips_predictor.seed import seed_collection_with_csv
import tweet_tips_predictor.utils as utils
from tweet_tips_predictor.models.tweet import Tweet
from tweet_tips_predictor.database import DB

def setup_module():
    """ Setup module seeding the MongoDB Collection. """
    DB.init('tweets_test')
    seed_collection_with_csv(utils.get_env('DATA_FILENAME'))

def test_seeded_data():
    """ Test if there are data in the collection. """
    assert Tweet.all()

def teardown_module():
    """ Clearing all data from collection after tests were runned. """
    Tweet.delete_all()

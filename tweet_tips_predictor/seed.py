"""
Module responsible for seeding the database collecction with
the database data.
"""

import pandas
from tweet_tips_predictor.models.tweet import Tweet
import tweet_tips_predictor.utils as utils

def seed_collection_with_csv(filename, debug=False):
    """ Fill all the collection with all data present in CSV. """
    data = pandas.read_csv(utils.dataset_path(filename), sep=";")
    if debug:
        print("Starting seed the data.")
    for index, row in data.iterrows():
        if debug:
            print("Adding row {} to database.".format(index))
        tweet = Tweet(
            row['text'],
            row['tipster'],
            is_tip=bool(row['is_tip']),
            created_at=row['created_at']
        )
        tweet.insert()
    if debug:
        print("Finished seeding database.")

def run_seed(debug=False):
    """ Perform the seed of the collection in case of there is no data in dev collection. """
    if not Tweet.all():
        seed_collection_with_csv(utils.get_env('DATA_FILENAME'), debug=debug)

""" Responsible for the mongodb connection. """

import pymongo
from tweet_tips_predictor.utils import get_env

class DB:
    """ Database class responsible for the mongodb connection. """

    URI = get_env("MONGODB_URI")

    @staticmethod
    def init(database):
        """ Init the database. """
        client = pymongo.MongoClient(DB.URI)
        DB.CLIENT = client
        DB.DATABASE = client[database]
        DB.NAME = database

    @staticmethod
    def insert(collection, data):
        """ Insert data in a collection. """
        return DB.DATABASE[collection].insert_one(data)

    @staticmethod
    def find_one(collection, query):
        """ Find one query inside a collection. """
        return DB.DATABASE[collection].find_one(query)

    @staticmethod
    def get_last(collection):
        """ Return the last inserted data in collection. """
        return list(DB.DATABASE[collection].find().sort([('created_at', -1)]).limit(1))[0]

    @staticmethod
    def find_one_and_update(collection, _id, data):
        """ Find one record and update it. """
        return DB.DATABASE[collection].find_one_and_update({"_id": _id}, {"$set": data})

    @staticmethod
    def delete_one(collection, _id):
        """ Remove a specific data from a collection. """
        return DB.DATABASE[collection].delete_one({"_id": _id})

    @staticmethod
    def get_all(collection):
        """ Get all data in a specific collection. """
        return DB.DATABASE[collection].find({})

    @staticmethod
    def clean_data(collection):
        """ Clean all data in the collection. """
        return DB.DATABASE[collection].delete_many({})

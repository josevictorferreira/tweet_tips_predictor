""" Config module responsible for setting flask settings variables.
"""

from tweet_tips_predictor.utils import get_env

class Config(): # pylint: disable=too-few-public-methods
    """ Main config class responsible for the main settings of the application.
    """
    DEBUG = False
    TESTING = False
    APP_HOST = get_env("APP_HOST")
    APP_PORT = int(get_env("APP_PORT"))
    PERMITTED_REMOTES = get_env("PERMITTED_REMOTES").split(",")
    DATA_FILENAME = get_env("DATA_FILENAME") or "tweets.csv"
    MONGODB_DATABASE = get_env("MONGODB_DATABASE")
    SERVER_NAME = get_env("APP_HOST") + ":" + get_env("APP_PORT")

class DevelopmentConfig(Config): # pylint: disable=too-few-public-methods
    """ Config class for the development environment.
    """
    DEBUG = True

class TestingConfig(Config): # pylint: disable=too-few-public-methods
    """ Config class for the testing environment.
    """
    DEBUG = True
    TESTING = True
    MONGODB_DATABASE = get_env("MONGODB_DATABASE_TEST")

class ProductionConfig(Config): # pylint: disable=too-few-public-methods
    """ Config class for the production environment.
    """
    DEBUG = False
    TESTING = False

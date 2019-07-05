"""
Module responsible for setting the fixtures to be loaded before the pytest
tests.
"""

import pytest
from tweet_tips_predictor import create_app
from tweet_tips_predictor.database import DB
from tweet_tips_predictor.utils import get_env
from tweet_tips_predictor.seed import seed_collection_with_csv

@pytest.yield_fixture
def app():
    """ Create a Flask app context for the test. """

    def _app(config_class):
        _app = create_app(config_class)
        seed_collection_with_csv(_app.config['DATA_FILENAME'])
        _app.app_context().push()
        return _app

    yield _app('config.TestingConfig')

@pytest.yield_fixture
def mongodb():
    """ Pass a mongodb and clean data after the test is runned."""
    DB.init(get_env('MONGODB_DATABASE_TEST'))
    yield DB
    DB.clean_data('tweets')

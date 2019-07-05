""" Test module responsible for testing the project setup configuration
"""

from tweet_tips_predictor.utils import get_env

def test_main_configs(app):
    """ Test if required environment variables are set.
    """
    assert app.config['DEBUG']
    assert app.config['TESTING']
    assert isinstance(app.config['APP_HOST'], str)
    assert isinstance(app.config['APP_PORT'], int)
    assert isinstance(app.config['PERMITTED_REMOTES'], list)
    assert isinstance(app.config['DATA_FILENAME'], str)

def test_development_config(app):
    """ Test if development environment config variables are set.
    """
    app.config.from_object('config.DevelopmentConfig')
    assert app.config['DEBUG']
    assert not app.config['TESTING']
    assert app.config['MONGODB_DATABASE'] == get_env("MONGODB_DATABASE")

def test_testing_config(app):
    """ Test if testing environment config variables are set.
    """
    app.config.from_object('config.TestingConfig')
    assert app.config['DEBUG']
    assert app.config['TESTING']
    assert not app.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    assert app.config['MONGODB_DATABASE'] == get_env("MONGODB_DATABASE_TEST")

def test_production_config(app):
    """ Test if production environment config variables are set.
    """
    app.config.from_object('config.ProductionConfig')
    assert not app.config['DEBUG']
    assert not app.config['TESTING']
    assert app.config['MONGODB_DATABASE'] == get_env("MONGODB_DATABASE")

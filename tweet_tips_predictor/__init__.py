""" Main TweetTipsPredictor module.
"""

from flask import Flask
from tweet_tips_predictor.database import DB

__version__ = '0.1.0'

def create_app(config_name):
    """ Create and return the flask app.
    """
    app = Flask(__name__)
    app.config.from_object(config_name)
    DB.init(app.config['MONGODB_DATABASE'])
    from tweet_tips_predictor.main import BP as main_bp
    app.register_blueprint(main_bp)
    return app

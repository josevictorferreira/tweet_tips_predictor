""" Main module responsible for setting the Blueprint for use and set the routes
of the application.
"""

from flask import Blueprint

BP = Blueprint('main', __name__)

from tweet_tips_predictor.main import routes

"""
WSGI runner file.
"""

from tweet_tips_predictor import create_app
from tweet_tips_predictor.utils import get_config_object

application = create_app(get_config_object())

if __name__ == '__main__':
    application.run()

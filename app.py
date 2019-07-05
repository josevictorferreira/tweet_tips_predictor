"""
Module responsible to run the web server.
"""

from tweet_tips_predictor import create_app
from tweet_tips_predictor.seed import run_seed

if __name__ == '__main__':
    APP = create_app('config.DevelopmentConfig')
    run_seed(debug=True)
    APP.run(
        host=APP.config["APP_HOST"],
        port=APP.config["APP_PORT"]
    )

"""
Module responsible for setting all routes methods in the BPlication.
"""

from flask import request, jsonify, json, current_app
from tweet_tips_predictor.main import BP
from tweet_tips_predictor.models.tweet import Tweet

@BP.before_app_request
def validate_remote():
    """
    Function responsible for the remote address validation before each
    request.
    """
    if not request.remote_addr in current_app.config["PERMITTED_REMOTES"]:
        message = {
            "status": 401,
            "message": "Unauthorized, only permitted remotes can request."
        }
        resp = jsonify(message)
        resp.status_code = 401
        return resp
    return None

@BP.app_errorhandler(404)
def page_not_found(error):
    """
    The errorhandler responsible for the 404 pages.
    If the page is not found, returns 404 status and the 'Not found message'.
    """
    message = {
        "status": 404,
        "message": str(error)
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@BP.route("/predict", methods=["POST"])
def predict():
    """
    The predict endpoint, receives the form with the text param
    and returns the result prediction.
    """
    text = json.loads(request.data)['text']
    tipster = json.loads(request.data)['tipster']
    tweet = Tweet(text, tipster)
    tweet.predict()
    tweet.insert()
    message = {
        "status": 200,
        "result": tweet.prediction
    }
    resp = jsonify(message)
    resp.status_code = 200
    return resp

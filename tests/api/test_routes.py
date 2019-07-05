""" Test module responsible for testing the webserver API routes.
"""

from datetime import datetime
from flask import json
from tweet_tips_predictor.utils import get_env
from tweet_tips_predictor.models.tweet import Tweet

def test_unauthorized_remote(app):
    """ Checks if the unauthorized response are given for a not permitted
    remote address. It should check a random route and the predict route.
    """
    test_client = app.test_client()
    app.config.update(
        PERMITTED_REMOTES="192.168.0.1"
    )
    resp = test_client.post(
        "/predict",
        data=json.dumps({"text": "A random text."}),
        content_type='application/json')
    data = json.loads(resp.get_data(as_text=True))
    assert resp.status_code == 401
    assert data['status'] == 401
    assert data['message'] == "Unauthorized, only permitted remotes can request."
    resp = test_client.get("/random_route")
    data = json.loads(resp.get_data(as_text=True))
    assert resp.status_code == 401
    assert data['status'] == 401
    assert data['message'] == "Unauthorized, only permitted remotes can request."
    app.config.update(
        PERMITTED_REMOTES=get_env("PERMITTED_REMOTES")
    )

def test_page_not_found(app):
    """ Checks if the page not found response for a route that does not exists.
    """
    test_client = app.test_client()
    resp = test_client.get("/random_route")
    data = json.loads(resp.get_data(as_text=True))
    assert resp.status_code == 404
    assert data['status'] == 404
    assert data['message'] == "404 Not Found: The requested URL was not found on " \
        "the server. If you entered the URL manually please check your spelling and " \
        "try again."

def test_prediction(app):
    """ Checks if the webserver returns the correct status code for the /predict route.
    Also checks if the result is boolean.
    """
    test_client = app.test_client()
    resp = test_client.post(
        "/predict",
        data=json.dumps({"text": "A random text.", "tipster": "Myself"}),
        content_type='application/json')
    data = json.loads(resp.get_data(as_text=True))
    assert resp.status_code == 200
    assert data['status'] == 200
    assert isinstance(data['result'], bool)
    tweet = Tweet.last()
    assert tweet['text'] == "A random text."
    assert not tweet['is_tip']
    assert isinstance(tweet['created_at'], datetime)
    assert isinstance(tweet['prediction'], bool)

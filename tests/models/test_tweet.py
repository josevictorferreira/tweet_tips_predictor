""" Test module responsible for testing the main functions of persisting data.
"""

from tweet_tips_predictor.models.tweet import Tweet

def test_create_tweet(mongodb):
    """
    Test the Tweet creating and find if is stored in the MongoDB collection.
    """
    tweet = Tweet('A random text with no meaning', 'Myself')
    result = tweet.insert()
    saved_tweet = mongodb.find_one("tweets", {"_id": result.inserted_id})
    assert result.acknowledged
    assert saved_tweet['text'] == 'A random text with no meaning'
    assert saved_tweet['tipster'] == 'Myself'

def test_update_tweet(mongodb):
    """
    Test updating a tweet and find if is corrected stored in the MongoDB collection.
    """
    tweet = Tweet('A random text with no meaning', 'Myself')
    tweet.insert()
    tweet.text = "A random text with meaning"
    tweet.tipster = "Not Myself"
    tweet.is_tip = True
    tweet.prediction = True
    tweet.is_evaluated = True
    tweet.update()
    saved_tweet = mongodb.find_one("tweets", {"_id": tweet.get_id()})
    assert saved_tweet['text'] == "A random text with meaning"
    assert saved_tweet['tipster'] == "Not Myself"
    assert saved_tweet['is_tip'] is True
    assert saved_tweet['prediction'] is True
    assert saved_tweet['is_evaluated'] is True

def test_delete_tweet(mongodb):
    """
    Test deleting a Tweet and checking if is not on database.
    """
    tweet = Tweet('A random text with no meaning', 'Myself')
    tweet.insert()
    _id = tweet.get_id()
    tweet.delete()
    assert tweet.get_id() is None
    saved_tweet = mongodb.find_one("tweets", {"_id": _id})
    assert saved_tweet is None

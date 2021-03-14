import tweepy as twitter
import keys
import time, datetime

auth = twitter.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)
api = twitter.API(auth)

id = 135124535732525734637


def tweet(text, id):
    api.update_status(text, id)                 # 2 arguments means that function responds to tweet, 1 argument mens its original tweet

tweet("Hello world this is a Twitter post!")


def favorite(id):
    api.create_favorite(id)

favorite(id)



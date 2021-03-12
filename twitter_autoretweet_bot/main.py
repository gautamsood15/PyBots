import tweepy as twitter
import keys
import time, datetime

auth = twitter.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)
api = twitter.API(auth)


def twitter_bot(hashtag, delay):
    while True:
    print(f"\n{datetime.datetime.now()}\n")

    for




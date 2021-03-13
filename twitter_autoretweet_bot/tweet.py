import tweepy as twitter
import keys
import time, datetime

auth = twitter.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)
api = twitter.API(auth)




def tweet(text):
    api.update_status(text)

tweet("Hello world this is a Twitter post!")


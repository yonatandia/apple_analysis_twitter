import tweepy
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

class TwitterClient:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        self.auth.set_access_token = (ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    def fetch_tweets(self, query, count):
        tweets = self.api.search_tweets(q=query, count=count, lang='en', tweet_mode='extended')
        return [tweet.full_text for tweet in tweets]
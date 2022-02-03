
"""
THIS TEST DOES NOT WORK
"""
import requests
import config
import tweepy as tw
from george import George

TWITTER_CLIENT = config.twittersecret
TWITTER_KEY = config.twitterkey
TWITTER_ACCESS_SECRET = config.twitteracceesssecret
TWITTER_ACCESS_KEY = config.twitteraccess

class TwitterData:
    def __init__(self, term):
        self.api = self.createApi()
        self.term = term
        self.tweets_list = []
        self.result = self.analysis_tweets()

    def createApi(self):
        auth = tw.OAuthHandler(TWITTER_KEY, TWITTER_CLIENT)
        auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
        return tw.API(auth)

    def getTweets(self):
        for tweet in self.api.search_tweets(q=self.term,count=100,lang="en", since="2017-04-03").items():
                self.tweets_list.append(tweet.text)

    def analysis_tweets(self):
        analysis = George(self.tweets_list)
        return analysis

    def __str__(self):
        return "{}".format(self.result)


if __name__ == "__main__":
    bot = TwitterData("Liverpool")
    print(bot)
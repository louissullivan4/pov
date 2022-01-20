import requests
import config
# import tweepy
import tweepy as tw

import pandas as pd
import csv
import preprocessor as p

TWITTER_CLIENT = config.twittersecret
TWITTER_KEY = config.twitterkey
TWITTER_ACCESS_SECRET = config.twitteracceesssecret
TWITTER_ACCESS_KEY = config.twitteraccess

def get_tweets():
        auth = tw.OAuthHandler(TWITTER_KEY, TWITTER_CLIENT)
        auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
        api = tw.API(auth)
        csvFile = open('ua.csv', 'a')
        csvWriter = csv.writer(csvFile)
        for tweet in api.search_tweets(q="#unitedAIRLINES",count=100,lang="en", since="2017-04-03").items():
                print(tweet.created_at, tweet.text)
                csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

get_tweets()
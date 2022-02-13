import praw
import sys
from keys import *
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import requests

def search(category, keyword):
    reddit = praw.Reddit(client_id=client_id(), client_secret=client_secret(), user_agent=user_agent())

    if (len(sys.argv)>1):
        category=(sys.argv[1])

    if (len(sys.argv)>2):
        keyword=(sys.argv[2])

    subreddit = reddit.subreddit(category)

    resp = subreddit.search(keyword,limit=15) # num of searches returned

    list_of_items = []
    fields = ('title', 'url', 'score', 'id', 'selftext')

    for submission in resp:
        to_dict = vars(submission)
        sub_dict = {field:to_dict[field] for field in fields}
        list_of_items.append(sub_dict)
        print ("=ID: %s" % submission.id)
        print ("  Title: %s" % submission.title.encode('ascii', 'ignore'))
        print ("  Score: %s"% submission.score)
        print ("  URL: %s"% submission.url.encode('ascii', 'ignore'))
        print ("  Text: %s"% submission.selftext[:120].encode('ascii', 'ignore'))

    json_str = json.dumps(list_of_items)
    with open('reddit_search.json', 'w') as outfile:
        outfile.write(json_str)

search("gaming", "valorant")
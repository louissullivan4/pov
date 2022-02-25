import json
# from turtle import up, update
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from pprint import pprint
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import praw
from keys import *

# maths imports
# import matplotlib.pyplot as plt
# import numpy as np
# import imp
# from IPython import display
# import math
# import re
# import seaborn as sns
# sns.set(style='darkgrid', context='talk', palette='Dark2')

def reddit_search(searchterm, category, id, secret, user):
    sia = SIA()
    results = []
    reddit = praw.Reddit(client_id=id, client_secret=secret, user_agent=user)
    headlines = set()
    new_json = {}

    if category == "game" or category == "Game":
        subreddit = "gaming"
    elif category == "Sport" or category == "sport":
        subreddit = "sports"
    elif category == "Travel" or category == "travel":
        subreddit = "travel"

    try:
        subreddit = reddit.subreddit(subreddit)
        resp = subreddit.search(searchterm,limit=None) # num of searches returned
        json_out = {}

        for submission in resp:
            headlines.add(submission.title)
            # print(len(headlines))

        for line in headlines:
            pol_score = sia.polarity_scores(line)
            pol_score['headline'] = line
            results.append(pol_score)

        # pprint(results[:3], width=100)

        df = pd.DataFrame.from_records(results)
        df['label']=0
        df.loc[df['compound']> 0.2, 'label'] = 1 # positive
        df.loc[df['compound']< -0.2, 'label'] = -1 # positive
        df.head()
        # saving csv
        df2 = df[['headline', 'label']]
        # df2.to_csv('reddit_headlines_labels.csv', mode='a', encoding='utf-8', index=False)

        # print("Positive headlines:\n")
        # pprint(list(df[df['label'] == 1].headline)[:5], width=200)
        json_out.update({'Positive headlines': list(df[df['label'] == 1].headline)[:5]})
        # print("Negative headlines:\n")
        # pprint(list(df[df['label'] == -1].headline)[:5], width=200)
        json_out.update({'Negative headlines': list(df[df['label'] == -1].headline)[:5]})
        # print(df.label.value_counts())
        headline_count = df.label.value_counts()
        json_out.update({'Headline count': headline_count.to_json()})
        # print(df.label.value_counts(normalize=True) * 100)
        headline_count_per = df.label.value_counts(normalize=True)
        json_out.update({'Headline count %': headline_count_per.to_json()})

        # bar chart
        # fig, ax = plt.subplots(figsize=(8, 8))
        # counts = df.label.value_counts(normalize=True) * 100
        # sns.barplot(x=counts.index, y=counts, ax=ax)
        # ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
        # ax.set_ylabel("Percentage")
        # plt.show()

        tokenizer = RegexpTokenizer(r'\w+')
        stop_words = stopwords.words('english')
        # word distro
        def process_text(headlines):
            tokens = []
            for line in headlines:
                toks = tokenizer.tokenize(line)
                toks = [t.lower() for t in toks if t.lower() not in stop_words]
                tokens.extend(toks)
            return tokens

        pos_lines = list(df[df.label == 1].headline)
        pos_tokens = process_text(pos_lines)
        pos_freq = nltk.FreqDist(pos_tokens)
        # print(pos_freq.most_common(20))
        json_out.update({'Positive word distro': pos_freq.most_common(20)})

        neg_lines = list(df2[df2.label == -1].headline)
        neg_tokens = process_text(neg_lines)
        neg_freq = nltk.FreqDist(neg_tokens)
        # print(neg_freq.most_common(20))
        json_out.update({'Negative word distro': neg_freq.most_common(20)})

        dict_dump = json_out

        # Status code 
        if len(dict_dump) > 2:
            new_json.update({'status': "200"})

            # Total reviews
            count_str = dict_dump["Headline count"]
            count = json.loads(count_str)
            total_count = 0
            for i, val in count.items():
                total_count += val
            new_json.update({'total_reviews': total_count})

            # Rating
            ratings_str = dict_dump["Headline count %"]
            ratings = json.loads(ratings_str)
            result_rating = 0
            for i, val in ratings.items():
                if i == "0" or i == "1":
                    result_rating += val
            result_rating = int(float(result_rating) * 100)
            new_json.update({'rating': str(result_rating)})

            # Comments and Word Bubble
            if result_rating > 50:
                comments = dict_dump["Positive headlines"]
                new_json.update({'reviews': comments})
                word_bubble = dict_dump["Positive word distro"]
                new_json.update({'word_bubble': word_bubble})
            else:
                comments = dict_dump["Negative headlines"]
                new_json.update({'reviews': comments})
                word_bubble = dict_dump["Negative word distro"]
                new_json.update({'word_bubble': word_bubble})
        else:
            new_json.update({'status': "503"})
            new_json.update({"msg": "Entry unavailable"})

    except Exception as e:
        new_json.update({'status': "503"})
        new_json.update({"msg": "Entry unavailable"})
    return(new_json)

# print(reddit_search("italy", "travel", client_id(), client_secret(), user_agent()))

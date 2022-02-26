from re import sub
import requests
import os
import json
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import nltk
import re
from pprint import pprint
import pandas as pd
from keys import *

bearer_token = bearer_token()

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def remove_emoji(string):
    emoji_pattern = re.compile("["
    u"\U0001F600-\U0001F64F" u"\U0001F680-\U0001F6FF" u"\U0001F1E0-\U0001F1FF" u"\U00002500-\U00002BEF"  
    u"\U00002702-\U000027B0"u"\U00002702-\U000027B0"u"\U000024C2-\U0001F251"u"\U0001f926-\U0001f937"
    u"\U00010000-\U0010ffff"u"\u2640-\u2642"u"\u2600-\u2B55"u"\u200d"u"\u23cf"u"\u23e9"u"\u231a"
    u"\ufe0f"u"\u3030""]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def filter_tweet(tweet):
    newline_remove = tweet.replace("\n", " ")
    rt_remove = re.compile('RT @').sub('@', newline_remove, count=1)
    username_remove = re.sub('@[^\s]+', '', rt_remove)
    filtered = username_remove.strip()
    filtered = " ".join(filtered.split())
    return filtered


def main(searchterm):
    sia = SIA()
    json_out = {}
    headlines = set()
    results = []
    try:
        query_params = {'query': '%s lang:en' %searchterm,
                    #'tweet.fields': 'author_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'max_results': 100,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    }
        search_url = "https://api.twitter.com/2/tweets/search/recent" # recent
        dict_response = connect_to_endpoint(search_url, query_params)
        dict_response = dict(dict_response)

        i = 0
        while i < len(dict_response['data']):
            tweet = dict_response['data'][i]["text"]
            no_emoji = remove_emoji(tweet)
            filtered_tweet = filter_tweet(no_emoji)
            headlines.add(filtered_tweet)
            i += 1

        for line in headlines:
            pol_score = sia.polarity_scores(line)
            pol_score['headline'] = line
            results.append(pol_score)

        df = pd.DataFrame.from_records(results)
        df['label']=0
        df.loc[df['compound']> 0.2, 'label'] = 1 # positive
        df.loc[df['compound']< -0.2, 'label'] = -1 # positive
        df.head()
        df2 = df[['headline', 'label']]
        json_out.update({'Positive headlines': list(df[df['label'] == 1].headline)[:5]})
        json_out.update({'Negative headlines': list(df[df['label'] == -1].headline)[:5]})
        headline_count = df.label.value_counts()
        json_out.update({'Headline count': headline_count.to_json()})
        headline_count_per = df.label.value_counts(normalize=True)
        json_out.update({'Headline count %': headline_count_per.to_json()})

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
        json_out.update({'Positive word distro': pos_freq.most_common(20)})

        neg_lines = list(df2[df2.label == -1].headline)
        neg_tokens = process_text(neg_lines)
        neg_freq = nltk.FreqDist(neg_tokens)
        json_out.update({'Negative word distro': neg_freq.most_common(20)})

        dict_dump = json_out
        new_json = {}
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
            if result_rating > 70:
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
        
if __name__ == "__main__":
    print(main('russia'))
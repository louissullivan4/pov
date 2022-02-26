import requests
import os
import json
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import nltk

# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

# search_url = "https://api.twitter.com/2/tweets/search/recent"
# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
# query_params = {'query': 'xbox lang:en',
#                 #'tweet.fields': 'author_id',
#                 'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
#                 'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
#                 'max_results': 10,
#                 'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
#                 'user.fields': 'id,name,username,created_at,description,public_metrics,verified'
#                 }


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


def main(searchterm):
    sia = SIA()
    query_params = {'query': '%s lang:en' %searchterm,
                #'tweet.fields': 'author_id',
                'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                'max_results': 10,
                'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                'user.fields': 'id,name,username,created_at,description,public_metrics,verified'
                }
    search_url = "https://api.twitter.com/2/tweets/search/recent" # recent
    dict_response = connect_to_endpoint(search_url, query_params)
    dict_response = dict(dict_response)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    text = []
    for tweet_list in dict_response["data"]:
        for tag in tweet_list:
            if tag == 'text':
                text.append(tweet_list[tag])

    pol_dict = {1:[], -1:[], 0:[]}
    for line in text:
        pol_score = sia.polarity_scores(line)
        if pol_score == 1:
            pol_dict[1].append(line)
        elif pol_score == -1:
            pol_dict[-1].append(line)
        else:
            pol_dict[0].append(line)
    
    # headline counts
    pos_count = len(pol_dict[1])
    neg_count = len(pol_dict[-1])
    neu_count = len(pol_dict[0])
    tot_count = pos_count + neg_count + neu_count
    pol_percent = {}
    pol_percent.update({1: (pos_count/tot_count)*100})
    pol_percent.update({-1: (neg_count/tot_count)*100})
    pol_percent.update({0: (neu_count/tot_count)*100})
    dict_response.update({'Headline count %': pol_percent})
    pol_count = {}
    pol_count.update({1: pos_count})
    pol_count.update({-1: neg_count})
    pol_count.update({0: neu_count})
    dict_response.update({'Headline count': pol_count})
    
    pos_tokens = process_text(pol_dict[1])
    pos_freq = nltk.FreqDist(pos_tokens)
    dict_response.update({'Positive word distro': pos_freq.most_common(20)})

    neg_tokens = process_text(pol_dict[-1])
    neg_freq = nltk.FreqDist(neg_tokens)
    dict_response.update({'Negative word distro': neg_freq.most_common(20)})
    
    print(json.dumps(dict_response, indent=4, sort_keys=True))
    return json.dumps(dict_response, indent=4, sort_keys=True)

def process_text(text):
    tokenizer = RegexpTokenizer(r'\w+')
    stop_words = stopwords.words('english')
    tokens = []
    for line in text:
        toks = tokenizer.tokenize(line)
        toks = [t.lower() for t in toks if t.lower() not in stop_words]
        tokens.extend(toks)
    return tokens

def csv_anal():
    import pandas as pd
    df = pd.read_csv('xbox.csv')
    df.head()
    from pprint import pprint
    df['label']=0
    df.loc[df['compound']> 0.2, 'label'] = 1 # positive
    df.loc[df['compound']< 0.2, 'label'] = -1 # positive
    df.head()
    # df2 = df[['headline', 'label']]
    print("Positive headlines:\n")
    pprint(list(df[df['label'] == 1].headline)[:5], width=200)

    print("Negative headlines:\n")
    pprint(list(df[df['label'] == -1].headline)[:5], width=200)



if __name__ == "__main__":
#    csv_anal()
    main('xbox')
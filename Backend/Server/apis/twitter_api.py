import requests
import os
import json
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': '#xbox','tweet.fields': 'author_id'}


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


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))

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
    #csv_anal()
    main()
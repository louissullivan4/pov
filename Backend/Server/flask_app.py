from flask import Flask
import json

from apis.amazon_api import AmazonData
from apis.imdb_api import ImdbData
from apis.reddit_api import reddit_search
from apis.twitter_api import twitter_search

from keys import *

app = Flask(__name__)
@app.route('/')
def welcome():
    homepage = """
        <br>
        <p>Welcome to POV's backend server. Use a correct endpoint to access our data.</p>
        <br>
        <p>List of API endpoints:</p>
        <ul>
            <li><a href="/pov/results/dune/movie">Movie Dune result</a></li>
            <li><a href="/pov/results/playstation5/product">Product Playstation5 result</a></li>
        </ul>
    """
    return homepage

@app.route('/pov/results/<string:term>/<string:category>')
def results(term: str, category: str):
    term = term.upper().strip()
    term = term.replace(" ", "")
    reddit_list = ['game', 'music', 'sport', 'travel']
    twitter_list = ['celebrity', 'politics']
    if category == "product":
        variables = AmazonData(term).getResult()
    elif category == "movie":
        variables = ImdbData(term).getResult()
    elif category in reddit_list:
        variables = reddit_search(term, category, client_id(), client_secret(), user_agent())
    elif category in twitter_list:
        variables = twitter_search(term)
    else:
        variables = {"status" : "503", "msg" : "Unavailable on all APIs"}
    app_json = json.dumps(variables)
    return app_json


if __name__ == "__main__":
    app.run()
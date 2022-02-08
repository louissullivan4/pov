from flask import Flask
import json
from apis.amazon_api import AmazonData
from apis.imdb_api import ImdbData

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
    if category == "product":
        tryApi = AmazonData(term).getResult()
    elif category == "movie":
        tryApi = ImdbData(term).getResult()
    else:
        tryApi = 503
    if tryApi == 503:
        #HERE WE WILL USE TWITTER OR REDDIT
        variables = {"result" : "200", "msg" : "Here we will use twitter or reddit"}
    else:
        variables = tryApi
    app_json = json.dumps(variables)
    return app_json


if __name__ == "__main__":
    app.run()

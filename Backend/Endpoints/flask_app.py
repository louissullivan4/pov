from flask import Flask
import json

app = Flask(__name__)
@app.route('/')
def welcome():
    homepage = """
        <br>
        <p>Welcome to Louis' API prototype. Use a correct endpoint to access our data.</p>
        <br>
        <p>List of API endpoints:</p>
        <ul>
            <li><a href="/amazon/asin/Playstation5">Amazon Playstation5 asin</a></li>
            <li><a href="/amazon/reviews/B08H95Y452">Amazon Playstation5 reviews</a></li>
            <li><a href="/imdb/id/Dune">IMDB Dune ID</a></li>
            <li><a href="/imdb/rating/tt1160419">IMDB Dune Reviews</a></li>
        </ul>
    """
    return homepage


@app.route('/amazon/asin')
def no_product():
    return "<p>Error: You have no passed any values to be searched...</p>"

@app.route('/amazon/asin/<string:term>')
def asin_val(term: str):
    term = term.lower().strip()
    term = term.replace(" ", "")
    if term == "playstation5":
        json_file = open("/home/louissullivcs/mysite/json/amazon_asin.json")
        variables = json.load(json_file)
        json_file.close()
    else:
        variables = "<p>Error: Value passed not available...</p>"
    return variables

@app.route('/amazon/reviews')
def no_review():
    return "<p>Error: You have no passed any values to be searched...</p>"

@app.route('/amazon/reviews/<string:term>')
def review_val(term: str):
    term = term.upper().strip()
    term = term.replace(" ", "")
    if term == "B08H95Y452":
        json_file = open("/home/louissullivcs/mysite/json/amazon_reviews.json")
        variables = json.load(json_file)
        json_file.close()
    else:
        variables = "<p>Error: Value passed not available...</p>"
    return variables

@app.route('/imdb/id')
def no_movie():
    return "<p>Error: You have no passed any values to be searched...</p>"

@app.route('/imdb/id/<string:term>')
def id_val(term: str):
    term = term.lower().strip()
    term = term.replace(" ", "")
    if term == "dune":
        json_file = open("/home/louissullivcs/mysite/json/imdb_id.json")
        variables = json.load(json_file)
        json_file.close()
    else:
        variables = "<p>Error: Value passed not available...</p>"
    return variables

@app.route('/imdb/rating')
def no_rating():
    return "<p>Error: You have no passed any values to be searched...</p>"

@app.route('/imdb/rating/<string:term>')
def rating_val(term: str):
    term = term.lower().strip()
    term = term.replace(" ", "")
    if term == "tt1160419":
        json_file = open("/home/louissullivcs/mysite/json/imdb_movie_rating.json")
        variables = json.load(json_file)
        json_file.close()
    else:
        variables = "<p>Error: Value passed not available...</p>"
    return variables

if __name__ == "__main__":
    app.run()
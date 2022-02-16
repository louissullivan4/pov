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
        <br><br>
        <p>Amazon:</p>
        <ul>
            <li><a href="/amazon/asin/Playstation5">Amazon Playstation5 asin</a></li>
            <li><a href="/amazon/reviews/B08H95Y452">Amazon Playstation5 reviews</a></li>
            <li><a href="/amazon/asin/Applewatch7">Amazon Apple Watch 7 asin</a></li>
            <li><a href="/amazon/reviews/B09HH9GWYZ">Amazon Apple Watch 7 reviews</a></li>
            <li><a href="/amazon/asin/Lindorchocolate">Amazon Lindor Chocolate asin</a></li>
            <li><a href="/amazon/reviews/B00NW479QO">Amazon Lindor Chocolate reviews</a></li>
            <li><a href="/amazon/asin/Potnoodle">Amazon Pot Noodle asin</a></li>
            <li><a href="/amazon/reviews/B007XR2IOE">Amazon Pot Noodle reviews</a></li>
        </ul>
        <p>IMDB:</p>
        <ul>
            <li><a href="/imdb/id/Dune">IMDB Dune ID</a></li>
            <li><a href="/imdb/rating/tt1160419">IMDB Dune Reviews</a></li>
            <li><a href="/imdb/id/Inception">IMDB Inception ID</a></li>
            <li><a href="/imdb/rating/tt1375666">IMDB Inception Reviews</a></li>
            <li><a href="/imdb/id/jackandjill">IMDB Jack&Jill ID</a></li>
            <li><a href="/imdb/rating/tt0810913">IMDB Jack&Jill Reviews</a></li>
            <li><a href="/imdb/id/Insideout">IMDB Inside Out ID</a></li>
            <li><a href="/imdb/rating/tt2096673">IMDB Inside Out Reviews</a></li>

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
        json_file = open("/home/louissullivcs/mysite/json/amazon/amazon_playstation5_asin.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "applewatch7":
        json_file = open("/home/louissullivcs/mysite/json/amazon/amazon_applewatch7_asin.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "lindorchocolate":
        json_file = open("/home/louissullivcs/mysite/json/amazon/amazon_lindor_asin.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "potnoodle":
        json_file = open("/home/louissullivcs/mysite/json/amazon/amazon_potnoodle_asin.json")
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
        json_file = open("/home/louissullivcs/mysite/json/amazon/amazon_playstation5_reviews.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "B09HH9GWYZ":
        json_file = open("/home/louissullivcs/mysite/json/amazon/amazon_applewatch7_reviews.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "B00NW479QO":
        json_file = open("/home/louissullivcs/mysite/json/amazon/amazon_lindor_reviews.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "B007XR2IOE":
        json_file = open("/home/louissullivcs/mysite/json/amazon/amazon_potnoodle_reviews.json")
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
        json_file = open("/home/louissullivcs/mysite/json/imdb/imdb_dune_id.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "inception":
        json_file = open("/home/louissullivcs/mysite/json/imdb/imdb_inception_id.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "jackandjill":
        json_file = open("/home/louissullivcs/mysite/json/imdb/imdb_jackandjill_id.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "insideout":
        json_file = open("/home/louissullivcs/mysite/json/imdb/imdb_insideout_id.json")
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
        json_file = open("/home/louissullivcs/mysite/json/imdb/imdb_dune_movie_rating.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "tt1375666":
        json_file = open("/home/louissullivcs/mysite/json/imdb/imdb_inception_movie_rating.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "tt2096673":
        json_file = open("/home/louissullivcs/mysite/json/imdb/imdb_jackandjill_movie_rating.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "tt0810913":
        json_file = open("/home/louissullivcs/mysite/json/imdb/imdb_insideout_movie_rating.json")
        variables = json.load(json_file)
        json_file.close()
    else:
        variables = "<p>Error: Value passed not available...</p>"
    return variables

@app.route('/imdb/review/<string:term>')
def rating_val(term: str):
    term = term.lower().strip()
    term = term.replace(" ", "")
    if term == "tt1160419":
        json_file = open("/home/louissullivcs/mysite/json/imdb/imdb_dune_review.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "tt1375666":
        json_file = open("/home/louissullivcs/mysite/json/imdb/imdb_inception_review.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "tt2096673":
        json_file = open("/home/louissullivcs/mysite/json/imdb/imdb_jackandjill_review.json")
        variables = json.load(json_file)
        json_file.close()
    elif term == "tt0810913":
        json_file = open("/home/louissullivcs/mysite/json/imdb/imdb_insideout_review.json")
        variables = json.load(json_file)
        json_file.close()
    else:
        variables = "<p>Error: Value passed not available...</p>"
    return variables

if __name__ == "__main__":
    app.run()
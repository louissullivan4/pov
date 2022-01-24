# import config
import json
from analysis.george import George

# IMDB_KEY = config.imdbkey

class ImdbData:
    def __init__(self, term):
        self.term = term
        self.id = self.get_movie_id()
        self.ratings = self.get_ratings()
        self.result = self.analysis_reviews()

    def get_movie_id(self):
        # as this is test data the api not being callled and so a term is not passed, only get playstation 5
        with open('Backend/APIs/json/imdb_id.json') as fp:
            data = json.load(fp)
            id = data["results"][0]["id"]
            return id[7:-1]
    
    def get_ratings(self):
        with open('Backend/APIs/json/imdb_movie_rating.json') as fp:
            data = json.load(fp)
            reviews = data["rating"]
        return reviews
    
    def analysis_reviews(self):
        result = float(self.ratings) * 10
        result = str(result)
        return result[:-2] + "%"

    def __str__(self):
        return "{}".format(self.result)

if __name__ == "__main__":
    bot = ImdbData("Dune")
    print(bot)

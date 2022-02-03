import requests

"""
Uses data from https://rapidapi.com/apidojo/api/imdb8/
"""

class ImdbData:
    """
    Get movie rating from inputted search term. See Amazon Class for full commments
    *Currently requests to a custom server due to API payment issues*
    """
    def __init__(self, term):
        self.term = term
        self.id = self.get_movie_id()
        self.ratings = self.get_ratings()
        self.result = self.analysis_reviews()

    def get_movie_id(self):
        #
        response = requests.get("https://louissullivcs.pythonanywhere.com/imdb/id/{}".format(str(self.term)))
        response_type = response.headers
        if response_type["Content-Type"] == 'application/json':
            data = response.json()
            #Get movie id from json
            id = data["results"][0]["id"]
            return id[7:-1]
        else:
            return None
    
    def get_ratings(self):
        if self.id != None:
            response = requests.get("https://louissullivcs.pythonanywhere.com/imdb/rating/{}".format(str(self.id)))
            data = response.json()
            #Get rating from json
            reviews = data["rating"]
            return reviews
        else:
            return None
    
    def analysis_reviews(self):
        """
        Converts rating to percentage and returns it as our total
        """
        if self.ratings != None:
            result = float(self.ratings) * 10
            result = str(result)
            return result[:-2] + "%"
        else:
            return "Error: Movie selected is not available..."

    def __str__(self):
        return "{}".format(self.result)

if __name__ == "__main__":
    bot = ImdbData("Dune")
    print(bot)

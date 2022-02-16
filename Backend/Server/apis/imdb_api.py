import requests
import json

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
        self.api_response = ""
        self.id = self.get_movie_id()
        self.rating = self.get_rating()
        self.rating_count = self.get_rating_count()
        self.top_rank = self.get_top_rank()
        self.reviews = self.get_reviews()
        self.result = self.final_result()

    def getResult(self):
        return self.result

    def get_movie_id(self):
        response = requests.get("https://louissullivcs.pythonanywhere.com/imdb/id/{}".format(str(self.term)))
        response_type = response.headers
        if response_type["Content-Type"] == 'application/json':
            data = response.json()
            #Get movie id from json
            id = data["id"]
            return id[7:-1]
        else:
            return None
    
    def get_rating(self):
        if self.id != None:
            response = requests.get("https://louissullivcs.pythonanywhere.com/imdb/rating/{}".format(str(self.id)))
            self.api_response = response.json()
            #Get rating from json
            reviews = self.api_response["rating"]
            result = str(float(reviews) * 10)
            return result[:-2]
        else:
            return None

    def get_rating_count(self):
        if self.id != None:
            count = self.api_response["ratingCount"]
            return str(count)
        else:
            return None

    def get_top_rank(self):
        if self.id != None:
            rank = self.api_response["topRank"]
            return str(rank)
        else:
            return None

    def get_reviews(self):
        if self.top_rank != None:
            response = requests.get("https://louissullivcs.pythonanywhere.com/imdb/review/{}".format(str("tt1160419")))
            response_json = response.json()
            i = 0
            reviews = []
            while i < len(response_json['reviews']):
                reviews.append(response_json["reviews"][i]["reviewTitle"])
                i += 1
            return reviews
        else:
            return None
    
    def final_result(self):
        if self.id != None:
            result_string = '{"status": "200", "rating": "'+str(self.rating)+'"}'
            result = json.loads(result_string)
            count = {"rating_count": self.rating_count}
            rank = {"peak_rank": self.top_rank}
            review = {"reviews": self.reviews}
            result.update(count)
            result.update(rank)
            result.update(review)
            return result
        else:
            result_string = '{"status": "503", "msg": "Entry unavailable"}'
            result = json.loads(result_string)
            return result

    def __str__(self):
        return "{}".format(self.result)

if __name__ == "__main__":
    bot = ImdbData("Dune")
    print(bot)
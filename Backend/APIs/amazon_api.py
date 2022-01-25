# import config
import json
import requests
from analysis.george import George

# AMAZON_KEY = config.azkey
# AZMAZON_SECERT = config.azsecret

class AmazonData:
    def __init__(self, term):
        self.term = term
        self.asin = self.get_product_asin()
        self.ratings = self.get_ratings()
        self.result = self.analysis_reviews()

    def get_product_asin(self):
        response = requests.get("https://louissullivcs.pythonanywhere.com/amazon/asin/{}".format(str(self.term)))
        response_type = response.headers
        if response_type["Content-Type"] == 'application/json':
            data = response.json()
            return data["result"][0]["asin"]
        else:
            return None
    
    def get_ratings(self):
        if self.asin != None:
            response = requests.get("https://louissullivcs.pythonanywhere.com/amazon/reviews/{}".format(str(self.asin)))
            data = response.json()
            reviews = data["stars_stat"]
            return reviews
        else:
            return None
    
    def analysis_reviews(self):
        if self.ratings != None:
            for key, val in self.ratings.items():
                if key == '4':
                    fourstars = val[:-1]
                elif key == "5":
                    fivestars = val[:-1]
                    total = int(fourstars) + int(fivestars)
            return str(total) + "%"
        else:
            return "Error: Amazon Product selected is not available..."

    def __str__(self):
        return "{}".format(self.result)

if __name__ == "__main__":
    bot = AmazonData("Playstation 5")
    print(bot)



"""
These functions use TextBlob to get rating (old)
"""
# def get_product_asin(self, term):
#         # as this is test data the api not being callled and so a term is not passed, only get playstation 5
#         with open('Backend/Test/amazon_asin.json') as fp:
#             data = json.load(fp)
#             return data["result"][0]["asin"]

    
#     def get_reviews(self):
#         # would use asin code here to get the specific product but currently dont as we are using test jsons
#         with open('Backend/Test/amazon_reviews.json') as fp:
#             data = json.load(fp)
#             i = 0
#             reviews = []
#             while i < len(data['result']):
#                 reviews.append(data["result"][i]["review"])
#                 i += 1
#         return reviews
    
#     def analysis_reviews(self):
#         analysis = George(self.reviews_list)
#         return analysis

# import config
import json
from analysis.george import George

# AMAZON_KEY = config.azkey
# AZMAZON_SECERT = config.azsecret

class AmazonData:
    def __init__(self, term):
        self.term = term
        self.asin = self.get_product_asin(self.term)
        self.reviews_list = self.get_reviews()
        self.result = self.analysis_reviews()

    def get_product_asin(self, term):
        # as this is test data the api not being callled and so a term is not passed, only get playstation 5
        with open('Backend/Test/amazon_asin.json') as fp:
            data = json.load(fp)
            return data["result"][0]["asin"]

    def get_reviews(self):
        # would use asin code here to get the specific product but currently dont as we are using test jsons
        with open('Backend/Test/amazon_reviews.json') as fp:
            data = json.load(fp)
            i = 0
            reviews = []
            while i < len(data['result']):
                reviews.append(data["result"][i]["review"])
                i += 1
        return reviews

    def analysis_reviews(self):
        analysis = George(self.reviews_list)
        return analysis

    def __str__(self):
        return "{}".format(self.result)


if __name__ == "__main__":
    bot = AmazonData("Playstation 5")
    print(bot)
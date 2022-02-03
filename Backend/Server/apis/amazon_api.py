import requests
import json

"""
Uses data from https://rapidapi.com/restyler/api/amazon23/
"""
class AmazonData:
    """
    Gets reviews from amazon api using a inputted search term
    *Currently requests to a custom server due to API payment issues*
    """
    def __init__(self, term):
        self.term = term
        self.asin = self.get_product_asin()
        self.ratings = self.get_ratings()
        self.result = self.analysis_reviews()

    def getResult(self):
        return self.result

    def get_product_asin(self):
        """
        Get the related amazon asin (product id) number from the search term
        """
        response = requests.get("https://louissullivcs.pythonanywhere.com/amazon/asin/{}".format(str(self.term))) 
        response_type = response.headers
        #if the value returned is a json file
        if response_type["Content-Type"] == 'application/json':
            #get the json values from what was returned
            data = response.json()
            #get asins value from the first result
            return data["result"][0]["asin"]
        else:
            #else we did not find the value so we return nothing
            return None
    
    def get_ratings(self):
        """
        Get the star ratings of a product from the related asin number
        """
        #if the asin is not none
        if self.asin != None:
            # get the reviews from the custom server using the asin number
            response = requests.get("https://louissullivcs.pythonanywhere.com/amazon/reviews/{}".format(str(self.asin)))
            data = response.json()
            #get the star ratings from the returned json
            reviews = data["stars_stat"]
            return reviews
        else:
            #else we could not find the stars so we return none
            return None
    
    def analysis_reviews(self):
        """
        Return value of 4 and 5 star ratings together, which is our positive rating result
        """
        if self.ratings != None:
            for key, val in self.ratings.items():
                if key == '4':
                    fourstars = val[:-1]
                elif key == "5":
                    fivestars = val[:-1]
                    total = int(fourstars) + int(fivestars)
                    # result_string = '{"status": "'+str(status)+'", "result": "'+str(total)+'%"}'
                    result_string = '{"result": "'+str(total)+'%"}'
                    result = json.loads(result_string)
            return result
        else:
            result_string = '{"result": "Error: Value selected is not available."}'
            result = json.loads(result_string)
            return result


    def __str__(self):
        return "{}".format(type(self.result))

if __name__ == "__main__":
    bot = AmazonData("Playstation 5")
    print(type(bot))
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


# def analysis_reviews(self):
#         """
#         Return value of 4 and 5 star ratings together, which is our positive rating result
#         """
#         if self.ratings != None:
#             status = "200"
#             for key, val in self.ratings.items():
#                 if key == '4':
#                     fourstars = val[:-1]
#                 elif key == "5":
#                     fivestars = val[:-1]
#                     total = int(fourstars) + int(fivestars)
#                     result_string = '{"status": "'+str(status)+'", "result": "'+str(total)+'%"}'
#                     result = json.loads(result_string)
#             return result
#         else:
#             status = "401"
#             result_string = '{"status": "'+str(status)+'", "result": "Error: Amazon Product selected is not available."}'
#             result = json.loads(result_string)
#             return result
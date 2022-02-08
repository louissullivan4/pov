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
        self.api_response = ""
        self.asin = self.get_product_asin()
        self.stars = self.get_stars()
        self.rating = self.get_rating()
        self.reviews = self.get_reviews()
        self.result = self.final_result()

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
    
    def get_stars(self):
        """
        Get the star ratings of a product from the related asin number
        """
        #if the asin is not none
        if self.asin != None:
            # get the reviews from the custom server using the asin number
            response = requests.get("https://louissullivcs.pythonanywhere.com/amazon/reviews/{}".format(str(self.asin)))
            self.api_response = response.json()
            #get the star ratings from the returned json
            reviews = self.api_response["stars_stat"]
            return reviews
        else:
            #else we could not find the stars so we return none
            return None
    
    def get_rating(self):
        """
        Return value of 4 and 5 star ratings together, which is our positive rating result
        """
        if self.asin != None:
            for key, val in self.stars.items():
                if key == '4':
                    fourstars = val[:-1]
                elif key == "5":
                    fivestars = val[:-1]
                    total = int(fourstars) + int(fivestars)
            return total
        else:
            return None

    def get_reviews(self):
        i = 0
        reviews = []
        if self.asin != None:
            while i < len(self.api_response['result']):
                reviews.append(self.api_response["result"][i]["review"])
                i += 1
            return reviews
        else:
            return None
    

    def final_result(self):
        if self.asin != None:
            total_reviews = self.api_response["total_reviews"]
            result_string = '{"rating": "'+str(self.rating)+'", "total_stars": "'+str(self.stars)+'"}'
            result = json.loads(result_string)
            total = {"total_reviews": total_reviews}
            reviews = {"reviews": self.reviews}
            result.update(total)
            result.update(reviews)
            return result
        else:
            result_string = '{"result": "503", "msg": "Entry unavailable"}'
            result = json.loads(result_string)
            return result

    def __str__(self):
        return "{}".format(self.result)

if __name__ == "__main__":
    bot = AmazonData("Playstation 5")
    print(bot)


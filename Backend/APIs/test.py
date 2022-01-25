import requests

def get_product_asin(term):
        # as this is test data the api not being callled and so a term is not passed, only get playstation 5
        response = requests.get("https://louissullivcs.pythonanywhere.com/amazon/asin/{}".format(str(term)))
        val = response.headers
        print(val)
        data = response.json()
        
        print(data["result"][0]["asin"])
        return data["result"][0]["asin"]

term = "playstation 4"
print(term)
vall = get_product_asin(term)

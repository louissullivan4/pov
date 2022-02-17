import requests
import json

term="inception"

result=[]
response = requests.get("https://louissullivcs.pythonanywhere.com/imdb/review/{}".format(str("tt1160419")))
response_json = response.json()
i = 0
reviews = []
while i < len(response_json['reviews']):
    reviews.append(response_json["reviews"][i]["reviewTitle"])
    i += 1
print(reviews)
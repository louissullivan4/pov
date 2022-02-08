import requests
import json

response = requests.get("https://louissullivcs.pythonanywhere.com/amazon/reviews/B08H95Y452")
api_response = response.json()
reviews = api_response["total_reviews"]
print(reviews)
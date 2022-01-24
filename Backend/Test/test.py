import json
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_product_asin():
    with open('Backend/Test/amazon_asin.json') as fp:
        data = json.load(fp)
        return data["result"][0]["asin"]

def get_ratings():
    with open('Backend/Test/amazon_reviews.json') as fp:
        data = json.load(fp)
        reviews = data["stars_stat"]
    return reviews

dict1 = get_ratings()

print(dict1)

















# def correct_spelling(list1):
#     newlist = []
#     for val in list1:
#         val = TextBlob(val)
#         spelled = val.correct()
#         newlist.append(str(spelled))
#     return newlist


# def getSentiments(list1):
#         sid_obj = SentimentIntensityAnalyzer()
#         for val in list1:
#             sentiment_dict = sid_obj.polarity_scores(val)
#             print("Overall sentiment dictionary is : ", sentiment_dict)
#             if sentiment_dict['compound'] >= 0.05 :
#                 print(val + "\tPositive")
#             elif sentiment_dict['compound'] <= - 0.05 :
#                 print(val + "\tNegative")
#             else :
#                 print(val + "\tNeutral")
#             print("\n")
        
# newlist = []
# newlist = correct_spelling(list1)
# # print(newlist)
# getSentiments(newlist)

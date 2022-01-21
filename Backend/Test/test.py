import json

def get_product_asin():
    with open('Backend/Test/amazon_asin.json') as fp:
        data = json.load(fp)
        return data["result"][0]["asin"]

def get_reviews():
    with open('Backend/Test/amazon_reviews.json') as fp:
        data = json.load(fp)
        i = 0
        reviews = []
        while i < len(data['result']):
            reviews.append(data["result"][i]["review"])
            i += 1
    return reviews

list1 = get_reviews()
for val in list1:
    print(val)

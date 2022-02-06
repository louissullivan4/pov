from google.cloud import language_v1
import os
import json
import config
cloud_key = config.cloudkey
def get_ratings():
        with open('Backend/APIs/json/amazon_reviews.json') as fp:
            data = json.load(fp)
            i = 0
            reviews = []
            while i < len(data['result']):
                reviews.append(data["result"][i]["review"])
                i += 1
        return reviews

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Louis Sullivan/Desktop/College/Software/Code/pov/{}".format(cloud_key)


data = get_ratings()

def sample_analyze_sentiment(data):
    total_sentiments = 0
    total_positve = 0
    total_negative = 0
    total_neutral = 0
    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/language
    for val in data:
        language = "en"
        document = {"content": val, "type_": type_, "language": language}

        # Available values: NONE, UTF8, UTF16, UTF32
        encoding_type = language_v1.EncodingType.UTF8

        response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
        # Get overall sentiment of the input document
        print(u"Document sentiment score: {}".format(response.document_sentiment.score))
        print(
            u"Document sentiment magnitude: {}".format(
                response.document_sentiment.magnitude
            )
        )

        # Get sentiment for all sentences in the document
        for sentence in response.sentences:
            total_sentiments += 1
            if sentence.sentiment.score >= 0.1:
                total_positve += 1
            elif sentence.sentiment.score <= -0.1:
                total_negative += 1
            else:
                total_neutral += 1
            # print(u"Sentence text: {}".format(sentence.text.content))
            # print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
            # print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

        # Get the language of the text, which will be the same as
        # the language specified in the request or, if not specified,
        # the automatically-detected language.
        print(u"Language of the text: {}".format(response.language))
    results = (total_positve / total_sentiments) * 100
    print(results)  


print(sample_analyze_sentiment(data))

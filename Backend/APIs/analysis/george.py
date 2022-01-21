from textblob import TextBlob

class George:
    def __init__(self, input):
        self.data = input
        self.total_sentiments = 0
        self.total_positve = 0
        self.total_negative = 0
        self.total_neutral = 0
        self.pol = 0
        self.getSentiments()
        self.result = self.calculateResults()

    def getSentiments(self):
        for val in self.data:
            val = TextBlob(val)
            for sentence in val.sentences:
                polarity = float(sentence.sentiment.polarity)
                self.pol = polarity
                self.total_sentiments += 1
                if polarity >= 0.1:
                    self.total_positve += 1
                elif polarity <= -0.1:
                    self.total_negative += 1
                else:
                    self.total_neutral += 1
    
    def calculateResults(self):
        return (self.total_positve / self.total_sentiments) * 100

    def __str__(self):
        return "Text Input: {} \nTotal Input: {} \nTotal Positive: {} \nTotal Negative: {} \nTotal Neutral: {} \nPolarity: {} \nPositive Rating: {}% \n".format(self.data, self.total_sentiments, self.total_positve, self.total_negative, self.total_neutral, self.pol, self.result)


if __name__ == "__main__":
    bot = George()
    print(bot)









    

    


if __name__ == "__main__":
    bot = George

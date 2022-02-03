from textblob import TextBlob


class George:
    """
    This class analysises passed values using textblob and outputs a positive rating
    as a total of all the values passed
    """
    def __init__(self, input):
        self.data = input
        self.total_sentiments = 0
        self.total_positve = 0
        self.total_negative = 0
        self.total_neutral = 0
        self.pol = 0
        self.clean_data = []
        self.correct_spelling()
        self.result = self.calculateResults()

    def correct_spelling(self):
        """
        Correts spelling of data passed to class and adds them to a new list.
        """
        newlist = []
        for val in self.data:
            val = TextBlob(val)
            spelled = val.correct()
            newlist.append(str(spelled))
        self.clean_data = newlist
        self.getSentiments()

    def getSentiments(self):
        """
        Function that gets the polaity of each value passed and counts the positive,
        negative, neutal and total reviews.
        """
        for val in self.clean_data:
            val = TextBlob(val)
            #Polaity value is a float of how positive, negative or neutral a text value is
            polarity = float(val.sentiment.polarity)
            self.pol = polarity
            self.total_sentiments += 1
            if polarity >= 0.1:
                self.total_positve += 1
            elif polarity <= -0.1:
                self.total_negative += 1
            else:
                self.total_neutral += 1
    
    def calculateResults(self):
        """
        Gets the total positive reviews as a percentage of the total reviews
        """
        return (self.total_positve / self.total_sentiments) * 100

    def __str__(self):
        return "Text Input: {} \nTotal Input: {} \nTotal Positive: {} \nTotal Negative: {} \nTotal Neutral: {} \nPolarity: {} \nPositive Rating: {}% \n".format(self.data, self.total_sentiments, self.total_positve, self.total_negative, self.total_neutral, self.pol, self.result)


if __name__ == "__main__":
    bot = George()
    print(bot)


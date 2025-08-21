from collections import Counter
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from reader import get_weapons

class Analyzer:
    def __init__(self, df):
        self.df = df


    def finding_the_rarest_word(self):
        words = " ".join(self.df['Text'].astype(str)).split()
        ctr = Counter(words)
        common = ctr.most_common()
        return common[-1][0]

    def finding_the_emotion(self):
        text = " ".join(self.df['Text'].astype(str))
        score = SentimentIntensityAnalyzer().polarity_scores(text)["compound"]
        if score > 0.5:
            return "positive"
        elif score < -0.5:
            return "negative"
        else:
            return "neutral"


    def finding_weapons(self):
        weapons = set(get_weapons("../data/weapon_list.txt"))
        words = " ".join(self.df['Text'].astype(str)).split()
        for word in words:
            if word in weapons:
                return word
        return ""

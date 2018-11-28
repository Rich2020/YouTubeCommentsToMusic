from collections import Counter
from nltk.corpus import stopwords
import pandas as pd
from textblob import TextBlob
import re


class CommentAnalyzer:

    def __init__(self):
        self.ignore_words = []

    def token_is_valid(self, token):
        return token is not None \
               and token != '' \
               and len(token) > 3 \
               and token not in stopwords.words('english') \
               and token.isalpha() \
               and token not in self.ignore_words

    def word_frequencies(self, comments):
        observations = {}

        for comment in comments:
            for word in comment.split(' '):
                token = word.lower().strip(":,.!?")
                if self.token_is_valid(token):
                    if token not in observations:
                        observations[token] = 1
                    else:
                        observations[token] += 1

        return observations

    @staticmethod
    def clean(comments):
        cleaned = [' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", comment)
                            .split()) for comment in comments]
        return cleaned

    @staticmethod
    def get_sentiments(comments):

        rows = []
        for comment in comments:
            analysis = TextBlob(comment)
            polarity = analysis.sentiment.polarity
            mood = 'neutral'
            if polarity > 0:
                mood = 'positive'
            if polarity < 0:
                mood = 'negative'

            row = {'Comment': comment, 'Sentiment': polarity, 'Mood': mood}
            rows.append(row)

        sentiments_df = pd.DataFrame(rows)

        return sentiments_df

    @staticmethod
    def get_top_n_observations(observations, number):
        return dict(Counter(observations).most_common(number))


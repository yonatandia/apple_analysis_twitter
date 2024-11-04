import pandas as pd

class DataHandler:
    def __init__(self, tweets):
        self.tweets = tweets
    
    def to_dataframe(self):
        return pd.DataFrame(self.tweets, columns=['Tweet'])
    
    def analyze_sentiment(self, sentiments):
        df = self.to_dataframe()
        df['Sentiment'] = sentiments
        return df
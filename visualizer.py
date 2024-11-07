import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def plot_sentiment_histogram(sentiments):
        plt.figure(figsize=(10, 6))
        plt.hist(sentiments, bins=80, alpha=0.7, color='blue')
        plt.title("Sentiment Analysis of Tweets about Apple")
        plt.xlabel("Sentiment Score")
        plt.ylabel("Count")
        plt.axvline(0, color='red', linestyle='dashed', linewidth=1) # the neutral line
        plt.show()
    
    @staticmethod
    def plot_sentiment_by_tweet(df):
        plt.figure(figsize=(12, 6))
        plt.barh(df['Tweet'], df['Sentiment'], color='skyblue')
        plt.title('Sentiment Scores of Tweets about Apple')
        plt.xlabel('Sentiment Score')
        plt.ylabel('Tweet')
        plt.tight_layout()
        plt.show()
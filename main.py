from twitter_client import TwitterClient
from sentiment_analyzer import SentimentAnalyzer
from data_hundler import DataHandler
from visualizer import Visualizer

tweets = ['Apple is great', 'I hate Apple', 'I hate Apple','Not good for Apple']  # this is a temporary line. when I'll have access to retrieve tweets, the line won't be necessary
def main():
    # create instances of the clients
    twitter_client = TwitterClient()
    sentiment_analyzer = SentimentAnalyzer()

    # fetch tweets containing "Apple"
    # tweets = twitter_client.fetch_tweets("Apple", count=1)
    # the line above is a comment because I currently don't have access to tweeter api (due the fact they demand money for retrieving tweets)

    # analyze sentiment of the fetched tweets
    sentiments = sentiment_analyzer.analyze_multiple(tweets)

    # handle data with pandas
    data_handler = DataHandler(tweets)
    df = data_handler.analyze_sentiment(sentiments)

    print(df)

    # visualize the results
    Visualizer.plot_sentiment_histogram(sentiments)
    Visualizer.plot_sentiment_by_tweet(df)

if __name__ == '__main__':
    main()
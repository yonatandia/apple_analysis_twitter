from textblob import TextBlob

class SentimentAnalyzer:
    def analyze(self, text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity
    
    def analyze_multiple(self, texts):
        return [self.analyze(text) for text in texts]
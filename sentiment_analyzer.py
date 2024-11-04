from textblob import TextBlob

class SentimentAnalyzer:
    def analyze(self, text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity # Returns a float between -1 (negative) and 1 (positive)
    
    def analyze_multiple(self, texts):
        return [self.analyze(text) for text in texts]
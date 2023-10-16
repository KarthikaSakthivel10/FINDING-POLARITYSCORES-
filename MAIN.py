from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentences =input()
analyzer = SentimentIntensityAnalyzer()
a=analyzer.polarity_scores(sentences)
print(sentences,str(a))

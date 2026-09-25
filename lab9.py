import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon', quiet=True)

sia = SentimentIntensityAnalyzer()
text = "I love this NLP course. It is amazing and very useful!"
scores = sia.polarity_scores(text)
compound = scores['compound']
if compound >= 0.05:
    sentiment = "Positive"
elif compound <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"
print("Scores:", scores)
print("Overall Sentiment:", sentiment)

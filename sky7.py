#for sentimental analysis
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import matplotlib.pyplot as plt
# from wordfilter import Wordfilter

with open('comment.txt', 'r', encoding='utf-8') as file:
    text = file.read()


nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()


sentiment_scores = sia.polarity_scores(text)


if sentiment_scores['compound'] >= 0.05:
    sentiment = 'Positive'
elif sentiment_scores['compound'] <= -0.05:
    sentiment = 'Negative'
else:
    sentiment = 'Neutral'


blob = TextBlob(text)

sentiment_polarity = blob.sentiment.polarity


if sentiment_polarity > 0:
    sentiment_tb = 'Positive'
elif sentiment_polarity < 0:
    sentiment_tb = 'Negative'
else:
    sentiment_tb = 'Neutral'


labels = ['NLTK Sentiment', 'TextBlob Sentiment']
sizes = [sentiment_scores['compound'], sentiment_polarity]
colors = ['#66ff66', '#6666ff']

plt.figure(figsize=(8, 4))
plt.bar(labels, sizes, color=colors)
plt.ylabel('Sentiment Score')
plt.title('Sentiment Analysis Results')
plt.show()

print(f'NLTK Sentiment: {sentiment}')
print(f'TextBlob Sentiment: {sentiment_tb}')
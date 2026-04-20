import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (only needed once)
nltk.download('vader_lexicon')

# Load cleaned data
print("Loading data...")
df = pd.read_csv("C:/Users/suhan/cineiq/data/tmdb_cleaned.csv")
df = df.dropna(subset=['overview'])
print(f"✅ {len(df)} movies loaded")

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Apply sentiment analysis on movie overview
print("Analyzing sentiment for every movie... (this takes 2-3 mins)")

def get_sentiment(text):
    scores = sia.polarity_scores(str(text))
    compound = scores['compound']
    if compound >= 0.05:
        return 'Positive', compound
    elif compound <= -0.05:
        return 'Negative', compound
    else:
        return 'Neutral', compound

# Apply to all movies
df[['sentiment', 'sentiment_score']] = df['overview'].apply(
    lambda x: pd.Series(get_sentiment(x))
)

print("✅ Sentiment analysis complete!")

# Results summary
print("\n📊 Sentiment Distribution:")
print(df['sentiment'].value_counts())

print("\n🎬 Top 5 Most Positive Movies:")
top_positive = df.nlargest(5, 'sentiment_score')[['title','sentiment_score','genres','vote_average']]
print(top_positive.to_string(index=False))

print("\n🎬 Top 5 Most Negative Movies:")
top_negative = df.nsmallest(5, 'sentiment_score')[['title','sentiment_score','genres','vote_average']]
print(top_negative.to_string(index=False))

print("\n📊 Average sentiment score by genre (top 10):")
genre_sentiment = df.groupby('genres')['sentiment_score'].mean().sort_values(ascending=False).head(10)
print(genre_sentiment)

# Save with sentiment scores
df.to_csv("C:/Users/suhan/cineiq/data/tmdb_with_sentiment.csv", index=False)
print("\n🎉 Saved! tmdb_with_sentiment.csv ready!")
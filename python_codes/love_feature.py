import pandas as pd
from transformers import pipeline

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("user_feature.csv")

# Load the pre-trained BERT model for sentiment analysis
sentiment_classifier = pipeline("sentiment-analysis")


# Function to analyze sentiment of phrases using BERT
def analyze_sentiment_with_bert(reviews):
    sentiments = sentiment_classifier(reviews)
    return sentiments


# Extract reviews
reviews = df["good_reviews"].tolist()

# Apply sentiment analysis to reviews
sentiments = analyze_sentiment_with_bert(reviews)

# Create a DataFrame to store sentiment results
sentiment_df = pd.DataFrame(sentiments)

# Combine sentiment results with original DataFrame
df_with_sentiment = pd.concat([df, sentiment_df], axis=1)

# Sort DataFrame by sentiment score
df_with_sentiment_sorted = df_with_sentiment.sort_values(by="score", ascending=False)

# Print the top 10 reviews with sentiment scores
for index, row in df_with_sentiment_sorted.head(10).iterrows():
    print(f"Review: {row['good_reviews']}")
    print(f"Sentiment: {row['label']} (Score: {row['score']})")
    print()

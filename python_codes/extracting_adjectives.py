import csv
import pandas as pd
import spacy
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the data from survey_responses.csv into a DataFrame
df_survey = pd.read_csv("survey_responses.csv")
df_pre = df_survey[["id", "love", "hate"]]

import string
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokens import Doc

# Load the spacy model
nlp = spacy.load("en_core_web_sm")

# Define custom stop words
custom_stop_words = [
    "get",
    "would",
    "could",
    "say",
    "go",
    "going",
    "like",
    "us",
    "use",
    "also",
    "don't",
    "that",
]


# Function to preprocess text
def preprocess_text(text, include_ngrams=False):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Lemmatize and remove stop words and custom stop words
    doc = nlp(text)
    result = []
    for token in doc:
        if (
            token.text not in STOP_WORDS
            and token.text not in custom_stop_words
            and token.is_alpha
        ):
            result.append(token.lemma_)
    if include_ngrams:
        # Generate bigrams and trigrams
        ngrams = (
            list(doc.noun_chunks)
            + list(zip(doc[:-1], doc[1:]))
            + list(zip(doc[:-2], doc[1:-1], doc[2:]))
        )
        result.extend([" ".join(str(t.lemma_) for t in ngram) for ngram in ngrams])
    return " ".join(result)


# Apply the preprocessing function to the 'love' and 'hate' columns with including n-grams
df_pre["love"] = df_pre["love"].apply(lambda x: preprocess_text(x, include_ngrams=True))
df_pre["hate"] = df_pre["hate"].apply(lambda x: preprocess_text(x, include_ngrams=True))

# Load spaCy model and VADER analyzer
nlp = spacy.load("en_core_web_sm")
analyzer = SentimentIntensityAnalyzer()


def extract_positive_adjectives(texts):
    positive_adjectives = []
    for doc in nlp.pipe(texts):
        for token in doc:
            if token.pos_ == "ADJ":
                # Perform sentiment analysis using VADER
                sentiment_score = analyzer.polarity_scores(token.text)
                if sentiment_score["compound"] > 0:  # Positive sentiment
                    positive_adjectives.append(token.lemma_)
    return Counter(positive_adjectives)


# Apply the function to the 'love' column
positive_adjectives_love = extract_positive_adjectives(df_pre["love"])


def extract_negative_adjectives(texts):
    negative_adjectives = []
    for doc in nlp.pipe(texts):
        for token in doc:
            if token.pos_ == "ADJ":
                # Perform sentiment analysis using VADER
                sentiment_score = analyzer.polarity_scores(token.text)
                if sentiment_score["compound"] < 0:  # Negative sentiment
                    negative_adjectives.append(token.lemma_)
    return Counter(negative_adjectives)


# Apply the function to the 'hate' column
negative_adjectives_hate = extract_negative_adjectives(df_pre["hate"])

# Print the most common positive adjectives
# print("Most common positive adjectives in 'love':")
# print(positive_adjectives_love.most_common(5))
# # Print the most common negative adjectives
# print("Most common negative adjectives in 'hate':")
# print(negative_adjectives_hate.most_common(5))

# Get the top 5 most common adjectives in 'love'
top_love_adjectives = [adj for adj, _ in positive_adjectives_love.most_common(5)]


# Function to extract love adjectives from a review
def extract_love_adjectives(text):
    doc = nlp(text)
    love_adjectives = []
    for token in doc:
        if token.lemma_ in top_love_adjectives:
            love_adjectives.append(token.lemma_)
    return love_adjectives


# Function to extract hate adjectives from a review
def extract_hate_adjectives(text):
    doc = nlp(text)
    hate_adjectives = []
    for token in doc:
        if token.pos_ == "ADJ":
            # Perform sentiment analysis using VADER
            sentiment_score = analyzer.polarity_scores(token.text)
            if sentiment_score["compound"] < 0:  # Negative sentiment
                hate_adjectives.append(token.lemma_)
    return hate_adjectives


# Add new columns with containing love and hate adjectives
df_survey["love_adjectives"] = df_survey["love"].apply(extract_love_adjectives)
df_survey["hate_adjectives"] = df_survey["hate"].apply(extract_hate_adjectives)

# Write the updated DataFrame back to the CSV file
df_survey.to_csv("survey_responses_updated.csv", index=False)

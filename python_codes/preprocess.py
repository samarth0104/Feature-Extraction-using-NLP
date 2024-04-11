import pandas as pd
import string
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2

# Load the data from survey_responses.csv into a DataFrame
df_survey = pd.read_csv("survey_responses.csv")

# Creating a new DataFrame df_pre with only 'id', 'love', and 'hate' columns
df_pre = df_survey[["id", "love", "hate"]]

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
    "not",  # Add "not" to custom stop words
]


# Preprocessing function for 'love' comments
def preprocess_love(text):
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
    return " ".join(result)


# Preprocessing function for 'hate' comments
def preprocess_hate(text):
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
            and token.pos_ != "ADJ"  # Exclude adjectives
            and token.text
            not in ["sure", "think", "moment"]  # Exclude irrelevant words
            and token.lemma_ != "not"  # Exclude "not"
            and not token.lemma_.startswith(
                "not_"
            )  # Exclude words starting with "not_"
        ):
            # Ensure phrases indicating negative sentiment are handled properly
            if token.text in ["lack", "low", "weakest", "link"]:
                result.append("NEG_" + token.lemma_)
            else:
                result.append(token.lemma_)
    return " ".join(result)


# Apply the preprocessing functions to the 'love' and 'hate' columns
df_pre["love_preprocessed"] = df_pre["love"].apply(preprocess_love)
df_pre["hate_preprocessed"] = df_pre["hate"].apply(preprocess_hate)

# Define TF-IDF Vectorizer with bigram configuration
tfidf_vectorizer = TfidfVectorizer(ngram_range=(2, 2), max_features=1000)

# Fit and transform 'love' comments
love_tfidf_matrix = tfidf_vectorizer.fit_transform(df_pre["love_preprocessed"])
love_tfidf_features = tfidf_vectorizer.get_feature_names_out()

# Fit and transform 'hate' comments
hate_tfidf_matrix = tfidf_vectorizer.fit_transform(df_pre["hate_preprocessed"])
hate_tfidf_features = tfidf_vectorizer.get_feature_names_out()

# Select top features using chi-square test
k = 100  # Number of top features to select
selector = SelectKBest(score_func=chi2, k=k)

# Fit selector on 'love' comments
love_selected_features = selector.fit_transform(love_tfidf_matrix, df_survey["love"])

# Get indices of selected features
love_selected_indices = selector.get_support(indices=True)

# Get selected feature names
love_selected_feature_names = [love_tfidf_features[i] for i in love_selected_indices]

# Fit selector on 'hate' comments
hate_selected_features = selector.fit_transform(hate_tfidf_matrix, df_survey["hate"])

# Get indices of selected features
hate_selected_indices = selector.get_support(indices=True)

# Get selected feature names
hate_selected_feature_names = [hate_tfidf_features[i] for i in hate_selected_indices]

# Output the selected features with example sentences
print("Selected two-word features (bigrams) from 'love' comments:")
print(love_selected_feature_names)
print("\nSelected two-word features (bigrams) from 'hate' comments:")

for feature_name in hate_selected_feature_names:
    print("\nFeature:", feature_name)
    # Find sentences containing the feature
    for sentence in df_pre["hate"][df_pre["hate"].str.contains(feature_name)].values[
        :5
    ]:
        print("Example:", sentence)

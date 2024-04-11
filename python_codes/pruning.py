import pandas as pd

# Read the CSV file
df = pd.read_csv("hate_feature_phrases_filtered.csv")

# Define the words to be removed
words_to_remove = [
    "g2",
    "time",
    "wish",
    "know",
    "half",
    "hour",
    "give",
    "review",
    "heck",
    "hey",
    "people",
    "coming",
    "understand",
    "admin" "way",
    "nothing",
    "dislike",
    "np",
    "try",
    "come",
    "lot",
    "told",
    "get",
    "next",
]


# Function to filter out rows containing any of the words to be removed
def filter_features(row):
    features = eval(
        row
    )  # Assuming the feature phrases are stored as string representation of lists
    filtered_features = [
        f for f in features if not any(word in f for word in words_to_remove)
    ]
    return filtered_features


# Apply the filter function to each row in the column
df["hate_feature_phrases_filtered"] = df["hate_feature_phrases_filtered"].apply(
    filter_features
)

# Write the modified DataFrame back to the CSV file
df.to_csv("pruned_hate_feature_phrases_filtered.csv", index=False)

import pandas as pd
from collections import Counter

# Read the CSV file
df = pd.read_csv("survey_responses_with_features.csv")

# Calculate the frequency of words in 'love_extracted_features' column
word_freq = Counter(" ".join(df["love_extracted_features"].dropna()).split())

# Get the top 5 most frequent words
top_5_words = [word for word, freq in word_freq.most_common(5)]

# Create a DataFrame for top 5 words
top_5_df = pd.DataFrame({"Top 5 Words": top_5_words})

# Write top 5 words to a CSV file
top_5_df.to_csv("g2_ps_2\\src\\love_key.csv", index=False)


# Function to extract top 5 words from each row
def extract_top_5(row):
    extracted_features = str(row["love_extracted_features"])
    if extracted_features != "nan":  # Handle missing values
        extracted_features = extracted_features.split()
        top_words_in_row = [word for word in extracted_features if word in top_5_words]
        return ", ".join(top_words_in_row)
    else:
        return ""


# Add a new column 'love_key' containing the top 5 words for each row
df["love_key"] = df.apply(extract_top_5, axis=1)

# Write the updated DataFrame back to the CSV file
df.to_csv("survey_responses_with_features_up.csv", index=False)

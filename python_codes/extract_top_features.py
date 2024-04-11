import ast
import pandas as pd

# Read the grouped features CSV file
df = pd.read_csv("grouped_features_1.csv")  # Change file path as necessary


# Function to convert string representation of dictionary to dictionary
def str_to_dict(s):
    try:
        return ast.literal_eval(s)
    except (SyntaxError, ValueError):
        return {}


# Convert the 'extracted_feature' column to dictionaries
df["extracted_feature"] = df["extracted_feature"].apply(str_to_dict)


# Function to extract top 5 features from each category
def extract_top_features(group):
    top_features = {}
    for category, features in zip(group["categories"], group["extracted_feature"]):
        feature_count = {}
        for feature in features.values():
            feature_count[feature] = feature_count.get(feature, 0) + 1
        sorted_features = sorted(
            feature_count.items(), key=lambda x: x[1], reverse=True
        )[:10]
        top_features[category] = [feature[0] for feature in sorted_features]
    return pd.Series(top_features)


# Extract top 5 features from each category
top_features_df = extract_top_features(df)

# Save the top features to a new CSV file
top_features_df.to_csv("top_features_1.csv")

# Display the top features
print(top_features_df)

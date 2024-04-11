import pandas as pd

# Read the categorized data CSV file
df = pd.read_csv("categorized_data_1.csv")  # Change file path as necessary

# Group the extracted features by categories and create key-value pairs
grouped_features = (
    df.groupby("categories")
    .apply(lambda x: dict(zip(x["id"], x["hate_feature"])))
    .reset_index(name="extracted_feature")
)

# Save the grouped features to a new CSV file
grouped_features.to_csv("grouped_features_1.csv", index=False)

# Display the grouped features
print(grouped_features)

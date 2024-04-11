import pandas as pd

# Read the CSV file
df = pd.read_csv("pruned_hate_feature_phrases_filtered.csv")

# Initialize an empty DataFrame for output
output_df = pd.DataFrame(columns=["id", "hate_feature"])

# Iterate through each row of the input DataFrame
for index, row in df.iterrows():
    id_val = row["id"]
    features = row["hate_feature_phrases_filtered"]
    features = eval(features)  # Convert string representation of list to actual list

    # Add each feature as a new row to the output DataFrame
    for feature in features:
        output_df = output_df.append(
            {"id": id_val, "hate_feature": feature}, ignore_index=True
        )

# Write the output DataFrame to a new CSV file
output_df.to_csv("output_1.csv", index=False)

import pandas as pd

# Read the CSV file
df = pd.read_csv("top_features_1.csv")

# Initialize an empty DataFrame for output
output_df = pd.DataFrame(columns=["Category", "Id", "Feature"])

# Iterate through each row of the input DataFrame
for index, row in df.iterrows():
    category = row["Category"]
    features_dict = eval(
        row["Features"]
    )  # Convert string representation of dictionary to actual dictionary

    # Add each feature as a new row to the output DataFrame
    for id_val, feature in features_dict.items():
        output_df = output_df.append(
            {"Category": category, "Id": id_val, "Feature": feature}, ignore_index=True
        )

# Write the output DataFrame to a new CSV file
output_df.to_csv("result.csv", index=False)

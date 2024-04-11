import pandas as pd

# Define category mapping
category_mapping = {
    "roi": ["return on investment", "profit", "revenue", "roi"],
    "social": ["social", "linkedin log", "email", "asset", "lead"],
    "Info": [
        "quality",
        "experience",
        "satisfaction",
        "bug",
        "issues",
        "feature",
        "resource",
        "info",
        "missing",
        "negative",
        "burden",
        "granular",
    ],
    "tools and tech": [
        "tool",
        "software",
        "application",
        "widget",
        "badge",
        "program",
        "search",
        "penetration",
        "database",
    ],
    "needs": ["value", "confusing", "demand", "lack", "reporting", "interface", "doc"],
    "security": ["security", "privacy", "cybersecurity", "ip"],
    "cost": [
        "cost",
        "price",
        "expense",
        "money",
        "charge",
        "subscription",
        "expensive",
        "membership",
    ],
    "landing and other pages": ["landing page", "page"],
    # Add more categories and associated words as needed
}

# Read the CSV file
df = pd.read_csv("output_1.csv")  # Change file path as necessary


# Create a function to categorize each feature
def categorize_feature(text):
    for category, keywords in category_mapping.items():
        for keyword in keywords:
            if keyword in text.lower():
                return category
    return "Other"  # If no category matches


# Create a function to categorize each row
def categorize_row(row):
    category = categorize_feature(row["hate_feature"])
    return category


# Apply the categorize_row function to create a new column 'categories'
df["categories"] = df.apply(categorize_row, axis=1)

# Save the categorized data back to a CSV file
df.to_csv("categorized_data_1.csv", index=False)

# Display the categorized data
print(df)

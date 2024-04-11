import csv
import requests

# Make the API call
headers = {
    "Authorization": "Token token=ffa93ab223c71abc7f54d74b0589c4fb3e59bfc1dffd5fb889db4195967e3c41",
    "Content-Type": "application/vnd.api+json",
}

# Initialize an empty list to store all survey responses
all_survey_responses = []

# Iterate through each page
for page_number in range(1, 9):
    url = f"https://data.g2.com/api/v1/survey-responses?page[number]={page_number}&page[size]=100"
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Add survey responses to the list
        all_survey_responses.extend(data["data"])
    else:
        print(f"Failed to fetch data for page {page_number}:", response.status_code)

# Write data to a CSV file
filename = "survey_responses.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
    fieldnames = [
        "id",
        "type",
        "product_name",
        "is_public",
        "slug",
        "percent_complete",
        "star_rating",
        "title",
        "love",
        "hate",
        "verified_current_user",
        "is_business_partner",
        "review_source",
        "votes_up",
        "votes_down",
        "votes_total",
        "user_id",
        "user_name",
        "user_image_url",
        "country_name",
        "regions",
        "submitted_at",
        "updated_at",
        "moderated_at",
        "product_id",
        "reference_user_consent",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for response in all_survey_responses:
        attributes = response["attributes"]
        regions = attributes.get("regions", [])
        if isinstance(regions, str):
            writer.writerow(
                {
                    "id": response["id"],
                    "type": response["type"],
                    "product_name": attributes.get("product_name", "Unknown"),
                    "is_public": attributes.get("is_public", "Unknown"),
                    "slug": attributes.get("slug", "Unknown"),
                    "percent_complete": attributes.get("percent_complete", "Unknown"),
                    "star_rating": attributes.get("star_rating", "Unknown"),
                    "title": attributes.get("title", "Unknown"),
                    "love": attributes["comment_answers"]
                    .get("love", {})
                    .get("value", "Unknown"),
                    "hate": attributes["comment_answers"]
                    .get("hate", {})
                    .get("value", "Unknown"),
                    "verified_current_user": attributes.get(
                        "verified_current_user", "Unknown"
                    ),
                    "is_business_partner": attributes.get(
                        "is_business_partner", "Unknown"
                    ),
                    "review_source": attributes.get("review_source", "Unknown"),
                    "votes_up": attributes.get("votes_up", "Unknown"),
                    "votes_down": attributes.get("votes_down", "Unknown"),
                    "votes_total": attributes.get("votes_total", "Unknown"),
                    "user_id": attributes.get("user_id", "Unknown"),
                    "user_name": attributes.get("user_name", "Unknown"),
                    "user_image_url": attributes.get("user_image_url", "Unknown"),
                    "country_name": attributes.get("country_name", "Unknown"),
                    "regions": regions,
                    "submitted_at": attributes.get("submitted_at", "Unknown"),
                    "updated_at": attributes.get("updated_at", "Unknown"),
                    "moderated_at": attributes.get("moderated_at", "Unknown"),
                    "product_id": attributes.get("product_id", "Unknown"),
                    "reference_user_consent": attributes.get(
                        "reference_user_consent", "Unknown"
                    ),
                }
            )
        else:
            writer.writerow(
                {
                    "id": response["id"],
                    "type": response["type"],
                    "product_name": attributes.get("product_name", "Unknown"),
                    "is_public": attributes.get("is_public", "Unknown"),
                    "slug": attributes.get("slug", "Unknown"),
                    "percent_complete": attributes.get("percent_complete", "Unknown"),
                    "star_rating": attributes.get("star_rating", "Unknown"),
                    "title": attributes.get("title", "Unknown"),
                    "love": attributes["comment_answers"]
                    .get("love", {})
                    .get("value", "Unknown"),
                    "hate": attributes["comment_answers"]
                    .get("hate", {})
                    .get("value", "Unknown"),
                    "verified_current_user": attributes.get(
                        "verified_current_user", "Unknown"
                    ),
                    "is_business_partner": attributes.get(
                        "is_business_partner", "Unknown"
                    ),
                    "review_source": attributes.get("review_source", "Unknown"),
                    "votes_up": attributes.get("votes_up", "Unknown"),
                    "votes_down": attributes.get("votes_down", "Unknown"),
                    "votes_total": attributes.get("votes_total", "Unknown"),
                    "user_id": attributes.get("user_id", "Unknown"),
                    "user_name": attributes.get("user_name", "Unknown"),
                    "user_image_url": attributes.get("user_image_url", "Unknown"),
                    "country_name": attributes.get("country_name", "Unknown"),
                    "regions": "Unknown",
                    "submitted_at": attributes.get("submitted_at", "Unknown"),
                    "updated_at": attributes.get("updated_at", "Unknown"),
                    "moderated_at": attributes.get("moderated_at", "Unknown"),
                    "product_id": attributes.get("product_id", "Unknown"),
                    "reference_user_consent": attributes.get(
                        "reference_user_consent", "Unknown"
                    ),
                }
            )

print(f"Data saved to {filename}")

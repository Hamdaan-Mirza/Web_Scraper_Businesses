import requests
import pandas as pd
import time

API_KEY = "AIzaSyCb4vTHYYtTqfQ7FQer-z390cWRVTOYtCI"
OUTPUT_FILE = "leads.csv"

SEARCH_QUERY = "roofing contractor"
LOCATION = "South Africa"

url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

params = {
    "query": f"{SEARCH_QUERY} in {LOCATION}",
    "key": API_KEY
}

leads = []

while True:
    response = requests.get(url, params=params)
    data = response.json()

    for place in data.get("results", []):
        name = place.get("name", "")
        place_id = place.get("place_id", "")

        # Get details (phone + website)
        details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        details_params = {
            "place_id": place_id,
            "fields": "name,formatted_phone_number,website",
            "key": API_KEY
        }

        details_resp = requests.get(details_url, params=details_params)
        details = details_resp.json().get("result", {})

        leads.append({
            "Business_Name": details.get("name", ""),
            "Website_URL": details.get("website", ""),
            "Phone_Number": details.get("formatted_phone_number", "")
        })

        time.sleep(0.2)  # stay safe with rate limits

    if "next_page_token" in data:
        params["pagetoken"] = data["next_page_token"]
        time.sleep(2)
    else:
        break

df = pd.DataFrame(leads)
df.drop_duplicates(inplace=True)
df.to_csv(OUTPUT_FILE, index=False)

print(f"✅ Saved {len(df)} leads to {OUTPUT_FILE}")

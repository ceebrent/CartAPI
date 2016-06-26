import requests
import json
from google_api_key import google_key

def get_google_coordinates(location, store_name):
    params = dict(
        location = location,
        types = "grocery_or_supermarket",
        name= store_name,
        rankby="distance",
        key = google_key
    )

    google_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    response = requests.get(google_url, params=params)

    return json.loads(response.text)
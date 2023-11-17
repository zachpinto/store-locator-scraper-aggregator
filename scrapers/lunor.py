import requests
import json
import pandas as pd
import os

# Function to append data to CSV
def append_to_csv(data, filename):
    if os.path.exists(filename):
        data.to_csv(filename, mode='a', index=False, header=False)
    else:
        data.to_csv(filename, mode='w', index=False, header=True)

# List of cities with their latitudes and longitudes
cities = [
    ("New York, NY", 40.7128, -74.0060),
    ("Boston, MA", 42.3601, -71.0589),
    ("Chicago, IL", 41.8781, -87.6298),
    ("Philadelphia, PA", 39.9526, -75.1652),
    ("Washington, DC", 38.9072, -77.0369),
    ("Charlotte, NC", 35.2271, -80.8431),
    ("Nashville, TN", 36.1627, -86.7816),
    ("Detroit, MI", 42.3314, -83.0458),
    ("St Louis, MO", 38.6270, -90.1994),
    ("Houston, TX", 29.7604, -95.3698),
    ("Phoenix, AZ", 33.4484, -112.0740),
    ("San Francisco, CA", 37.7749, -122.4194),
    ("Portland, OR", 45.5051, -122.6750),
]

# API Endpoint
api_url = "https://lunor.com/wp-admin/admin-ajax.php"

for city, lat, lng in cities:
    print(f"Scraping data for {city}...")

    # Payload for each city
    payload = {
        'action': 'get_stores',
        'lat': str(lat),
        'lng': str(lng),
        'radius': '500',  # Radius in miles
        'online_offline': 'all',
        'name': ''
    }

    # Sending the POST request with payload
    response = requests.post(api_url, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        data = json.loads(response.text)

        # Extracting store details
        stores = []
        for key, value in data.items():
            store_name = value.get('na', '')
            street = value.get('st', '')
            city = value.get('ct', '').strip()
            region = value.get('rg', '')
            zip_code = value.get('zp', '')
            stores.append({'Name': store_name, 'Street': street, 'City': city, 'Region': region, 'Zip': zip_code})

        # Convert to DataFrame and Append to CSV
        df = pd.DataFrame(stores)
        append_to_csv(df, '../data/lunor_store_locations.csv')

    else:
        print(f"Failed to retrieve data for {city}. Status Code:", response.status_code)

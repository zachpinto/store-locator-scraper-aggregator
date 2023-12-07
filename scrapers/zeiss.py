import requests
import pandas as pd
import os

def scrape_zeiss_stores(latitude, longitude, token='e3ba1bc5d0bfb79a3c8f67e8330caf67', bucket_id=142, limit=10, list_by='premium', premium_radius=20):
    url = "https://api.o-c.io/places/"

    payload = {
        'token': token,
        'bucket_id': bucket_id,
        'lat': latitude,
        'lng': longitude,
        'limit': limit,
        'list_by': list_by,
        'premium_radius': premium_radius
    }

    response = requests.post(url, data=payload)

    if response.status_code != 200:
        print(f"Failed to retrieve data for coordinates {latitude}, {longitude}")
        return []

    stores = response.json().get('data', [])
    data = []

    for store in stores:
        data.append({
            'Name': store.get('name'),
            'Formatted Address': store.get('formatted_address')
        })

    return data

def main():
    output_file = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/data/zeiss_store_locations.csv'
    coordinates_file = "../utils/coordinates.txt"  # Update this path as needed

    with open(coordinates_file, "r") as file:
        coordinates = file.readlines()

    for coord in coordinates:
        try:
            latitude, longitude = map(float, coord.strip().split(","))
            store_data = scrape_zeiss_stores(latitude, longitude)
            if store_data:
                df = pd.DataFrame(store_data)
                df.to_csv(output_file, mode='a', header=not os.path.exists(output_file), index=False)
                print(f"Data for coordinates {latitude}, {longitude} appended to CSV.")
            else:
                print(f"No data found for coordinates {latitude}, {longitude}.")
        except ValueError:
            print(f"Invalid coordinate line: '{coord.strip()}'")

if __name__ == "__main__":
    main()

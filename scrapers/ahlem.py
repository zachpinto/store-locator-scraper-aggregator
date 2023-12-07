import requests
import pandas as pd
import os

def scrape_ahlem_stores(latitude, longitude, distance=25):
    url = "https://stockist.co/api/v1/u9359/locations/search"

    params = {
        'tag': 'u9359',
        'latitude': latitude,
        'longitude': longitude,
        'filter_operator': 'and',
        'distance': distance
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Failed to retrieve data for coordinates {latitude}, {longitude}")
        return []

    stores = response.json().get('locations', [])
    data = []

    for store in stores:
        data.append({
            'Name': store.get('name'),
            'Address': store.get('address_line_1'),
            'City': store.get('city'),
            'State': store.get('state'),
            'Postal Code': store.get('postal_code')
        })

    return data

def main():
    output_file = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/data/ahlem_store_locations.csv'
    coordinates_file = "../utils/coordinates.txt"  # Update this path as needed

    with open(coordinates_file, "r") as file:
        coordinates = file.readlines()

    for coord in coordinates:
        try:
            latitude, longitude = map(float, coord.strip().split(","))
            store_data = scrape_ahlem_stores(latitude, longitude)
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

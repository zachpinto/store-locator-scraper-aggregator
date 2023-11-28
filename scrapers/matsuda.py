import requests
import pandas as pd
import os

def scrape_matsuda_stores(latitude, longitude, distance=250):
    url = "https://stockist.co/api/v1/u2744/locations/search"

    params = {
        'tag': 'u2744',
        'latitude': latitude,
        'longitude': longitude,
        'filter_operator': 'and',
        'distance': distance
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Failed to retrieve data for coordinates {latitude}, {longitude}")
        return []

    locations = response.json().get('locations', [])
    data = []

    for location in locations:
        data.append({
            'Name': location.get('name'),
            'Address': location.get('address_line_1'),
            'City': location.get('city'),
            'State': location.get('state'),
            'Postal Code': location.get('postal_code'),
            'Country': location.get('country')
        })

    return data

def main():
    output_file = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/data/matsuda_store_locations.csv'
    coordinates_file = "../utils/coordinates.txt"  # Update this path as needed

    with open(coordinates_file, "r") as file:
        coordinates = file.readlines()

    for coord in coordinates:
        try:
            latitude, longitude = map(float, coord.strip().split(","))
            store_data = scrape_matsuda_stores(latitude, longitude)
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

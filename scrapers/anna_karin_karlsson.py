import requests
import pandas as pd
import os

def scrape_anna_karin_karlsson_stores(latitude, longitude, max_results=100, search_radius=10000):
    url = "https://annakarinkarlsson.com/wp-admin/admin-ajax.php"

    params = {
        'action': 'store_search',
        'lat': latitude,
        'lng': longitude,
        'max_results': max_results,
        'search_radius': search_radius
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Failed to retrieve data for coordinates {latitude}, {longitude}")
        return []

    stores = response.json()
    data = []

    for store in stores:
        data.append({
            'Name': store.get('store'),
            'Address': store.get('address'),
            'City': store.get('city'),
            'Zip': store.get('zip')
        })

    return data

def main():
    output_file = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/data/anna_karin_karlsson_store_locations.csv'
    coordinates_file = "../utils/coordinates_minimal.txt"  # Update this path as needed

    with open(coordinates_file, "r") as file:
        coordinates = file.readlines()

    for coord in coordinates:
        try:
            latitude, longitude = map(float, coord.strip().split(","))
            store_data = scrape_anna_karin_karlsson_stores(latitude, longitude)
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

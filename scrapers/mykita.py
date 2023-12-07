import requests
import pandas as pd
import os

def scrape_mykita_stores(latitude, longitude, radius=20):
    url = "https://mykita.com/en/shopfinder"

    payload = {
        'searchTerm': f"{latitude}, {longitude}, USA",
        'breakPoint': 4,
        'requestResults': 'true',
        'poi[lat]': latitude,
        'poi[lng]': longitude,
        'bounds[ne][lat]': latitude + 0.1,  # Adjust bounds as needed
        'bounds[ne][lng]': longitude + 0.1,
        'bounds[sw][lat]': latitude - 0.1,
        'bounds[sw][lng]': longitude - 0.1
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01'
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve data for coordinates {latitude}, {longitude}")
        return []

    stores = response.json().get('json', {}).get('results', [])
    data = []

    for store in stores:
        data.append({
            'Name': store.get('name'),
            'Address': store.get('address'),
            'City': store.get('city'),
            'Zip': store.get('zip')
        })

    return data

def main():
    output_file = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/data/mykita_store_locations.csv'
    coordinates_file = "../utils/coordinates.txt"  # Update this path as needed

    with open(coordinates_file, "r") as file:
        coordinates = file.readlines()

    for coord in coordinates:
        try:
            latitude, longitude = map(float, coord.strip().split(","))
            store_data = scrape_mykita_stores(latitude, longitude)
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

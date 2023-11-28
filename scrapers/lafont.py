import requests
import pandas as pd
import os

def scrape_lafont_stores(latitude, longitude):
    url = f"https://www.lafont.com/api/getstore/{latitude}/{longitude}"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data for coordinates {latitude}, {longitude}")
        return []

    try:
        stores = response.json()
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return []

    print("First few stores (for debugging):", stores[:5])  # Print the first few stores for debugging

    data = []

    for store in stores:
        if isinstance(store, dict):
            data.append({
                'Store Name': store.get('RAISONSOCIAL'),
                'Address': store.get('ADRESSE'),
                'City': store.get('VILLE'),
                'Country': store.get('PAYS'),
                'Postal Code': store.get('CP')
            })
        else:
            print("Unexpected data format:", store)

    return data

def main():
    output_file = '../data/lafont_store_locations.csv'
    coordinates_file = "../utils/coordinates.txt"  # Update this path as needed

    with open(coordinates_file, "r") as file:
        coordinates = file.readlines()

    for coord in coordinates:
        try:
            latitude, longitude = map(float, coord.strip().split(","))
            store_data = scrape_lafont_stores(latitude, longitude)
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

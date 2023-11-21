import requests
import pandas as pd
import os

def scrape_costadelmar_stores(latitude, longitude):
    url = f"https://www.costadelmar.com/service/AjaxStoreLocatorJSONResultsView"

    params = {
        'storeId': 11501,
        'catalogId': 10501,
        'langId': -1,
        'maxItems': 50,
        'uom': 'miles',
        'radius': 300,
        'all': 'true',
        'geoCodeLatitude': latitude,
        'geoCodeLongitude': longitude
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Failed to retrieve data")
        return []

    stores = response.json()['PhysicalStore']
    data = []

    for store in stores:
        data.append({
            'Store Name': store.get('displayStoreName'),
            'Address': store.get('addressLine'),
            'City': store.get('city'),
            'State': store.get('stateOrProvinceName'),
            'Zip Code': store.get('postalCode'),
            'Country': store.get('country')
        })

    return data

def main():
    output_file = '../data/costadelmar_store_locations.csv'

    # Read coordinates from file
    with open("../utils/coordinates.txt", "r") as file:
        coordinates = file.readlines()

    for coord in coordinates:
        try:
            latitude, longitude = map(float, coord.strip().split(","))
            store_data = scrape_costadelmar_stores(latitude, longitude)
            df = pd.DataFrame(store_data)
            df.to_csv(output_file, mode='a', header=not os.path.exists(output_file), index=False)
            print(f"Data for coordinates {latitude}, {longitude} appended to CSV.")
        except ValueError:
            print(f"Invalid coordinate line: '{coord.strip()}'")

if __name__ == "__main__":
    main()

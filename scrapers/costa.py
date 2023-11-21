import requests
import pandas as pd
import os

def scrape_costadelmar_stores(latitude, longitude):
    url = "https://www.costadelmar.com/service/AjaxStoreLocatorJSONResultsView"
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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.costadelmar.com/store-locator/'
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Failed to retrieve data with status code: {response.status_code}")
        return []

    try:
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
    except KeyError:
        print("Error in parsing response. The key 'PhysicalStore' might not exist.")
        return []

def main():
    output_file = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/data/costa_store_locations.csv'

    # Read coordinates from file
    with open("/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/utils/coordinates.txt", "r") as file:
        coordinates = [line.strip().split(",") for line in file if line.strip()]

    for latitude, longitude in coordinates:
        store_data = scrape_costadelmar_stores(latitude, longitude)
        if store_data:
            df = pd.DataFrame(store_data)
            df.to_csv(output_file, mode='a', header=not os.path.exists(output_file), index=False)
            print(f"Data for coordinates {latitude}, {longitude} appended to CSV.")
        else:
            print(f"No data for coordinates {latitude}, {longitude}.")

if __name__ == "__main__":
    main()

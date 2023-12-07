import requests
import pandas as pd
import os

def scrape_tomford_stores(postal_code, radius=15.0):
    url = "https://www.tomford.com/on/demandware.store/Sites-tomford-Site/default/Stores-FindStores"

    params = {
        'showMap': 'false',
        'radius': radius,
        'postalCode': postal_code
    }

    try:
        response = requests.get(url, params=params)

        print(f"Requesting: {url} with params: {params}")

        if response.status_code != 200:
            print(f"Failed to retrieve data for postal code {postal_code} with status code {response.status_code}")
            return []

        print(f"Raw response: {response.text[:500]}")  # Print the first 500 characters of the response for debugging

        stores = response.json().get('stores', [])
        data = []

        for store in stores:
            data.append({
                'Name': store.get('name'),
                'Address': store.get('address1'),
                'City': store.get('city'),
                'State': store.get('stateCode'),
                'Postal Code': store.get('postalCode')
            })

        return data

    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")
        return []

def main():
    output_file = '/data/tom_ford_store_locations_old.csv'
    postal_codes_file = "../utils/zips.txt"  # Update this path as needed

    with open(postal_codes_file, "r") as file:
        postal_codes = file.readlines()

    for postal_code in postal_codes:
        postal_code = postal_code.strip()
        store_data = scrape_tomford_stores(postal_code)
        if store_data:
            df = pd.DataFrame(store_data)
            df.to_csv(output_file, mode='a', header=not os.path.exists(output_file), index=False)
            print(f"Data for postal code {postal_code} appended to CSV.")
        else:
            print(f"No data found for postal code {postal_code}.")

if __name__ == "__main__":
    main()

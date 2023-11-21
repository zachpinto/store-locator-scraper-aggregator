import requests
import pandas as pd
import os


def scrape_alainmikli_stores(location):
    url = "https://www.alainmikli.com/content/themes/alainmikli/inc/ajax-get-locations.php"

    post_data = {
        'location': location,
        'cmr': 'false'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        # Add any other necessary headers here
    }

    try:
        response = requests.post(url, data=post_data, headers=headers)

        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code

        stores = response.json()
        data = []

        for store in stores:
            data.append({
                'Name': store.get('name'),
                'Address': store.get('address_1'),
                'City': store.get('city'),
                'State': store.get('state'),
                'Zip': store.get('zip'),
                'Country': store.get('country')
            })

        return data

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

    return []


def main():
    output_file = '../data/alainmikli_store_locations.csv'

    with open("../utils/coordinates.txt", "r") as file:
        locations = file.readlines()

    for location in locations:
        location = location.strip()
        store_data = scrape_alainmikli_stores(location)
        df = pd.DataFrame(store_data)
        df.to_csv(output_file, mode='a', header=not os.path.exists(output_file), index=False)
        print(f"Data for location {location} appended to CSV.")


if __name__ == "__main__":
    main()

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_saltoptics_data(coordinates):
    # Replace with the actual URL or API endpoint of saltoptics.com
    url = "https://www.saltoptics.com/your-api-or-page-url"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://www.saltoptics.com/",
        # Add other necessary headers here
    }

    # Data to be sent with the request (assuming coordinates are used here)
    data = {
        'coordinates': coordinates
    }

    # Make a POST or GET request to the API or webpage
    response = requests.post(url, headers=headers, data=data)  # or requests.get(url, params=data)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract data from specified classes and IDs
        store_data = []
        store_list = soup.find_all('li', {'id': 'scasl-list-container'})
        for store in store_list:
            title = store.find('div', {'id': 'scasl-title'}).get_text(strip=True)
            address = store.find('div', {'id': 'scasl-address'}).get_text(strip=True)
            store_info = {
                'Name': title,
                'Address': address
            }
            store_data.append(store_info)
        return store_data
    else:
        print("Failed to retrieve data")
        return []

def append_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)

def main():
    with open('coordinates.txt', 'r') as file:
        coordinates_list = file.readlines()

    for coordinates in coordinates_list:
        store_data = scrape_saltoptics_data(coordinates.strip())
        append_to_csv(store_data, 'saltoptics_store_locations.csv')

if __name__ == "__main__":
    main()

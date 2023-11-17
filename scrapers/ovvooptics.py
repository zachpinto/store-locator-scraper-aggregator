import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_ovvooptics_data(coordinates):
    # API endpoint and headers based on your provided information
    url = "https://store-locator.ovvooptics.com/wp-admin/admin-ajax.php"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://store-locator.ovvooptics.com/",
        # Add other necessary headers here
    }

    # Data to be sent with the request (assuming coordinates are used here)
    data = {
        'coordinates': coordinates
    }

    # Make a POST request to the API
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract data within <h3> and <p> tags
        h3_tags = soup.find_all('h3')
        p_tags = soup.find_all('p')

        store_data = []
        for h3, p in zip(h3_tags, p_tags):
            store_info = {
                'Name': h3.text.strip(),
                'Address': p.text.strip().replace('<br>', ', ')
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
        store_data = scrape_ovvooptics_data(coordinates.strip())
        append_to_csv(store_data, 'ovvooptics_store_locations.csv')

if __name__ == "__main__":
    main()

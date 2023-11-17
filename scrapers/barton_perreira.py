import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_bartonperreira_stores():
    url = 'https://bartonperreira.com/pages/retail-stores'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    stores = soup.find_all('div', class_='scasl-info-location')

    data = []

    for store in stores:
        title = store.find('div', id='scasl-title').text.strip() if store.find('div', id='scasl-title') else None
        address = store.find('div', id='scasl-address').text.strip() if store.find('div', id='scasl-address') else None
        city = store.find('span', id='scasl-city').text.strip() if store.find('span', id='scasl-city') else None
        state = store.find('span', id='scasl-state').text.strip() if store.find('span', id='scasl-state') else None
        zipcode = store.find('span', id='scasl-zipcode').text.strip() if store.find('span', id='scasl-zipcode') else None

        data.append({
            'Title': title,
            'Address': address,
            'City': city,
            'State': state,
            'Zip Code': zipcode
        })

    return pd.DataFrame(data)

# Call the function and save the data
df = scrape_bartonperreira_stores()
if df is not None:
    df.to_csv('bartonperreira_stores.csv', index=False)
    print(df)

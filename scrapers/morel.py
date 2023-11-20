import requests
import pandas as pd
import os

def get_morel_data(latitude, longitude):
    url = f"https://morel-storelocat.frb.io/api/getClosestStores?latitude={latitude}&longitude={longitude}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve data from Morel API")
        return []

    stores = response.json()

    data = []
    for store in stores:
        data.append({
            'Name': store.get('name'),
            'Street': store.get('street1'),
            'City': store.get('city'),
            'Department': store.get('department'),
            'ZipCode': store.get('zipCode')
        })

    return data

def main():
    # Define the path for the output CSV file
    output_file = '../data/morel_store_locations.csv'

    # Read coordinates from file
    with open("../utils/coordinates.txt", "r") as file:
        coordinates = file.readlines()

    # Iterate over each pair of coordinates
    for coord in coordinates:
        try:
            # Strip whitespace and split by comma
            latitude, longitude = map(float, coord.strip().split(","))

            data = get_morel_data(latitude, longitude)

            # Convert the data to a DataFrame
            df = pd.DataFrame(data)

            # Append the data to the CSV file
            df.to_csv(output_file, mode='a', header=not os.path.exists(output_file), index=False)

            # Optional: print a message for progress tracking
            print(f"Data for coordinates {latitude}, {longitude} appended to CSV.")
        except ValueError:
            print(f"Invalid coordinate line: '{coord.strip()}'")

# Run the main function
main()

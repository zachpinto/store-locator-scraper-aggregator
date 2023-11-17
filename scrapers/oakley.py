import requests
import pandas as pd
import os

def get_oakley_data(latitude, longitude):
    url = f"https://www.oakley.com/en-us/store-finder/stores?lat={latitude}&lng={longitude}&oakleyStore=true&_oakleyStore=on&oakleyVault=true&_oakleyVault=on&oakleyDealer=true&_oakleyDealer=on&oakleyRxFullService=true&_oakleyRxFullService=on&oakleyRxPickUp=true&_oakleyRxPickUp=on&eyewear=true&_eyewear=on&apparel=true&_apparel=on&footwear=true&_footwear=on&goggles=true&_goggles=on&custom=true&_custom=on&perscription=true&_perscription=on&accessories=true&_accessories=on&accessoriesLenses=true&_accessoriesLenses=on&other=true&_other=on"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return []

    store_data = response.json()
    
    data = []
    for store in store_data['stores']:
        data.append({
            'Name': store.get('name'),
            'Address': ' '.join(store.get('address', []))
        })

    return data

def main():
    # Define the path for the output CSV file
    output_file = '../../data/oakley/oakley_store_locations.csv'

    # Read coordinates from file
    with open("../../utils/coordinates.txt", "r") as file:
        coordinates = file.readlines()

    # Iterate over each pair of coordinates
    for coord in coordinates:
        try:
            # Strip whitespace and split by comma
            latitude, longitude = map(float, coord.strip().split(","))

            data = get_oakley_data(latitude, longitude)

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

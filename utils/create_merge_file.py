import os
import pandas as pd
from fuzzywuzzy import fuzz

def standardize_data(df):
    df['Name'] = df['Name'].str.lower().str.strip()
    df['Address'] = df['Address'].str.lower().str.strip()
    return df

def read_and_preprocess_csv(file_path):
    df = pd.read_csv(file_path)
    df = standardize_data(df)
    return df.sort_values(by='Address')

def address_based_deduplication(dataframes):
    unique_addresses = {}
    for brand, df in dataframes.items():
        for _, row in df.iterrows():
            addr = row['Address']
            name = row['Name']
            if addr not in unique_addresses:
                unique_addresses[addr] = {'Name': name, 'brands': {brand}}
            else:
                if fuzz.ratio(unique_addresses[addr]['Name'], name) > 80:
                    unique_addresses[addr]['brands'].add(brand)
    return unique_addresses

def create_final_dataframe(unique_addresses, brands):
    columns = ['Name', 'Address'] + brands
    final_df = pd.DataFrame(columns=columns)

    for addr, data in unique_addresses.items():
        row = [data['Name'], addr] + [1 if brand in data['brands'] else 0 for brand in brands]
        final_df.loc[len(final_df)] = row

    return final_df

def main():
    folder_path = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/final_data'
    output_file = '/final_data/00_merged_data.csv'

    brands = os.listdir(folder_path)
    dataframes = {brand.split('.')[0]: read_and_preprocess_csv(os.path.join(folder_path, brand)) for brand in brands}

    unique_addresses = address_based_deduplication(dataframes)
    final_df = create_final_dataframe(unique_addresses, [brand.split('.')[0] for brand in brands])

    final_df.to_csv(output_file, index=False)
    print(f"Final data saved to {output_file}")

if __name__ == "__main__":
    main()

import pandas as pd

def uppercase_names_in_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Convert the 'name' column to uppercase
    df['Name'] = df['Name'].str.upper()

    # Save the modified DataFrame back to the CSV
    df.to_csv(file_path, index=False)
    print(f"Updated file saved to {file_path}")

def clean_ic_berlin_entries(file_path, brand_column_name):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Ensure the brand column is of integer type and handle NaN values
    df[brand_column_name] = df[brand_column_name].fillna(0).astype(int)

    # Ensure the Address column is a string (make sure the column name matches your CSV file)
    df['Address'] = df['Address'].astype(str)

    # Filter out rows where 'ic! berlin' is 1 and Address does not end with 'usa'
    df = df[~((df[brand_column_name] == 1) & (~df['Address'].str.lower().str.endswith('usa')))]

    # Save the modified DataFrame back to the CSV
    df.to_csv(file_path, index=False)
    print(f"Updated file saved to {file_path}")

def main():
    file_path = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/merged_data/merged_data.csv'  # Update this to the path of your CSV file
    brand_column_name = 'ic! berlin'  # Update this if the column name is different
    clean_ic_berlin_entries(file_path, brand_column_name)
    uppercase_names_in_csv(file_path)

if __name__ == "__main__":
    main()

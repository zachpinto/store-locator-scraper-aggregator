import pandas as pd

def remove_duplicates_from_csv(file_path, output_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Remove duplicate rows, keeping the first occurrence
    unique_df = df.drop_duplicates()

    # Save the unique rows back to a CSV file
    unique_df.to_csv(output_path, index=False)

# Example usage
input_csv = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/data/ahlem_store_locations.csv'  # Replace with your input CSV file path
output_csv = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/data/ahlem_store_locations_.csv'  # Replace with your desired output CSV file path
remove_duplicates_from_csv(input_csv, output_csv)

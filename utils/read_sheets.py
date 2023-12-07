import pandas as pd
import os

def excel_sheets_to_csv(excel_file, output_folder):
    # Load the Excel file
    xls = pd.ExcelFile(excel_file)

    # Iterate over all sheets in the Excel file
    for sheet_name in xls.sheet_names:
        # Read the sheet into a pandas DataFrame
        df = xls.parse(sheet_name)

        # Construct the CSV file name based on the sheet name
        csv_file = os.path.join(output_folder, f"{sheet_name}.csv")

        # Save the DataFrame to a CSV file
        df.to_csv(csv_file, index=False)

        print(f"Saved sheet '{sheet_name}' to '{csv_file}'")

def main():
    excel_file = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/data/eyewear-competitors-store-locators.xlsx'  # Update with the path to your Excel file
    output_folder = '/Users/pintoza/Desktop/dev/python-development/python_store_locator_web_scraper/final_data'  # Update with the path to your output folder

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    excel_sheets_to_csv(excel_file, output_folder)

if __name__ == "__main__":
    main()

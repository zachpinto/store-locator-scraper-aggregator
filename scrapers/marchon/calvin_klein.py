import requests
import xml.etree.ElementTree as ET
import pandas as pd
import os

def get_ck_data(latitude, longitude):
    # Define the base URL
    url = "https://hosted.where2getit.com/marchon/ajax"

    # Create the XML payload
    xml_payload = f"""
    <request>
      <appkey>C8BE1040-DDD4-11DD-992A-26DE3B999D57</appkey>
      <formdata id="locatorsearch">
        <dataview>store_default</dataview>
        <geolocs>
          <geoloc>
            <longitude>{longitude}</longitude>
            <latitude>{latitude}</latitude>
            <country>US</country>
          </geoloc>
        </geolocs>
        <radiusuom>mile</radiusuom>
        <searchradius>50</searchradius>
        <limit>40</limit>
        <where>
          <ck><eq>1</eq></ck> <!-- Calvin Klein selected -->
        </where>
      </formdata>
    </request>
    """

    try:
        # Send the request (consider changing to POST if required)
        response = requests.post(url, data={'xml_request': xml_payload})

        # Check if the response is successful
        if response.status_code == 200:
            # Parse the XML response
            root = ET.fromstring(response.content)

            # Initialize a list to store the extracted data
            data = []

            # Iterate through each 'poi' tag in the XML
            for poi in root.findall('.//poi'):
                # Extract relevant data
                name = poi.find('name').text if poi.find('name') is not None else None
                address1 = poi.find('address1').text if poi.find('address1') is not None else None
                city = poi.find('city').text if poi.find('city') is not None else None
                state = poi.find('state').text if poi.find('state') is not None else None
                postalcode = poi.find('postalcode').text if poi.find('postalcode') is not None else None
                country = poi.find('country').text if poi.find('country') is not None else None

                # Add the data to the list
                data.append({
                    'Name': name,
                    'Address': address1,
                    'City': city,
                    'State': state,
                    'Postal Code': postalcode,
                    'Country': country
                })

            # Return the list
            return data
        else:
            print(f"Failed to retrieve data: Status Code {response.status_code}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Main function to iterate over coordinates
def main():
    # Define the path for the output CSV file
    output_file = '../../data/marchon/calvin_klein_store_locations1.csv'

    # Read coordinates from file
    with open("../../utils/coordinates.txt", "r") as file:
        coordinates = file.readlines()

    # Iterate over each pair of coordinates
    for coord in coordinates:
        try:
            # Strip whitespace and split by comma
            latitude, longitude = map(float, coord.strip().split(","))

            data = get_ck_data(latitude, longitude)

            # Convert the data to a DataFrame
            df = pd.DataFrame(data)

            # Append the data to the CSV file
            df.to_csv(output_file, mode='a', header=not os.path.exists(output_file), index=False)

            # Optional: print a message for progress tracking
            print(f"Data for coordinates {latitude}, {longitude} appended to CSV.")
        except ValueError:
            print(f"Invalid coordinate line: '{coord.strip()}'")

# Call the main function
main()

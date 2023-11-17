# Generating the coordinates as before
import numpy as np

def generate_coordinates(min_lat, max_lat, min_lon, max_lon, step=0.8):
    """
    Generate a grid of coordinates within specified bounds.
    Step size is in degrees and approximately corresponds to 80 miles.
    """
    latitudes = np.arange(min_lat, max_lat, step)
    longitudes = np.arange(min_lon, max_lon, step)
    return [(lat, lon) for lat in latitudes for lon in longitudes]

# U.S. continental bounds
min_latitude = 24.396308  # southernmost latitude
max_latitude = 49.384358  # northernmost latitude
min_longitude = -125.001651  # westernmost longitude
max_longitude = -66.93457  # easternmost longitude

# Generate the coordinates
coordinates = generate_coordinates(min_latitude, max_latitude, min_longitude, max_longitude)

# Save the coordinates to a file
coordinates_file_path = 'coordinates.txt'
with open(coordinates_file_path, 'w') as file:
    for lat, lon in coordinates:
        file.write(f"{lat},{lon}\n")

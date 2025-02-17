""""
This script takes a CSV file containing DMS coordinates (Latitude and Longitude columns)
into DD format, returning a CSV file with two columns with the converted values.
"""
import pandas as pd

# Function to convert DMS to DD
def dms_to_dd(dms, direction):
    """Convert DMS (Degrees, Minutes, Seconds) to Decimal Degrees."""
    # Split DMS string into components
    dms = dms.replace('°', '').replace('’', '').replace('’’', '').replace('"', '').strip()
    parts = dms.split()
    degrees, minutes, seconds = map(float, parts)
    decimal = degrees + (minutes / 60) + (seconds / 3600)
    if direction in ['S', 'W']:
        decimal *= -1
    return decimal

# Load the CSV file
input_file = "input.csv"  # Replace with your file path
output_file = "output.csv"

df = pd.read_csv(input_file)

# Apply the conversion for Latitude and Longitude
df['Latitude_DD'] = df['Latitude'].apply(
    lambda x: dms_to_dd(x[:-1], x[-1])  # Separate value and direction
)
df['Longitude_DD'] = df['Longitude'].apply(
    lambda x: dms_to_dd(x[:-1], x[-1])  # Separate value and direction
)

# Save the updated data to a new CSV file
df.to_csv(output_file, index=False)

print(f"Converted file saved as {output_file}")

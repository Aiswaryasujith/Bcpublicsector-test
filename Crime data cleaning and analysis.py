#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

# Load the CSV file
file_path = '/Users/aiswarya/Desktop/bc public sector assignment/2. REQ 112534 csv/5_crime_data.csv'
df = pd.read_csv(file_path)

# Replace missing HOUR, MINUTE values with a placeholder like -1
df['HOUR'].fillna(-1, inplace=True)
df['MINUTE'].fillna(-1, inplace=True)

# If you want to drop rows with missing time information instead
df = df.dropna(subset=['HOUR', 'MINUTE'])

# Remove rows with 'OFFSET TO PROTECT PRIVACY'
df = df[df['HUNDRED_BLOCK'] != 'OFFSET TO PROTECT PRIVACY']

# Combine date and time into a single datetime column
df['DATETIME'] = pd.to_datetime(df[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE']])

# Drop unnecessary columns
df = df.drop(columns=['X', 'Y'])

# Normalize 'HUNDRED_BLOCK' by removing 'XX'
df['HUNDRED_BLOCK'] = df['HUNDRED_BLOCK'].str.replace(r'XX', '00', regex=True)

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned data to a new CSV file
df.to_csv('/Users/aiswarya/Desktop/bc public sector assignment/2. REQ 112534 csv/crime_data.csv', index=False)


# In[8]:


import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the CSV file with crime data
crime_data_path = '/Users/aiswarya/Desktop/bc public sector assignment/2. REQ 112534 csv/crime_data.csv'  # Adjust this path
crime_df = pd.read_csv(crime_data_path)

# Load the Vancouver shapefile (adjust file path)
shapefile_path = '/Users/aiswarya/Desktop/bc public sector assignment/2. REQ 112534 csv/local-area-boundary.shp'  # Adjust path to your shapefile
vancouver_map = gpd.read_file(shapefile_path)

# Filter data for "Theft from Vehicle" and "Mischief" crimes
theft_from_vehicle_df = crime_df[crime_df['TYPE'] == 'Theft from Vehicle']
mischief_df = crime_df[crime_df['TYPE'] == 'Mischief']

# Convert the filtered data into GeoDataFrame for both crime types
theft_from_vehicle_gdf = gpd.GeoDataFrame(
    theft_from_vehicle_df,
    geometry=gpd.points_from_xy(theft_from_vehicle_df['Longitude'], theft_from_vehicle_df['Latitude']),
    crs='EPSG:4326'  # Ensure that the CRS is set to WGS84
)

mischief_gdf = gpd.GeoDataFrame(
    mischief_df,
    geometry=gpd.points_from_xy(mischief_df['Longitude'], mischief_df['Latitude']),
    crs='EPSG:4326'
)

# Plot the Vancouver boundaries
vancouver_map.plot(edgecolor='black', figsize=(10, 10))
plt.title("Vancouver Neighborhood Boundaries")

# Plot "Theft from Vehicle" crimes
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
vancouver_map.boundary.plot(ax=ax, edgecolor='black')
theft_from_vehicle_gdf.plot(ax=ax, color='red', markersize=10, label="Theft from Vehicle")
plt.title('Theft from Vehicle Crimes in Vancouver')
plt.legend()

# Plot "Mischief" crimes
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
vancouver_map.boundary.plot(ax=ax, edgecolor='black')
mischief_gdf.plot(ax=ax, color='blue', markersize=10, label="Mischief")
plt.title('Mischief Crimes in Vancouver')
plt.legend()

plt.show()

# Spatial join crime data with the Vancouver map to assign crimes to neighborhoods
crime_gdf = gpd.GeoDataFrame(
    crime_df, 
    geometry=gpd.points_from_xy(crime_df['Longitude'], crime_df['Latitude']),
    crs='EPSG:4326'
)

# Perform spatial join to match crimes with neighborhood polygons
crime_with_neighborhoods = gpd.sjoin(crime_gdf, vancouver_map, how='left', predicate='within')


# Count total crimes by neighborhood
neighborhood_crime_counts = crime_with_neighborhoods.groupby('name').size().reset_index(name='Total_Crimes')

# Find the neighborhood with the most total crimes
most_crime_neighborhood = neighborhood_crime_counts.loc[neighborhood_crime_counts['Total_Crimes'].idxmax()]

print(f"Neighborhood with the greatest number of total crimes: {most_crime_neighborhood['name']} ({most_crime_neighborhood['Total_Crimes']} crimes)")


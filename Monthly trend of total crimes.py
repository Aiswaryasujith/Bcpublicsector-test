#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
crime_df = pd.read_csv('/Users/aiswarya/Desktop/bc public sector assignment/2. REQ 112534 csv/crime_data.csv')

# Ensure that 'DATETIME' column is in datetime format
crime_df['DATETIME'] = pd.to_datetime(crime_df['DATETIME'])
crime_df['Month-Year'] = crime_df['DATETIME'].dt.to_period('M')
monthly_crime_counts = crime_df.groupby('Month-Year').size().reset_index(name='Total_Crimes')

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(monthly_crime_counts['Month-Year'].astype(str), monthly_crime_counts['Total_Crimes'], marker='o')
plt.xlabel('Month-Year')
plt.ylabel('Total Number of Crimes')
plt.title('Monthly Trend of Total Number of Crimes')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()

import geopandas as gpd

# Load the shapefiles
map_df = gpd.read_file('/Users/aiswarya/Desktop/bc public sector assignment/2. REQ 112534 csv/local-area-boundary.shp')

# Convert crime data to GeoDataFrame
gdf_crimes = gpd.GeoDataFrame(
    crime_df,
    geometry=gpd.points_from_xy(crime_df['Longitude'], crime_df['Latitude']),
    crs="EPSG:4326"  # Assuming WGS84 latitude/longitude
)

# Plot the map with crime data
fig, ax = plt.subplots(figsize=(12, 12))
map_df.plot(ax=ax, color='lightgrey')
gdf_crimes.plot(ax=ax, markersize=5, color='red', alpha=0.5, label='Crimes')
plt.legend()
plt.title('Crime Locations on Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


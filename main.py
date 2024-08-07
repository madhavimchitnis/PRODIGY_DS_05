

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Loading and exploring the dataset
data = pd.read_csv('US_Accidents_March23.csv')

# Displaying first few rows and basic info
print(data.head())
print(data.info())

# Data cleaning and preprocessing
# Convert Start_Time and End_Time to datetime format
data['Start_Time'] = pd.to_datetime(data['Start_Time'])
data['End_Time'] = pd.to_datetime(data['End_Time'])

# Extracting date and time components
data['Date'] = data['Start_Time'].dt.date
data['Time'] = data['Start_Time'].dt.time

# Descriptive analysis and visualization

# Accident frequency by road conditions
plt.figure(figsize=(10, 6))
sns.countplot(x='Weather_Condition', data=data)
plt.title('Accident Frequency by Weather Condition')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Accident frequency by time of day
data['Hour'] = data['Start_Time'].dt.hour
plt.figure(figsize=(10, 6))
sns.countplot(x='Hour', data=data)
plt.title('Accident Frequency by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')
plt.tight_layout()
plt.show()

# Visualizing accident hotspots
# Create a heatmap of accident locations
accident_map = folium.Map(location=[data['Start_Lat'].mean(), data['Start_Lng'].mean()], zoom_start=10)

heat_data = [[row['Start_Lat'], row['Start_Lng']] for index, row in data.iterrows()]

HeatMap(heat_data).add_to(accident_map)

accident_map.save('accident_hotspots.html')

# Identify patterns and factors (further analysis as needed)
# Correlation matrix
correlation_matrix = data[['Severity', 'Temperature(F)', 'Wind_Speed(mph)', 'Visibility(mi)', 'Humidity(%)']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()



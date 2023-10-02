import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import opendatasets as od

#!pip install opendatasets --upgrade --quiet
## can download requred dataset file from this link  using your kaggle credentials
download_url = 'https://www.kaggle.com/sobhanmoosavi/us-accidents'
od.download(download_url)
# Loading the dataset
data = pd.read_csv("US_Accidents_March23.csv")

# Exploring the dataset to understand its structure and columns
print(data.info())

# Analyzing patterns related to road conditions
road_condition_counts = data['Weather_Condition'].value_counts()
print("\nTop 10 Weather Conditions:")
print(road_condition_counts.head(10))

# Analyzing patterns related to weather conditions
weather_counts = data['Weather_Condition'].value_counts()
print("\nTop 10 Weather Conditions:")
print(weather_counts.head(10))

# Analyzing patterns related to time of day
data['Start_Time'] = pd.to_datetime(data['Start_Time'])
data['Hour'] = data['Start_Time'].dt.hour
hourly_accidents = data.groupby('Hour').size()
print("\nHourly Accident Counts:")
print(hourly_accidents)

# Visualizing accident hotspots
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Start_Lng', y='Start_Lat', data=data, alpha=0.1)
plt.title('Accident Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Visualizing contributing factors
contributing_factors = data['Traffic_Signal'].value_counts()
plt.figure(figsize=(8, 4))
sns.barplot(x=contributing_factors.index, y=contributing_factors.values)
plt.title('Traffic Signals vs. Accidents')
plt.xlabel('Traffic Signal Presence')
plt.ylabel('Accident Count')
plt.show()

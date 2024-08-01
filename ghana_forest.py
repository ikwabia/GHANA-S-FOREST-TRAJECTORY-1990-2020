# -*- coding: utf-8 -*-
"""Ghana Forest.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jfdcsALvEABUHa2iemRDxthb83_EmXde
"""

import numpy as np
import pandas as pd

forest =pd.read_csv("/content/Forest_Area.csv")

forest

forest.dropna()

forest.info()

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Convert 'Country and Area' column to string
forest['Country and Area'] = forest['Country and Area'].astype(str)

# Convert 'Forest Area' columns to numeric
for year in range(1990, 2021, 10):
    forest[f'Forest Area, {year}'] = pd.to_numeric(forest[f'Forest Area, {year}'], errors='coerce')

# Create a dictionary for word cloud where key is country and value is mean forest area from 1990 to 2020
wordcloud_dict = {}
for country in forest['Country and Area'].unique():
    if country.lower() != 'world':  # Make comparison case-insensitive
        country_data = forest[forest['Country and Area'] == country]
        mean_forest_area = country_data[['Forest Area, 1990', 'Forest Area, 2000', 'Forest Area, 2010', 'Forest Area, 2020']].mean(axis=1).values[0]
        wordcloud_dict[country] = mean_forest_area

# Generate word cloud with green background
wordcloud = WordCloud(background_color='white', width=800, height=400).generate_from_frequencies(wordcloud_dict)

# Display word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Filter the DataFrame for rows where 'Country and Area' is 'Ghana'
ghana_data = forest[forest['Country and Area'] == 'Ghana']

# Display the data
print(ghana_data)

# Check specific columns for Ghana
print(ghana_data[['Forest Area, 1990', 'Forest Area, 2000', 'Forest Area, 2010', 'Forest Area, 2020']])

import matplotlib.pyplot as plt

# Filter the DataFrame for rows where 'Country and Area' is 'Ghana'
ghana_data = forest[forest['Country and Area'] == 'Ghana']

# Prepare data for plotting
years = ['1990', '2000', '2010', '2020']
forest_area = [ghana_data[f'Forest Area, {year}'].values[0] for year in years]

# Create plot
plt.figure(figsize=(12, 6))  # Increase figure size
plt.plot(years, forest_area, marker='o', linewidth=2, linestyle='-', color='green')  # Increase line width, change line style and color

# Add gridlines
plt.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)

# Set plot title and labels with increased font size
plt.title('Forest Area in Ghana from 1990 to 2020', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Forest Area (in square km)', fontsize=14)  # More descriptive label

# Show plot
plt.show()

import matplotlib.pyplot as plt

# Filter the DataFrame for rows where 'Country and Area' is 'Ghana'
ghana_data = forest[forest['Country and Area'] == 'Ghana']

# Prepare data for plotting
years = ['1990', '2000', '2010', '2020']
forest_area = [ghana_data[f'Forest Area, {year}'].values[0] for year in years]

# Define colors for the bars
colors = ['blue', 'green', 'red', 'purple']

# Create plot
plt.figure(figsize=(10, 5))
plt.bar(years, forest_area, color=colors)

# Set plot title and labels
plt.title('Forest Area in Ghana from 1990 to 2020')
plt.xlabel('Year')
plt.ylabel('Forest Area')

# Show plot
plt.show()

import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame and you're looking at data for a specific country
country_data = forest[forest['Country and Area'] == 'Ghana']

# Get the forest area and total land area for a specific year
forest_area = country_data['Forest Area, 2020'].values[0]
total_land_area = country_data['Total Land Area, 2020'].values[0]

# Calculate the non-forest area
non_forest_area = total_land_area - forest_area

# Prepare data for plotting
labels = ['Forest Area', 'Non-Forest Area']
sizes = [forest_area, non_forest_area]
colors = ['green', 'red']  # Specify the colors here

# Create pie chart
plt.figure(figsize=(10, 5))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

# Set plot title
plt.title("Proportion of Ghana's Forest Area to Total Land Area in 2020")

# Show plot
plt.show()

import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame and you're looking at data for a specific country
country_data = forest[forest['Country and Area'] == 'Ghana']

# Get the forest area and total land area for a specific year
forest_area = country_data['Forest Area, 1990'].values[0]
total_land_area = country_data['Total Land Area, 2020'].values[0]

# Calculate the non-forest area
non_forest_area = total_land_area - forest_area

# Prepare data for plotting
labels = ['Forest Area', 'Non-Forest Area']
sizes = [forest_area, non_forest_area]
colors = ['green', 'red']  # Specify the colors here

# Create pie chart
plt.figure(figsize=(10, 5))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

# Set plot title
plt.title("Proportion of Ghana's Forest Area to Total Land Area in 1990")

# Show plot
plt.show()

import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame and you're looking at data for a specific country
country_data = forest[forest['Country and Area'] == 'Ghana']

# Get the forest area and total land area for a specific year
forest_area = country_data['Forest Area, 2010'].values[0]
total_land_area = country_data['Total Land Area, 2020'].values[0]

# Calculate the non-forest area
non_forest_area = total_land_area - forest_area

# Prepare data for plotting
labels = ['Forest Area', 'Non-Forest Area']
sizes = [forest_area, non_forest_area]
colors = ['green', 'red']  # Specify the colors here

# Create pie chart
plt.figure(figsize=(10, 5))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

# Set plot title
plt.title("Proportion of Ghana's Forest Area to Total Land Area in 2010")

# Show plot
plt.show()

import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame and you're looking at data for a specific country
country_data = forest[forest['Country and Area'] == 'Ghana']

# Get the forest area and total land area for a specific year
forest_area = country_data['Forest Area, 2000'].values[0]
total_land_area = country_data['Total Land Area, 2020'].values[0]

# Calculate the non-forest area
non_forest_area = total_land_area - forest_area

# Prepare data for plotting
labels = ['Forest Area', 'Non-Forest Area']
sizes = [forest_area, non_forest_area]
colors = ['green', 'red']  # Specify the colors here

# Create pie chart
plt.figure(figsize=(10, 5))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

# Set plot title
plt.title("Proportion of Ghana's Forest Area to Total Land Area in 2000")

# Show plot
plt.show()

# Get the forest area for 1990 and 2020
forest_area_1990 = ghana_data['Forest Area, 1990'].values[0]
forest_area_2020 = ghana_data['Forest Area, 2020'].values[0]

# Calculate the difference in forest area
difference = forest_area_2020 - forest_area_1990

# Calculate the percentage difference
percentage_difference = (difference / forest_area_1990) * 100

print(f"The difference in forest cover between 1990 and 2020 is {difference} hectares.")
print(f"This represents a change of {percentage_difference}%.")

import matplotlib.pyplot as plt
import numpy as np

# Identify the index of the row(s) where 'Country and Area' is 'World'
index_names = forest[forest['Country and Area'] == 'World'].index

# Drop these row(s) from the dataFrame
forest.drop(index_names, inplace=True)

# Select countries with the 2nd highest to the 11th highest deforestation rate
selected_deforestation = forest.nlargest(10, 'Deforestation, 2015-2020').iloc[1:]

# Create bar chart with different colors for each bar
plt.figure(figsize=(12, 6))
colors = plt.cm.viridis(np.linspace(0, 1, 10))
bars = plt.barh(selected_deforestation['Country and Area'], selected_deforestation['Deforestation, 2015-2020'], color=colors)

# Set plot title and labels with increased font size
plt.title('TOP 10 DEFORESTED COUNTRIES, 2015-2020', fontsize=20)
plt.xlabel('Deforestation Rate', fontsize=18)
plt.ylabel('Country', fontsize=18)

# Add gridlines
plt.grid(axis='x')

# Invert y-axis to display the country with highest rate at the top
plt.gca().invert_yaxis()

# Show plot
plt.show()

GHANA = pd.read_csv('/content/GHANA.csv')

GHANA
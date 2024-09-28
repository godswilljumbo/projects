# Airbnb NYC Data Analysis and Interactive Dashboard

<br/>

This project provides a detailed Exploratory Data Analysis (EDA) and an Interactive Dashboard for exploring Airbnb listings in New York City using the AB_NYC_2019.csv dataset. The dashboard is built using Plotly and Dash, allowing users to explore listings by neighborhood, price, and room type.

<br/>

### Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Key Features](#key-features)
4. [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
5. [Exploratory Data Analysis](#exploratory-data-analysis)
6. [Interactive Dashboard](#interactive-dashboard)
7. [Installation Instructions](#installation-instructions)
8. [Usage](#usage)
9. [Author](#author-credential)

<br/>

### Project Overview
The goal of this project is to analyze the Airbnb listings in New York City and provide insights through data visualizations and statistical analysis. Additionally, we offer a sophisticated interactive dashboard that allows users to explore Airbnb listings by selecting various filters such as neighborhood, price range, and room type.

<br/>

### Dataset
- Name: AB_NYC_2019.csv
- Source: Kaggle Airbnb NYC Dataset
- Size: ~49,000 Airbnb listings in New York City with features including:
   - id: Listing ID
   - name: Listing name
   - host_id: Host ID
   - neighbourhood_group: Borough (Manhattan, Brooklyn, etc.)
   - neighbourhood: Specific neighborhood
   - latitude: Latitude for geolocation
   - longitude: Longitude for geolocation
   - room_type: Type of room (Entire home/apt, Private room, etc.)
   - price: Price of the listing per night
   - minimum_nights: Minimum number of nights required for booking
   - number_of_reviews: Number of reviews for the listing
   - availability_365: Number of days available per year
   - reviews_per_month: Reviews per month

<br/>

### Key Features
- Data cleaning to handle missing values and outliers.
- Descriptive statistics to summarize the dataset and generate initial insights.
- Bivariate analysis to explore the relationships between different variables such as price, room_type, and neighbourhood_group.
- Geospatial analysis using latitude and longitude to map the distribution of listings in New York City.
- Interactive Dashboard to visualize and explore the dataset in real-time using:
      - A map showing listings based on the neighborhood and price.
      - A bar chart to explore room types by price and availability.

<br/>

### Data Cleaning and Preprocessing

Before performing the analysis, the dataset was cleaned to ensure accuracy and reliability:
- Missing Data: Columns like reviews_per_month had missing values, which were filled with 0. Unnecessary columns and rows with missing essential data were dropped.
- Outliers: Listings with extreme outliers in price and minimum_nights were identified and removed to ensure data quality.
- The price column was reformatted to currency data type.

<br/>

### Exploratory Data Analysis
Summary Statistics:
  - A detailed summary of numerical features (e.g., price, number of reviews) was produced.
  - Visualizations such as histograms and box plots were created to explore data distributions and detect outliers.

Key Insights:
  - Price Distribution: Most listings are priced under $500 per night, with a few outliers reaching over $1,000.
  - Room Type: Entire homes/apartments dominate the listings, followed by private rooms.
  - Neighbourhoods: Manhattan and Brooklyn have the most listings, with Manhattan having the highest average prices.

<br/>

### Interactive Dashboard

The interactive dashboard is designed to provide an easy-to-use interface for exploring the Airbnb data. Key features include:
  - Map Visualization: A map of Airbnb listings with filters for neighbourhood_group and price.
  - Room Type Analysis: A bar chart showing the distribution of listings by room type and their average price.
  - Filters: The user can filter the listings by borough, room type, and price range.
  - Interactive Maps: Geographical maps showing the distribution of listings across New York City.

<br/>

### Installation Instructions

To run the project locally, follow these steps:
Prerequisites
Make sure you have Python 3.x installed along with the following packages:
 - pandas
 - numpy
 - matplotlib
 - seaborn
 - plotly
 - dash
 - folium

You can install these required dependencies using:

    bash

    pip install pandas numpy matplotlib seaborn plotly dash folium

Running the Project
   - Clone or download the repository to your local machine.
   - Place the AB_NYC_2019.csv dataset in the same directory.
    Run the airbnb_dashboard.py script:

    bash

    python airbnb_dashboard.py

    Open your browser and navigate to http://127.0.0.1:8050/ to view the interactive dashboard.

<br/>

### Usage
Once the dashboard is running:
   - Select a borough from the dropdown to filter the listings.
   - Use the price slider to adjust the maximum price.
   - Explore the listings visually on the interactive map and analyze room types with the bar chart.

<br/>
<br/>
<br/>

## Author Credential 

<br/>

Godswill Sotonye Jumbo [Freelance Data Analyst] <br/>
godswill.j@outlook.com </br>
[GitHub Profile](https://www.github.com/godswilljumbo) <br/>
View my portfolio at [godswilljumbo.github.io](https://godswilljumbo.github.io)

<br/>
<br/>

<div align="center"> &copy; 2024 Godswill Jumbo. All rights reserved. </div>

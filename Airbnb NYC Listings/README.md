Airbnb NYC 2019 Analysis: EDA, Predictive Modeling & Dashboard
Project Overview

This project presents an in-depth Exploratory Data Analysis (EDA), predictive modeling, and an interactive dashboard based on the Airbnb NYC 2019 dataset. The dataset consists of over 48,000 listings in New York City and contains various attributes such as price, location, room type, and availability. The aim is to provide insights into the rental market and predict future pricing trends, along with an easy-to-use dashboard for data visualization.
Dataset Information

    Source: The dataset was obtained from Inside Airbnb.
    Description: The dataset contains the following features:
        id, name, host_id, host_name
        neighbourhood_group, neighbourhood
        latitude, longitude
        room_type, price, minimum_nights
        number_of_reviews, reviews_per_month
        availability_365

Project Objectives

    Data Cleaning and Preparation: Preprocessing and handling of missing data, outliers, and feature engineering.
    Exploratory Data Analysis (EDA): Understand key trends and insights within the Airbnb market in NYC.
    Predictive Modeling: Build a machine learning model to predict the price of Airbnb listings based on relevant features.
    Interactive Dashboard: Create a user-friendly dashboard to visualize data, trends, and model predictions.

Steps in the Analysis
1. Data Cleaning

    Handled missing values and removed outliers to improve data quality.
    Transformed variables to prepare for predictive modeling and dashboard integration.

2. Exploratory Data Analysis (EDA)

    Price Analysis: Visualized the price distribution of listings across NYC, focusing on different room types and neighborhoods.
    Neighborhood Insights: Analyzed which neighborhoods had the highest number of listings and compared their average prices.
    Host Activity: Investigated patterns in host behavior, including availability and the number of listings managed by individual hosts.

3. Predictive Modeling

    Model Objective: Predict the price of an Airbnb listing based on features like location, room type, and availability.
    Algorithms Used: Implemented various machine learning models, including:
        Linear Regression
        Random Forest Regressor
        Gradient Boosting
    Model Evaluation: Evaluated model performance using metrics like Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² score. The best-performing model was tuned for higher accuracy.
    Feature Importance: Determined the most significant features influencing price, such as room type and neighborhood.

4. Interactive Dashboard

    Technology: Built using Plotly and Dash.
    Features:
        Real-time filtering by neighborhood, room type, and price range.
        Interactive maps showing the geographic distribution of listings and pricing.
        Visualizations of the most important features affecting price predictions.

Key Findings

    Price Distribution: The majority of listings are priced under $200 per night, with premium listings concentrated in Manhattan.
    Room Type Impact: Entire homes/apartments are significantly more expensive compared to private or shared rooms.
    Neighborhood Popularity: Manhattan and Brooklyn dominate the Airbnb market, both in terms of listings and average price.
    Predictive Modeling: The Random Forest Regressor provided the best accuracy in predicting prices, with an RMSE of approximately X and R² of Y.
    Dashboard Insights: The dashboard allows for a dynamic exploration of Airbnb listings, enabling users to analyze pricing trends based on various filters and geographic regions.

Tools and Technologies

    Languages: Python
    Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Plotly, Dash
    IDE: Jupyter Notebook
    Version Control: Git
    Machine Learning: Linear Regression, Random Forest, Gradient Boosting

How to Run the Project
1. Clone the Repository

2. Install Required Libraries

3. Running the Jupyter Notebook

Run the Jupyter Notebook to explore the EDA and predictive modeling sections:
    jupyter notebook Airbnb_NYC_exploratory_analysis.ipynb

4. Running the Dashboard
    To view the interactive dashboard:

    python app.py


Conclusion

This project demonstrates how exploratory data analysis, predictive modeling, and interactive dashboards can provide insights into the Airbnb market in NYC. By understanding price trends and host behavior, users can make informed decisions whether they are hosts, renters, or data analysts.

Contact
For any inquiries or collaborations, feel free to reach out at godswill.j@outlook.com


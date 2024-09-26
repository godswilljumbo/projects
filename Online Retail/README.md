Customer Segmentation Using the Online Retail Dataset
Project Overview

This project involves customer segmentation using the Online Retail dataset from the UCI Machine Learning Repository. The primary objective is to categorize customers based on their purchasing behavior using RFM (Recency, Frequency, Monetary) analysis and clustering techniques like K-Means. Additionally, an interactive dashboard was built to visualize and analyze customer segments, providing valuable insights for business decisions.
Dataset Information

    Source: UCI Machine Learning Repository - Online Retail Dataset
    Description: This dataset contains transactional data from a UK-based online retail company (December 2010 to December 2011), including the following features:
        InvoiceNo: Unique invoice number.
        StockCode: Product code.
        Description: Product name.
        Quantity: Number of items sold.
        InvoiceDate: Date of the transaction.
        UnitPrice: Price per unit.
        CustomerID: Unique identifier for each customer.
        Country: Country of residence.

Project Objectives

    Data Cleaning: Remove missing values, duplicates, and preprocess the dataset.
    RFM Analysis: Perform Recency, Frequency, and Monetary analysis to profile customer behavior.
    Clustering: Apply K-Means clustering to segment customers based on RFM scores.
    Interactive Dashboard: Build a user-friendly dashboard to visualize customer segments and key features.
    Business Insights: Generate actionable insights for targeted marketing strategies and customer retention.

Methodology
1. Data Cleaning

    Missing Values: Removed rows with missing CustomerID.
    Duplicates: Eliminated duplicate records.
    Feature Engineering: Created new features such as TotalPrice (Quantity × UnitPrice) for monetary value analysis.

2. RFM Analysis

    Recency (R): How recently a customer made a purchase.

    Frequency (F): How often a customer makes purchases.

    Monetary (M): How much money a customer has spent.

    These scores help categorize customers based on their purchasing behaviors, allowing for detailed segmentation.

3. Clustering (K-Means)

    Feature Scaling: Applied MinMaxScaler to normalize RFM features.

    Elbow Method: Used the Elbow Method to determine the optimal number of clusters.

    K-Means Clustering: Segmented customers into distinct groups based on their RFM scores.

    Each cluster was profiled to understand the type of customers (e.g., high-value, frequent shoppers, or inactive customers).

4. Predictive Modeling

    Objective: Predict customer behaviors and potential future transactions.
    Algorithms: Evaluated different clustering models and provided a robust analysis for customer segmentation.

5. Interactive Dashboard

    Technology: Developed using Plotly and Dash for visualization.
    Features:
        Dynamic filtering based on RFM scores and clusters.
        Visual representation of customer segments.
        Key metrics like average recency, frequency, and monetary value displayed for each customer group.
        Insights into customer lifetime value and engagement rates.

Key Insights

    High-Value Customers: Customers with high recency, frequency, and monetary scores are high-value and should be targeted with loyalty and rewards programs.
    Low-Engagement Customers: Customers with low recency and frequency scores could benefit from re-engagement marketing efforts.
    Moderate-Value Customers: Frequent shoppers with moderate spending could be targeted for upselling or cross-selling.
    Dashboard Utility: The interactive dashboard enables businesses to monitor customer segmentation in real-time and make data-driven decisions.

Technologies and Tools

    Programming Language: Python
    Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Plotly, Dash
    Algorithms: K-Means Clustering
    Data Source: Online Retail Dataset from UCI

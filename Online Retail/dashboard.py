# For data manipulation and visualization
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# For clustering and segmentation
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# For building the dashboard
import plotly.express as px
import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

# Loading dataset and preprocessing
df = pd.read_excel(r"C:\Users\USER\Desktop\Portfolio\Datasets\Online_Retail.xlsx")

df = df.dropna(subset=['CustomerID'])
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)] 
df['TotalSpend'] = df['Quantity'] * df['UnitPrice']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create RFM metrics
latest_date = df['InvoiceDate'].max()
rfm = df.groupby('CustomerID').agg({
    'InvoiceNo': 'count',
    'InvoiceDate': lambda x: (latest_date - x.max()).days,
    'TotalSpend': 'sum'
}).rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalSpend': 'Monetary'
    })
rfm.reset_index(inplace=True)

# Scale the RFM data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# Top products by revenue
top_products = df.groupby('Description').agg({
    'TotalSpend': 'sum', 
    'Quantity': 'sum'
}).sort_values(by='TotalSpend', ascending=False).head(10).reset_index()

# Monthly revenue
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')
monthly_revenue = df.groupby('InvoiceMonth')['TotalSpend'].sum().reset_index()
monthly_revenue['InvoiceMonth'] = monthly_revenue['InvoiceMonth'].dt.to_timestamp()

# Correlation matrix for heatmap
corr_matrix = rfm[['Recency', 'Frequency', 'Monetary']].corr()

# Aggregating revenue by country
country_revenue = df.groupby('Country')['TotalSpend'].sum().reset_index()

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the dashboard
app.layout = dbc.Container(
    [
        # Header
        dbc.Row(dbc.Col(html.H1("Customer Segmentation Dashboard", style={
            'textAlign': 'center',
            'fontSize': 50,
            'fontWeight': 'bold',
            'backgroundColor': 'navy',
            'color': 'silver',
            'border': '3px solid blue',
            'padding': 40,
            'marginTop': 15,
            'fontFamily': 'verdana, sans-serif'
        }), className="mb-4")),

        # Key Metrics
        dbc.Row(
            [
                dbc.Col(dbc.Card(dbc.CardBody([html.H5("Total Customers"), html.H3(rfm['CustomerID'].nunique())], style={
                    'backgroundColor': 'forestgreen',
                    'textAlign': 'center',
                    'color': 'silver'})), width=3),
                dbc.Col(dbc.Card(dbc.CardBody([html.H5("Total Revenue"), html.H3(f"${rfm['Monetary'].sum():,.0f}")], style={
                    'backgroundColor': 'forestgreen',
                    'textAlign': 'center',
                    'color': 'silver'})), width=3),
                dbc.Col(dbc.Card(dbc.CardBody([html.H5("Average Frequency"), html.H3(f"{rfm['Frequency'].mean():.2f}")], style={
                    'backgroundColor': 'forestgreen',
                    'textAlign': 'center',
                    'color': 'silver'})), width=3),
                dbc.Col(dbc.Card(dbc.CardBody([html.H5("Average Recency"), html.H3(f"{rfm['Recency'].mean():.2f}")], style={
                    'backgroundColor': 'forestgreen',
                    'textAlign': 'center',
                    'color': 'silver'})), width=3),
            ],
            className="mb-4",
        ),
        # Table for Customer Details (optional)
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        html.Div(
                            dcc.Dropdown(
                                id="customer-dropdown",
                                options=[{'label': f'Customer {i}', 'value': i} for i in rfm['CustomerID']],
                                placeholder="Select a Customer",
                            )
                        )
                    ),
                ),
                width=12,
            ),
        ),

        dbc.Row(
            dbc.Col(
                html.Div(id="customer-info", className="mt-4"),
                width=12,
            ),
        ),
        # Revenue by Cluster Pie Chart
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id="revenue-by-cluster",
                        figure=px.pie(
                            rfm,
                            values="Monetary",
                            names="Cluster",
                            title="Revenue Contribution by Cluster",
                            hole=0.4,
                        ),
                    ),
                    width=6,
                ),
                dbc.Col(
                    dcc.Graph(
                        id="customer-count-by-cluster",
                        figure=px.bar(
                            rfm["Cluster"].value_counts().reset_index(name='count'),
                            x="Cluster",
                            y="count",
                            labels={"index": "Cluster", "count": "Customer Count"},
                            title="Customer Distribution by Cluster",
                        ),
                    ),
                    width=6,
                ),
            ]
        ),

        # Scatter plot for Frequency vs Monetary Value
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id="frequency-vs-monetary",
                        figure=px.scatter(
                            rfm,
                            x="Frequency",
                            y="Monetary",
                            color="Cluster",
                            size="Monetary",
                            hover_data=["CustomerID"],
                            title="Frequency vs Monetary Value by Cluster",
                        ),
                    ),
                    width=12,
                ),
            ]
        ),

        # Scatter plot for Recency vs Monetary Value
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id="recency-vs-monetary",
                        figure=px.scatter(
                            rfm,
                            x="Recency",
                            y="Monetary",
                            color="Cluster",
                            size="Monetary",
                            hover_data=["CustomerID"],
                            title="Recency vs Monetary Value by Cluster",
                        ),
                    ),
                    width=12,
                ),
            ]
        ),

        # Correlation Heatmap for RFM Metrics
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id="rfm-heatmap",
                        figure=go.Figure(data=go.Heatmap(
                            z=corr_matrix.values,
                            x=['Recency', 'Frequency', 'Monetary'],
                            y=['Recency', 'Frequency', 'Monetary'],
                            colorscale='Blues'
                        )).update_layout(title="Correlation Heatmap for RFM Metrics"),
                    ),
                    width=6,
                ),
                # Bar chart for top-selling products
                dbc.Col(
                    dcc.Graph(
                        id="top-products-bar",
                        figure=px.bar(
                            top_products,
                            x="Description",
                            y="TotalSpend",
                            title="Top-Selling Products by Revenue"
                        ),
                    ),
                    width=6,
                ),
            ]
        ),

        # Time Series of Monthly Revenue
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id="monthly-revenue",
                        figure=px.line(
                            monthly_revenue,
                            x="InvoiceMonth",
                            y="TotalSpend",
                            title="Monthly Revenue Over Time"
                        ),
                    ),
                    width=12,
                ),
            ]
        ),
        
        # Geographical visualization: Revenue by Country
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id="revenue-by-country-map",
                        figure=go.Figure(data=go.Choropleth(
                            locations=country_revenue['Country'],  # ISO-3 country codes or full country names
                            z=country_revenue['TotalSpend'],
                            locationmode='country names',
                            colorscale='Blues',
                            marker_line_color='darkgray',
                            marker_line_width=0.5
                        )).update_layout(
                            title_text='Revenue by Country',
                            geo=dict(showframe=False, showcoastlines=False, projection_type='equirectangular')
                        )
                    ),
                    width=12,
                ),
            ]
        ),
    ],
    fluid=True,
    style={'background':'grey'}
)

# Callback to display customer-specific information
@app.callback(
    Output("customer-info", "children"),
    Input("customer-dropdown", "value")
)
def display_customer_info(customer_id):
    if customer_id is None:
        return "No customer selected"
    elif rfm[rfm['CustomerID'] == customer_id].empty:
        return "Customer not found."
    else:
        selected_customer = rfm[rfm['CustomerID'] == customer_id].iloc[0]
        return html.Div(
            [
                html.H4(f"Customer ID: {customer_id}"),
                html.P(f"Frequency: {selected_customer['Frequency']}"),
                html.P(f"Recency: {selected_customer['Recency']}"),
                html.P(f"Monetary: {selected_customer['Monetary']}"),
                html.P(f"Cluster: {selected_customer['Cluster']}"),
            ]
        )


if __name__ == "__main__":
    app.run_server(debug=True)
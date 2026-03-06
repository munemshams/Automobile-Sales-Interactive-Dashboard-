# Automobile Sales Interactive Dashboard

This project builds an **interactive data visualization dashboard using Python, Dash, and Plotly** to analyze automobile sales trends across different economic conditions.

The dashboard allows users to explore **automobile sales statistics during recession and non-recession periods**, providing insights into how economic factors such as **consumer confidence, unemployment rate, vehicle price, and advertising expenditure** affect automobile sales.

The dashboard is fully interactive and runs locally as a **web application**.

---

# Project Overview

The objective of this project is to analyze historical automobile sales data and provide interactive visualizations to help understand how different economic indicators impact automobile sales.

Users can interact with the dashboard to view different analytical perspectives such as:

- Yearly automobile sales trends
- Sales distribution by vehicle type
- Impact of consumer confidence
- Relationship between unemployment rate and automobile sales
- Advertising expenditure distribution

The dashboard dynamically updates visualizations based on user selections.

---

# Dashboard Features

The dashboard provides two main analysis modes:

### 1. Yearly Statistics

Users can select a specific year and explore:

- Automobile sales by vehicle type
- Average automobile sales trends across years
- Vehicle price vs automobile sales relationship
- Advertising expenditure distribution by vehicle type

---

### 2. Recession Period Statistics

This mode focuses on analyzing sales behavior during economic recessions.

Visualizations include:

- Automobile sales by vehicle type during recession
- Average automobile sales trends during recession periods
- Consumer confidence vs automobile sales
- Impact of unemployment rate on automobile sales

---

# Interactive Controls

The dashboard includes two dropdown menus:

### Statistics Selector
Allows users to choose between:

- Yearly Statistics
- Recession Period Statistics

### Year Selector
Allows users to select a specific year to analyze when the **Yearly Statistics** mode is selected.

---

# Files Included

| File | Description |
|-----|-------------|
| dashboard.py | Main Python script that runs the interactive Dash dashboard |
| automobile_sales.csv | Dataset containing automobile sales and economic indicators |
| README.md | Project documentation |

---

# Dataset Description

The dataset contains historical automobile sales data along with several economic indicators.

Key dataset variables include:

| Column | Description |
|------|-------------|
| Year | Year of the observation |
| Month | Month of the observation |
| Automobile_Sales | Total automobile sales |
| Vehicle_Type | Category of vehicle |
| Price | Average vehicle price |
| Advertising_Expenditure | Advertising budget |
| Consumer_Confidence | Consumer confidence index |
| Unemployment_Rate | Unemployment rate |
| Recession | Indicator showing recession period |

These variables help analyze how economic conditions influence automobile sales.

---

# Python Libraries Used

The project uses the following Python libraries:

- Dash
- Plotly
- Pandas

Dash provides the framework for building the interactive web application, while Plotly is used for creating dynamic visualizations.

---

# How the Dashboard Works

The dashboard is built using **Dash callbacks**, which allow the application to dynamically update visualizations whenever user inputs change.

The workflow is:

1. Load the dataset using Pandas
2. Initialize a Dash application
3. Create dropdown menus for user input
4. Use Dash callbacks to respond to user selections
5. Generate Plotly charts dynamically
6. Display charts in the browser interface

This approach allows real-time interaction with the dataset.

---

# How to Run the Project

Run the dashboard locally using the following command:

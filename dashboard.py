import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("automobile_sales.csv")

# -----------------------------
# Create Dash App
# -----------------------------
app = dash.Dash(__name__)
app.title = "Automobile Sales Dashboard"

# Dropdown options
dropdown_options = [
    {"label": "Yearly Statistics", "value": "Yearly Statistics"},
    {"label": "Recession Period Statistics", "value": "Recession Period Statistics"}
]

year_list = sorted(df["Year"].unique())

# -----------------------------
# Layout
# -----------------------------
app.layout = html.Div([

    html.H1(
        "Automobile Sales Statistics Dashboard",
        style={"textAlign": "center"}
    ),

    html.Div([

        html.Div([
            html.Label("Select Statistics:"),
            dcc.Dropdown(
                id="dropdown-statistics",
                options=dropdown_options,
                value="Yearly Statistics",
                clearable=False
            )
        ], style={"width": "48%", "display": "inline-block"}),

        html.Div([
            html.Label("Select Year:"),
            dcc.Dropdown(
                id="select-year",
                options=[{"label": i, "value": i} for i in year_list],
                value=year_list[0],
                clearable=False
            )
        ], style={"width": "48%", "display": "inline-block"})

    ]),

    html.Br(),

    html.Div(id="output-container")

])

# -----------------------------
# Callback Function
# -----------------------------
@app.callback(
    Output("output-container", "children"),
    Input("dropdown-statistics", "value"),
    Input("select-year", "value")
)
def update_dashboard(statistics, year):

    # -----------------------------
    # Recession Statistics
    # -----------------------------
    if statistics == "Recession Period Statistics":

        recession_data = df[df["Recession"] == 1]

        fig1 = px.bar(
            recession_data.groupby("Vehicle_Type")["Automobile_Sales"].sum().reset_index(),
            x="Vehicle_Type",
            y="Automobile_Sales",
            title="Automobile Sales by Vehicle Type (Recession)"
        )

        fig2 = px.line(
            recession_data.groupby("Year")["Automobile_Sales"].mean().reset_index(),
            x="Year",
            y="Automobile_Sales",
            title="Average Automobile Sales During Recession"
        )

        fig3 = px.scatter(
            recession_data,
            x="Consumer_Confidence",
            y="Automobile_Sales",
            color="Vehicle_Type",
            title="Consumer Confidence vs Automobile Sales"
        )

        fig4 = px.line(
            recession_data.groupby(["Unemployment_Rate", "Vehicle_Type"])["Automobile_Sales"]
            .mean()
            .reset_index(),
            x="Unemployment_Rate",
            y="Automobile_Sales",
            color="Vehicle_Type",
            title="Unemployment Rate vs Automobile Sales"
        )

        return [

            html.Div([
                dcc.Graph(figure=fig1),
                dcc.Graph(figure=fig2)
            ]),

            html.Div([
                dcc.Graph(figure=fig3),
                dcc.Graph(figure=fig4)
            ])

        ]

    # -----------------------------
    # Yearly Statistics
    # -----------------------------
    else:

        yearly_data = df[df["Year"] == year]

        fig1 = px.bar(
            yearly_data.groupby("Vehicle_Type")["Automobile_Sales"].sum().reset_index(),
            x="Vehicle_Type",
            y="Automobile_Sales",
            title="Automobile Sales by Vehicle Type"
        )

        fig2 = px.line(
            df.groupby("Year")["Automobile_Sales"].mean().reset_index(),
            x="Year",
            y="Automobile_Sales",
            title="Average Automobile Sales per Year"
        )

        fig3 = px.scatter(
            yearly_data,
            x="Price",
            y="Automobile_Sales",
            color="Vehicle_Type",
            title="Vehicle Price vs Automobile Sales"
        )

        fig4 = px.pie(
            yearly_data,
            values="Advertising_Expenditure",
            names="Vehicle_Type",
            title="Advertising Expenditure by Vehicle Type"
        )

        return [

            html.Div([
                dcc.Graph(figure=fig1),
                dcc.Graph(figure=fig2)
            ]),

            html.Div([
                dcc.Graph(figure=fig3),
                dcc.Graph(figure=fig4)
            ])

        ]


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)

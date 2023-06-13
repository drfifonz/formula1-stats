from dash import dcc, html
import pandas as pd
import numpy as np

# import geopandas as gpd


YEAR = 2022


races_df = pd.read_csv("data/races.csv")
circuits_df = pd.read_csv("data/circuits.csv")
years = np.sort(races_df["year"].unique()).tolist()


year_tab = html.Div(
    [
        html.H1("YEAR DATA"),
        dcc.Dropdown(id="years-dropdown", options=[{"label": i, "value": i} for i in years], value=2022),
        html.Div(id="page-1-content"),
        html.Div(className="year-travel-fig", children=[dcc.Graph(figure={}, id="year-travel-map")]),
    ]
)

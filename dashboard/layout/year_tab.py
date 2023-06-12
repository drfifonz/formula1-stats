from dash import dcc, html
import pandas as pd
import numpy as np

# import geopandas as gpd


YEAR = 2022


races_df = pd.read_csv("data/races.csv")
circuits_df = pd.read_csv("data/circuits.csv")
YEARS = np.sort(races_df["year"].unique()).tolist()

yaer_tabs = dcc.Tabs(
    id="year-tabs",
    # value="year-map",
    value="year-stats",
    className="custom-tabs-container",
    children=[
        dcc.Tab(
            label="Map",
            value="year-map",
            className="custom-tab",
            selected_className="custom-tab--selected",
        ),
        dcc.Tab(
            label="Year stats",
            value="year-stats",
            className="custom-tab",
            selected_className="custom-tab--selected",
        ),
    ],
)


year_tabs_content = html.Div(id="tabs-year-content", className="main-panel")


year_tab = html.Div(
    [
        html.H1("YEAR DATA"),
        dcc.Dropdown(id="years-dropdown", options=[{"label": i, "value": i} for i in YEARS], value=2022),
        yaer_tabs,
        year_tabs_content,
    ]
)

# year_tab = html.Div(
#     [
#         html.H1("YEAR DATA"),
#         dcc.Dropdown(id="years-dropdown", options=[{"label": i, "value": i} for i in years], value=2022),
#         # html.Div(id="page-1-content"),
#         html.Div(className="year-travel-fig", children=[dcc.Graph(figure={}, id="year-travel-map")]),
#     ]
# )

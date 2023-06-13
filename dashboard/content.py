# content.py
from dash import dcc, html
from dashboard.index import app
from dashboard.layout.callbacks import *  # noqa: F401, F403

tabs = dcc.Tabs(
    id="app-tabs",
    value="travel-year-tab",
    className="custom-tabs-container",
    children=[
        dcc.Tab(
            label="DataFrame",
            value="tab-3",
            className="dataframe-tab",
            selected_className="custom-tab--selected",
        ),
        dcc.Tab(
            label="F1 Map Analysis",
            value="tab-2",
            className="map-analysis-tab",
            selected_className="custom-tab--selected",
        ),
        dcc.Tab(
            label="F1 Data By Year",
            value="travel-year-tab",
            className="year-data-tab",
            selected_className="custom-tab--selected",
        ),
    ],
)
tabs_content = html.Div(id="tabs-example-content", className="main-panel")
logo = html.Div(id="logo-f1", className="logo-f1")
app.layout = html.Div(
    [
        # header,
        logo,
        tabs,
        tabs_content,
    ]
)

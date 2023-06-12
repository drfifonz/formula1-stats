# content.py
from dash import dcc, html

from dashboard.index import app
from dashboard.layout.callbacks import *  # noqa: F401, F403

tabs = dcc.Tabs(
    id="app-tabs",
    value="tab-1",
    className="custom-tabs-container",
    children=[
        dcc.Tab(
            label="Tab1",
            value="tab-1",
            className="custom-tab",
            selected_className="custom-tab--selected",
        ),
        dcc.Tab(
            label="Tab2",
            value="tab-2",
            className="custom-tab",
            selected_className="custom-tab--selected",
        ),
        dcc.Tab(
            label="Tab3-example",
            value="tab-3",
            className="custom-tab",
            selected_className="custom-tab--selected",
        ),
        dcc.Tab(
            label="Year data",
            value="yaer-tab",
            className="custom-tab",
            selected_className="custom-tab--selected",
        ),
    ],
)
tabs_content = html.Div(id="tabs-example-content", className="main-panel")
app.layout = html.Div(
    [
        # header,
        tabs,
        tabs_content,
    ]
)

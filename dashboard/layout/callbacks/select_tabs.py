# callbacks2.py
from dashboard.index import app
from dashboard.layout.tab_1 import tab_1
from dashboard.layout.tab_2 import tab_2
from dashboard.layout.tab_3 import tab_3
from dashboard.layout.year_tab import year_tab
from dash.dependencies import Input, Output


@app.callback(Output("tabs-example-content", "children"), Input("app-tabs", "value"))
def select_tabs(tab):
    if tab == "tab-1":
        # print(tab)
        return tab_1
    elif tab == "tab-2":
        return tab_2
    elif tab == "tab-3":
        return tab_3
    elif tab == "yaer-tab":
        return year_tab

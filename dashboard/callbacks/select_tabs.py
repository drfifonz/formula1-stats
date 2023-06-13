<<<<<<< HEAD:dashboard/callbacks/select_tabs.py
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
=======
# callbacks2.py
from dashboard.index import app
from dashboard.layout.tab_1 import tab_1
from dashboard.layout.tab_2 import tab_2
from dashboard.layout.tab_3 import tab_3
from dashboard.layout.year_tab import year_tab

# import tabs for year tab
from dashboard.layout.year_map import year_map
from dashboard.layout.year_stats import year_stats


# from dashboard.layout.stats_year import stats_year
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
    elif tab == "travel-year-tab":
        return year_tab
    # elif tab == "stats-year-tab":
    #     return stats_year


@app.callback(Output("tabs-year-content", "children"), Input("year-tabs", "value"))
def select_year_tabs(tab):
    if tab == "year-map":
        return year_map
    elif tab == "year-stats":
        return year_stats
>>>>>>> 44c3a6036ca7cb19d0820bc3f869ca088c520c0e:dashboard/layout/callbacks/select_tabs.py

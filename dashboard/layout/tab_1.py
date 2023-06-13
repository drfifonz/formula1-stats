from dash import dcc, html

tab_1 = html.Div(
    [
        html.H1("Page 1"),
        dcc.Dropdown(
            id="page-1-dropdown", options=[{"label": i, "value": i} for i in ["LA", "NYC", "MTL"]], value="LA"
        ),
        html.Div(id="page-1-content"),
    ]
)

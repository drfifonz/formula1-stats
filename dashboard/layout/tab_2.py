from dash import dcc, html

tab_2 = html.Div(
    [
        html.H1("Page 2"),
        dcc.RadioItems(
            id="page-2-radios", options=[{"label": i, "value": i} for i in ["Orange", "Blue", "Red"]], value="Orange"
        ),
        html.Div(id="page-2-content"),
    ]
)

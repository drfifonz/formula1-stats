from dash import dcc, html

year_stats = html.Div(
    [
        html.H1("Choose race in selected season"),
        dcc.Dropdown(id="race-dropdown", options={}, value=""),
        html.Div(className="race-pace", children=[dcc.Graph(figure={}, id="race-pace-fig")]),
        html.Img(id="race-fig-map"),
    ]
)

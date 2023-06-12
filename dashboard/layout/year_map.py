from dash import dcc, html


year_map = html.Div(
    [
        html.H1("YEAR MAP"),
        html.Div(id="year-map-content"),
        html.Div(className="year-travel-fig", children=[dcc.Graph(figure={}, id="year-travel-map")]),
    ]
)

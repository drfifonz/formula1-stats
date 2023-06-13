from dash import dcc, html


year_map = html.Div(
    [
        html.H1("Formula 1 races in selected season"),
        html.Div(id="year-map-content"),
        html.Div(className="year-travel-fig", children=[dcc.Graph(figure={}, id="year-travel-map")]),
    ]
)

import pandas as pd
from dash import dash_table, dcc, html


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")


tab_3 = html.Div(
    [
        html.Div(
            className="row",
            children="My First App with Data, Graph, and Controls",
            style={"textAlign": "center", "color": "blue", "fontSize": 30},
        ),
        html.Div(
            className="row",
            children=[
                dcc.RadioItems(
                    options=["pop", "lifeExp", "gdpPercap"],
                    value="lifeExp",
                    inline=True,
                    id="my-radio-buttons-final",
                )
            ],
        ),
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="six columns",
                    children=[
                        dash_table.DataTable(
                            data=df.to_dict("records"), page_size=11, style_table={"overflowX": "auto"}
                        )
                    ],
                ),
                html.Div(className="six columns", children=[dcc.Graph(figure={}, id="histo-chart-final")]),
            ],
        ),
    ]
)

import pandas as pd
import plotly.express as px
from dash import Input, Output, dash_table, dcc, html

from dashboard.index import app

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


@app.callback(
    Output(component_id="my-final-graph-example", component_property="children"),
    Input(component_id="my-final-radio-item-example", component_property="value"),
)
def update_graph(col_chosen):
    print("Xxxxxxxxxxxxxxxx")
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig

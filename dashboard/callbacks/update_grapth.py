from dashboard.index import app
import plotly.express as px


from dashboard.layout.tab_3 import df
from dash.dependencies import Input, Output


@app.callback(
    Output(component_id="histo-chart-final", component_property="figure"),
    Input(component_id="my-radio-buttons-final", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig

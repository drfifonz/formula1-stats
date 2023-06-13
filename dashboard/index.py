from dash import Dash
import pandas as pd
from layout import tab_2
from callbacks.update_graph import register_callbacks

# Load data
races_df = pd.read_csv('data/races.csv')
circuits_df = pd.read_csv('data/circuits.csv')
drivers_df = pd.read_csv('data/drivers.csv')
constructors_df = pd.read_csv('data/constructors.csv')
constructor_standings_df = pd.read_csv('data/constructor_standings.csv')
driver_standings_df = pd.read_csv('data/driver_standings.csv')

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)

app_title = "Formula 1 Dashboard"
app.title = app_title

app.layout = tab_2.get_layout(races_df)

register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
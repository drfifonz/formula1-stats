# index.py
from dash import Dash


# external_stylesheets = [dbc.themes.BOOTSTRAP, "./assets/style.css"]
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)
app_title = "Formula 1 Dashboard"
app.title = app_title

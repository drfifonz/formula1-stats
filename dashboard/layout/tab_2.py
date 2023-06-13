import dash
from dash import dcc, html

def get_layout(races_df):
    return html.Div([
        html.H1("Formula 1 Races Analysis"),

        # Dropdown for selecting the minimum year
        dcc.Dropdown(
            id='min-year-dropdown',
            options=[{'label': str(year), 'value': year} for year in sorted(races_df['year'].unique())],
            value=races_df['year'].min(),
            clearable=False,
            style={'width': '200px'}
        ),

        # Dropdown for selecting the maximum year
        dcc.Dropdown(
            id='max-year-dropdown',
            options=[{'label': str(year), 'value': year} for year in sorted(races_df['year'].unique())],
            value=races_df['year'].max(),
            clearable=False,
            style={'width': '200px'}
        ),

        dcc.Graph(id='f1-map')
    ])
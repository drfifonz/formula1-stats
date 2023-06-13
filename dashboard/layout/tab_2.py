from dash import dcc, html
import pandas as pd

races_df = pd.read_csv('data/races.csv')

map_data = html.Div([
    html.H1("Formula 1 Races Analysis"),

    html.H3("Short informations about Formula 1 number of races, last race and winner per country"),
    
    html.Div([
        # Dropdown for selecting the minimum year
        dcc.Dropdown(
            id='min-year-dropdown',
            options=[{'label': str(year), 'value': year} for year in sorted(races_df['year'].unique())],
            value=races_df['year'].min(),
            clearable=False,
            style={'width': '150px'}
        ),
        html.H5(" - ", style={'margin': '0 15px'}),
        # Dropdown for selecting the maximum year
        dcc.Dropdown(
            id='max-year-dropdown',
            options=[{'label': str(year), 'value': year} for year in sorted(races_df['year'].unique())],
            value=races_df['year'].max(),
            clearable=False,
            style={'width': '150px'}
        ),
    ], style={'display': 'flex', 
              'align-items': 'center',
              'margin-left': '38%'}),

    html.H6("Log number of F1 races", id="log-map"),
    dcc.Graph(id='f1-map')
])
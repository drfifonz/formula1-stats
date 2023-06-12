import pandas as pd
import geopandas as gpd
import plotly.graph_objs as go
import json
import numpy as np
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load data
races_df = pd.read_csv('data/races.csv')
circuits_df = pd.read_csv('data/circuits.csv')
drivers_df = pd.read_csv('data/drivers.csv')
constructors_df = pd.read_csv('data/constructors.csv')
constructor_standings_df = pd.read_csv('data/constructor_standings.csv')
driver_standings_df = pd.read_csv('data/driver_standings.csv')

# Map country names
country_mapping = {
    'UK': 'United Kingdom',
    'USA': 'United States of America',
    'UAE': 'United Arab Emirates',
    'Korea': 'South Korea',
}

# Load map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# DASH BOARD
app = dash.Dash(__name__)

# Define dashboard
# app.layout = html.Div([
#     html.H1("Formula 1 Races Analysis"),

#     dcc.RangeSlider(
#         id='year-slider',
#         min=races_df['year'].min(),
#         max=races_df['year'].max(),
#         step=1,
#         marks={str(year): str(year) for year in races_df['year'].unique()},
#         value=[races_df['year'].min(), races_df['year'].max()]
#     ),

#     dcc.Graph(id='f1-map')
# ])

app.layout = html.Div([
    html.H1("Formula 1 Races Analysis"),

    # Dropdown for selecting the minimum year
    dcc.Dropdown(
        id='min-year-dropdown',
        options=[{'label': str(year), 'value': year} for year in races_df['year'].unique()],
        value=races_df['year'].min(),
        clearable=False,
        style={'width': '200px'}
    ),

    # Dropdown for selecting the maximum year
    dcc.Dropdown(
        id='max-year-dropdown',
        options=[{'label': str(year), 'value': year} for year in races_df['year'].unique()],
        value=races_df['year'].max(),
        clearable=False,
        style={'width': '200px'}
    ),

    dcc.Graph(id='f1-map')
])

# @app.callback(
#     Output('f1-map', 'figure'),
#     [Input('year-slider', 'value')]
# )
@app.callback(
    Output('f1-map', 'figure'),
    [Input('min-year-dropdown', 'value'), Input('max-year-dropdown', 'value')]
)
def update_graph(min_selected_year, max_selected_year):
    full_df = pd.merge(races_df, circuits_df, on='circuitId')
    full_df['country'] = full_df['country'].replace(country_mapping)
    filtered_df = full_df[(full_df['year'] >= min_selected_year) & (full_df['year'] <= max_selected_year)]

    # Races by country
    country_races = filtered_df['country'].value_counts().reset_index()
    country_races.columns = ['country', 'count']

    # Winners
    constructor_standings_with_constructors_df = pd.merge(constructor_standings_df, constructors_df, on='constructorId')
    driver_standings_with_drivers_df = pd.merge(driver_standings_df, drivers_df, on='driverId')

    filtered_df = filtered_df.merge(constructor_standings_with_constructors_df[constructor_standings_with_constructors_df['wins'] > 0], on='raceId', suffixes=('_race', '_constructor'))
    filtered_df = filtered_df.merge(driver_standings_with_drivers_df[driver_standings_with_drivers_df['wins'] > 0], on='raceId', suffixes=('', '_driver'))

    # Merge
    merged = world.set_index('name').join(country_races.set_index('country'))
    merged['count'] = merged['count'].fillna(0)
    merged['log_count'] = np.log(merged['count'] + 1)
    merged_json = json.loads(merged.to_json())

    latest_race_in_country = filtered_df.sort_values('date', ascending=False).drop_duplicates(subset='country')

    # Prepare pop-up
    hover_text = []
    for country in merged.index:
        if merged.loc[country, 'count'] > 0:
            race_row = latest_race_in_country[latest_race_in_country['country'] == country]
            race_count = merged.loc[country, 'count']
            if not race_row.empty:
                race_text = (f'Total Races: <b>{str(int(race_count)) if race_count > 0 else "No Races"}</b><br>'
                             f'Most recent race: <b>{race_row.iloc[0]["name_x"]}</b><br>'
                             f'Winner: <b>{race_row.iloc[0]["forename"]} {race_row.iloc[0]["surname"]}</b>, '
                             f'<b>{race_row.iloc[0]["name_y"]}</b>')
                hover_text.append(race_text)
            else:
                race_text = (f'Total Races: <b>{str(int(race_count)) if race_count > 0 else "No Races"}</b><br>')
                hover_text.append(race_text)
        else:
            hover_text.append(f'No data for {country}')

    # Prepare plot
    data = go.Choropleth(
        geojson=merged_json,
        locations=merged.index,
        z=merged['log_count'],
        text=hover_text,
        colorscale=[
            [0, 'gray'],
            [0.01, 'yellow'],
            [0.7, 'orange'],
            [1, 'red']
        ],
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title='Log number of F1 races',
    )

    layout = go.Layout(
        title_text='Short informations about Formula 1 number of races, last race and winner per country',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        autosize=False,
        width=1880,
        height=820
    )

    fig = go.Figure(data=data, layout=layout)

    return fig

# Dash app
if __name__ == "__main__":
    app.run_server(debug=True)

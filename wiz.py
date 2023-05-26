import pandas as pd
import geopandas as gpd
import plotly.graph_objs as go
import json
import numpy as np

races_df = pd.read_csv('data/races.csv')
circuits_df = pd.read_csv('data/circuits.csv')

full_df = pd.merge(races_df, circuits_df, on='circuitId')

country_mapping = {
    'UK': 'United Kingdom',
    'USA': 'United States of America',
    'UAE': 'United Arab Emirates',
    'Korea': 'South Korea'
}

full_df['country'] = full_df['country'].replace(country_mapping)

country_races = full_df['country'].value_counts().reset_index()
country_races.columns = ['country', 'count']

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

merged = world.set_index('name').join(country_races.set_index('country'))

merged['count'] = merged['count'].fillna(0)

merged['log_count'] = np.log(merged['count'] + 1) 
merged_json = json.loads(merged.to_json())


hover_text = ["Races " + str(int(count)) if count > 0 else "No Races" for count in merged['count']]

data = go.Choropleth(
    geojson=merged_json,
    locations=merged.index,
    z=merged['log_count'],  
    text=hover_text,  
    autocolorscale=True,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title='Log number of F1 races',  
)

layout = go.Layout(
    title_text='Number of Formula 1 races per country',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    autosize=True,
)

fig = go.Figure(data=data, layout=layout)
fig.show()

import pandas as pd
from dash import dash_table, dcc, html

country_mapping = {
    'UK': 'United Kingdom',
    'USA': 'United States of America',
    'UAE': 'United Arab Emirates',
    'Korea': 'South Korea',
}

# Load data
races_df = pd.read_csv('data/races.csv')
circuits_df = pd.read_csv('data/circuits.csv')
drivers_df = pd.read_csv('data/drivers.csv')
constructors_df = pd.read_csv('data/constructors.csv')
constructor_standings_df = pd.read_csv('data/constructor_standings.csv')

full_df = pd.merge(races_df, circuits_df, on='circuitId')
full_df['country'] = full_df['country'].replace(country_mapping)
full_df = full_df.drop(['raceId', 'circuitId'], axis = 1)
drivers_df = drivers_df.drop(['driverId'], axis = 1)
full_df = full_df.rename(columns={
    "name_x": "Race name",
    "url_x": "Race wikipedia Url",
    "name_y": "Circuit name",
    "year": "Race year",
    "round": "Race round",
    "date": "Race date",
    "time": "Time",
    "location": "Location",
    "url_y": "Circuit wikipedia url",
})
drivers_df = drivers_df.rename(columns={
    "driverRef": "Driver's shorten name",
    "number": "Number",
    "code": "Driver's code",
    "forename": "Driver's forename",
    "surname": "Driver's surname",
    "nationality": "Driver's nationality",
    "url": "Wikipedia url about driver",
})

tab_3 = html.Div(
    [
        html.Div(
            className="f1-dataset",
            children="DataFrame of F1, used in our project",
        ),
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="",
                    children=[
                        dash_table.DataTable(
                            data=full_df.to_dict("records"), page_size=11, style_table={"overflowX": "auto"}
                        )
                    ],
                ),
            ],
        ),
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="",
                    children=[
                        dash_table.DataTable(
                            data=drivers_df.to_dict("records"), page_size=11, style_table={"overflowX": "auto"}
                        )
                    ],
                ),
            ],
        ),
    ]
)

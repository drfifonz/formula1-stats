import numpy as np
from dashboard.index import app
import pandas as pd
import base64
from io import BytesIO
import plotly.graph_objs as go
from dashboard.layout.year_tab import races_df, circuits_df
from dash.dependencies import Input, Output
import seaborn as sns
import matplotlib.pyplot as plt
import time
import matplotlib
from datetime import datetime

matplotlib.use("agg")
lap_times_df = pd.read_csv("data/lap_times.csv")
drivers_df = pd.read_csv("data/drivers.csv")


@app.callback(
    Output(component_id="year-travel-map", component_property="figure"),
    Input(component_id="years-dropdown", component_property="value"),
)
def travel_map_by_year(year):
    YEAR = year
    races_year = races_df[races_df["year"] == YEAR][
        [
            "round",
            "raceId",
            "date",
            "name",
            "circuitId",
        ]
    ]
    races_year = races_year.sort_values(by="round", ascending=True)

    circuit_year = circuits_df[["circuitId", "location", "lat", "lng", "alt"]]

    races_year = races_year.merge(circuit_year, on="circuitId", how="left")

    fig = go.Figure()

    fig.add_trace(
        go.Scattergeo(
            locationmode="USA-states",
            lon=races_year["lng"],
            lat=races_year["lat"],
            hoverinfo="text",
            text=races_year["name"],
            mode="markers",
            marker=dict(size=6, color="rgb(255, 0, 0)", line=dict(width=3, color="rgba(68, 68, 68, 0)")),
        )
    )

    # Add traces, one for each slider step
    for i in range(len(races_year) - 1):
        fig.add_trace(
            go.Scattergeo(
                # locationmode = 'USA-states',
                visible=False,
                lon=[races_year["lng"][i], races_year["lng"][i + 1]],
                lat=[races_year["lat"][i], races_year["lat"][i + 1]],
                mode="lines",
                line=dict(width=2, color="red"),
                opacity=0.5,
                # text="lupka",
                # hovertext="123",
                hoverinfo="text",
                showlegend=False,
                text=races_year["name"][i],
            )
        )

    # Create and add slider
    steps = []
    for i in range(len(fig.data)):
        step = dict(
            method="update",
            args=[
                {"visible": [False] * len(fig.data)},
            ],
        )
        for j in range(len(fig.data)):
            if j <= i:
                step["args"][0]["visible"][j] = True
        steps.append(step)

    sliders = [
        dict(
            active=0,
            currentvalue={
                "prefix": "Grand Prix tour: ",
            },
            steps=steps,
        )
    ]

    fig.update_layout(
        title_text=f"{YEAR} season",
        showlegend=False,
        width=1660,
        height=820,
        paper_bgcolor="white",
        sliders=sliders,
    )

    return fig


@app.callback(
    Output(component_id="race-fig-map", component_property="src"),
    # Output(component_id="race-pace-fig", component_property="figure"),
    Input(component_id="race-dropdown", component_property="value"),
)
def update_box_plot(raceId):
    df_boxplot = lap_times_df.loc[lap_times_df["raceId"] == raceId]

    df_boxplot = df_boxplot[["driverId", "time", "milliseconds"]]

    df_boxplot = pd.merge(df_boxplot, drivers_df[["driverId", "surname"]], on="driverId")

    driver_names = df_boxplot["surname"].unique().tolist()
    boxplot_res = pd.DataFrame()
    for driver in driver_names:
        driver_data = df_boxplot.loc[df_boxplot["surname"] == driver].sort_values(by="milliseconds")
        boxplot_res = pd.concat([boxplot_res, driver_data])

    df_boxplot = df_boxplot

    fig, ax = plt.subplots(figsize=(14, 9), dpi=120)
    boxplot = sns.boxplot(data=boxplot_res, x="milliseconds", y="surname", orient="h")
    formatter = matplotlib.ticker.FuncFormatter(lambda ms, _: time.strftime("%M:%S.000", time.gmtime(ms / 1000)))
    ax.xaxis.set_major_formatter(formatter)

    ax.grid(True)
    ax.set_xlabel("Lap time")
    ax.set_ylabel("Driver surname")
    ax.set_title("Drivers race pace")

    buf = BytesIO()
    fig.savefig(buf, format="png")
    plt.close()
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    buf.close()
    return f"data:image/png;base64,{data}"


@app.callback(
    Output(component_id="race-pace-fig", component_property="figure"),
    Input(component_id="race-dropdown", component_property="value"),
)
def plot_pace_fig(raceId):
    df_line = lap_times_df.loc[lap_times_df["raceId"] == raceId]

    data = [
        go.Scatter(
            x=df_line["lap"][df_line["driverId"] == driver],
            y=pd.to_timedelta(df_line["milliseconds"][df_line["driverId"] == driver], unit="ms")
            + pd.to_datetime("1970/01/01"),  # NEEDS TO ADD DATETIME FOR PLOTLY TO WORK
            name=f"{drivers_df['forename'][drivers_df['driverId'] == driver].values[0]}\
 {drivers_df['surname'][drivers_df['driverId'] == driver].values[0]}",
        )
        for driver in df_line["driverId"].unique()
    ]

    layout = go.Layout(
        title="Race pace",
        yaxis=dict(
            title="time",
            tickformat="%M:%S.000",
        ),
        xaxis=dict(title="lap"),
    )

    for i in range(len(data)):
        data[i]["visible"] = True if i < 5 else "legendonly"
        # data[i]["visible"] = "legendonly"
    fig = go.Figure(data=data, layout=layout)

    return fig


@app.callback(
    [
        Output(component_id="race-dropdown", component_property="options"),
        Output(component_id="race-dropdown", component_property="value"),
    ],
    [Input(component_id="years-dropdown", component_property="value")],
)
def update_races_year_dropdown(year):
    races_in_year = races_df[["raceId", "name"]][races_df["year"] == year]
    # # print(races_in_year, type(races_in_year))
    # x = [i for i in races_in_year.to_dict("records")]
    # # print(*x, sep="\n")
    races = races_in_year.to_dict("records")
    # print(races[0]["name"])
    return [{"label": i["name"], "value": i["raceId"]} for i in races], races[0]["raceId"]

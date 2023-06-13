from dashboard.index import app


import plotly.graph_objs as go
from dashboard.layout.year_tab import races_df, circuits_df
from dash.dependencies import Input, Output


# def update_graph(col_chosen):
#     fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
#     return fig


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
        title_text=f"Formula 1 races {YEAR} season",
        showlegend=False,
        width=1280,
        height=720,
        paper_bgcolor="white",
        sliders=sliders,
    )

    return fig

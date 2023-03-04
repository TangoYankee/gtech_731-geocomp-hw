import io
import json
import pandas as pd
import plotly.express as px

# https://plotly.com/python/choropleth-maps/
with io.open("data/boi_select_ages_tract_borders.geojson", encoding="utf-8") as f:
    tracts = json.load(f)

df = pd.read_csv("data/bois-ages-tract.csv", dtype={"Geography": str})

fig = px.choropleth(
    df,
    geojson=tracts,
    featureidkey="properties.Geography",
    locations="Geography",
    color="tot_pop_over_65_est",
    color_continuous_scale="viridis_r",
    labels={"tot_pop_over_65_est": "Population over 65"},
    scope="usa",
)
fig.update_geos(fitbounds="geojson")
fig.show()

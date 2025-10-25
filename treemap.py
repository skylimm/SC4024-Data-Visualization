import pandas as pd
import plotly.express as px

df = pd.read_csv("all.csv")

# data cleansing
df = df.dropna(subset=["Country", "Sport", "Medal"])

# standardize formatting
df["Country"] = df["Country"].str.strip().str.title()
df["Sport"] = df["Sport"].str.strip().str.title()
df["Medal"] = df["Medal"].str.strip().str.capitalize()

# Counting total medals per country 
country_medal_totals = (
    df.groupby("Country")
    .size()
    .reset_index(name="Total_Medals")
)

# retrieving top 10 countries
top10_countries = (
    country_medal_totals.nlargest(10, "Total_Medals")["Country"]
)

# count medals by (Country, Sport) for the treemap
medal_counts_by_sport = (
    df[df["Country"].isin(top10_countries)]
    .groupby(["Country", "Sport"])
    .size()
    .reset_index(name="Total_Medals")
)

fig = px.treemap(
    medal_counts_by_sport,
    path=["Country", "Sport"],
    values="Total_Medals",
    color="Total_Medals",
    color_continuous_scale="Blues",
    range_color=[medal_counts_by_sport["Total_Medals"].min(), medal_counts_by_sport["Total_Medals"].max()],
    title="🏅 Top 10 Countries — Olympic Dominance by Sport",
)

fig.update_traces(
    hovertemplate="<b>%{label}</b><br>Medals: %{value}<extra></extra>",
)

fig.update_layout(
    margin=dict(t=60, l=25, r=25, b=25),
    plot_bgcolor="white",
)

fig.show()
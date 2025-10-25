import pandas as pd
import plotly.express as px
import statsmodels.api as sm

df = pd.read_csv("all.csv")

# data cleansing
df = df.dropna(subset=["Country", "Medal", "GDP per Capita"])  # ensure no missing values

# computing total medals per country
medal_counts = df.groupby("Country").size().reset_index(name="Total_Medals")

gdp_data = df.groupby("Country", as_index=False).agg({
    "GDP per Capita": "mean",
    "Population": "mean"  # Add population aggregation
})

merged = pd.merge(medal_counts, gdp_data, on="Country", how="inner")

fig = px.scatter(
    merged,
    x="GDP per Capita",
    y="Total_Medals",
    size="Population",          
    color="Population",           # color gradient by population
    hover_name="Country",
    trendline="ols",              # add trendline
    size_max=60,
    log_x=True,                   
    title="Population, Wealth & Olympic Success: GDP per Capita vs Medal Count",
)

fig.update_layout(
    xaxis_title="GDP per Capita (log scale)",
    yaxis_title="Total Olympic Medals",
    plot_bgcolor="white",
    annotations=[
        dict(
            xref="paper", yref="paper",
            x=0.9, y=0.55,
            showarrow=False,
            text="Each bubble represents a country,<br>Bubble size reflects population size.",
            font=dict(size=14, color="gray"),
            align='left'
        )
    ]
)

fig.show()
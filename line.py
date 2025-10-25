import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("all.csv")

# data cleansing 
df = df.dropna(subset=["Year", "Gender", "Medal"])
df["Year"] = df["Year"].astype(int)
df["Gender"] = df["Gender"].str.strip().str.capitalize()

# Before 1992, Summer and Winter Olympics happened in the same year (e.g., 1988).
# After 1992, the Winter Games shifted to occur two years after the Summer Games (e.g., 1994).
# So I Map Winter Olympic years (1994, 1998, 2002, 2006, …) → back to the previous Summer year (1992, 1996, 2000, 2004, …)
# And keep everything else unchanged
def align_year(year):
    if year > 1992 and (year - 2) % 4 == 0:
        return year - 2
    return year

df["Aligned_Year"] = df["Year"].apply(align_year)

# group by aligned year & gender
gender_year = (
    df.groupby(["Aligned_Year", "Gender"])
    .size()
    .reset_index(name="Medal_Count")
    .sort_values("Aligned_Year")
)

fig = px.line(
    gender_year,
    x="Aligned_Year",
    y="Medal_Count",
    color="Gender",
    markers=True,
)

fig.update_layout(showlegend=False)

# adding text labels ("Men", "Women") at the end of each line
for gender in gender_year["Gender"].unique():
    last_point = gender_year[gender_year["Gender"] == gender].iloc[-1]
    fig.add_annotation(
        x=last_point["Aligned_Year"],
        y=last_point["Medal_Count"],
        text=gender,
        showarrow=False,
        font=dict(size=14, color="black", family="Arial"),
        xanchor="left",
        yanchor="middle",
        xshift=15 
    )

fig.update_layout(
    title="🏅 Olympic Medal Count by Gender Over Time",
    xaxis_title="Year",
    yaxis_title="Total Medals Won",
    plot_bgcolor="white",
    hovermode="x unified",
    font=dict(size=14),
    margin=dict(r=80) 
)

fig.show()

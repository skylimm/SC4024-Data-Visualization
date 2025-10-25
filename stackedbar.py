import pandas as pd
import plotly.express as px

df = pd.read_csv("all.csv")
df = df.dropna(subset=["Country", "Medal"])
df["Medal"] = df["Medal"].str.strip().str.capitalize()

medal_counts = df.groupby(["Country", "Medal"]).size().reset_index(name="Count")

total_medals = medal_counts.groupby("Country")["Count"].sum().reset_index(name="Total_Medals")

top10_countries = total_medals.nlargest(5, "Total_Medals")["Country"]

top10_data = medal_counts[medal_counts["Country"].isin(top10_countries)]

medal_order = ["Bronze", "Silver", "Gold"]
top10_data["Medal"] = pd.Categorical(top10_data["Medal"], categories=medal_order, ordered=True)

fig = px.bar(
    top10_data,
    x="Country",
    y="Count",
    color="Medal",
    category_orders={"Medal": medal_order},
    color_discrete_sequence=["#CD7F32", "#C0C0C0", "#FFD700"],  # Bronze, Silver, Gold
    title="🏆 Top 5 Nations — Olympic Medal Composition",
    text="Count"
)

fig.update_layout(
    xaxis_title="Country",
    yaxis_title="Number of Medals",
    plot_bgcolor="white",
    barmode="stack",
)
fig.show()

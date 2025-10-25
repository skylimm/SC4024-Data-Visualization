import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("all.csv")
df = df.dropna(subset=["Season", "Gender", "Medal"])
df["Gender"] = df["Gender"].str.strip().str.capitalize()
df["Season"] = df["Season"].str.strip().str.capitalize()

medal_counts = (
    df.groupby(["Season", "Gender", "Year"])
    .size()
    .reset_index(name="Medal_Count")
)

sns.set_theme(style="whitegrid", font_scale=1.15)

palette_teal_gold = {
    "Men": "#1B929D",    # Deep teal
    "Women": "#E56B70"   # Muted gold
}

selected_palette = palette_teal_gold  

plt.figure(figsize=(10, 7))  

ax = sns.violinplot(
    data=medal_counts,
    x="Season",
    y="Medal_Count",
    hue="Gender",
    split=True,
    inner="quart",
    linewidth=1.2,
    fill=True,
    palette=selected_palette,
    saturation=0.8
)

plt.title("Distribution of Medal Counts by Gender Across Olympic Seasons",
          fontsize=16, weight="bold", pad=25)
plt.xlabel("Olympic Season", fontsize=13, weight="semibold")
plt.ylabel("Number of Medals", fontsize=13, weight="semibold")

plt.legend(title="Gender", loc="upper right", frameon=True, 
           fancybox=True, shadow=True, framealpha=0.9)

# caption
caption_text = "Note: The slight negative tails are smoothing artifacts from the violin plot kernel density estimation, not negative medal counts."
plt.figtext(
    0.5, 0.05,  
    caption_text,
    ha="center", 
    fontsize=11, 
    color="#555555",
    style="italic",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#f8f9fa", 
              edgecolor="#e9ecef", alpha=0.8)  
)

plt.subplots_adjust(bottom=0.15)  
plt.tight_layout(rect=[0, 0.05, 1, 0.95])  


plt.show()
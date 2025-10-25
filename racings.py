# this file is used to generate output_file_for_flourish.csv which is being used in flourish to create the racing bar chart
# https://flourish-user-preview.com/api/canva/embed/visualisation/25792358/md7FpoOMksnWeSqJSIsnPCV8wr7KaHK8EefvvHZ9WKEvqMgMNnT1r_RUaGLk1glA/
import pandas as pd
import pycountry

df = pd.read_csv("all.csv")
df = df.dropna(subset=["Country", "Year", "Medal"])
df["Country"] = df["Country"].str.strip().str.title()
df["Year"] = df["Year"].astype(int)

medals_by_year = (
    df.groupby(["Year", "Country"])
    .size()
    .reset_index(name="Total_Medals")
    .sort_values(["Year", "Total_Medals"], ascending=[True, False])
)

# Pivot: make each year a column (wide format)
pivoted = medals_by_year.pivot_table(
    index="Country",
    columns="Year",
    values="Total_Medals",
    fill_value=0
).reset_index()

# adding flag image URLs
def get_country_code(name):
    try:
        return pycountry.countries.lookup(name).alpha_2.lower()
    except:
        return None

pivoted["country_code"] = pivoted["Country"].apply(get_country_code)
pivoted["image_url"] = pivoted["country_code"].apply(
    lambda code: f"https://flagcdn.com/w40/{code}.png" if pd.notna(code) else ""
)

pivoted = pivoted.drop(columns=["country_code"])
pivoted.to_csv("output_file_for_flourish.csv", index=False)

print(pivoted.head())

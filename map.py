import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("all.csv")
df = df.dropna(subset=['Year', 'Country', 'Medal'])

df['Country'] = df['Country'].str.strip()
df = df[df['Country'] != '#N/A']  
df['Year'] = df['Year'].astype(int)

# Before 1992, Summer and Winter Olympics happened in the same year (e.g., 1988).
# After 1992, the Winter Games shifted to occur two years after the Summer Games (e.g., 1994).
# So I Map Winter Olympic years (1994, 1998, 2002, 2006, …) → back to the previous Summer year (1992, 1996, 2000, 2004, …)
# And keep everything else unchanged

def align_year(year):
    # After 1992, shift Winter Games (e.g., 1994, 1998...) back 2 years
    if year > 1992 and (year - 2) % 4 == 0:
        return year - 2
    return year

df['Aligned_Year'] = df['Year'].apply(align_year)

medal_counts = df.groupby(['Aligned_Year', 'Country']).size().reset_index(name='Total_Medals')

# Merging ISO3 codes for Country column
iso_mapping = df[['Country', 'ISO3']].drop_duplicates().dropna()
medal_counts = medal_counts.merge(iso_mapping, on='Country', how='left')
medal_counts = medal_counts.dropna(subset=['ISO3'])

# sort years for animation
years = sorted(medal_counts['Aligned_Year'].unique())
print(f"Aligned years in dataset: {years}")
print(f"Countries with medals: {medal_counts['Country'].nunique()}")

# building animation frames
frames = []
for year in years:
    year_data = medal_counts[medal_counts['Aligned_Year'] == year]
    frame = go.Frame(
        data=[
            go.Choropleth(
                locations=year_data['ISO3'],
                z=year_data['Total_Medals'],
                text=year_data['Country'] + ': ' + year_data['Total_Medals'].astype(str) + ' medals',
                hoverinfo='text+z',
                colorscale='Viridis',
                colorbar_title='Total Medals',
                zmin=0,
                zmax=medal_counts['Total_Medals'].max()
            )
        ],
        name=str(year)
    )
    frames.append(frame)


init_data = medal_counts[medal_counts['Aligned_Year'] == years[0]]

fig = go.Figure(
    data=[
        go.Choropleth(
            locations=init_data['ISO3'],
            z=init_data['Total_Medals'],
            text=init_data['Country'] + ': ' + init_data['Total_Medals'].astype(str) + ' medals',
            hoverinfo='text+z',
            colorscale='Viridis',
            colorbar_title='Total Medals',
            zmin=0,
            zmax=medal_counts['Total_Medals'].max()
        )
    ],
    frames=frames
)

fig.update_layout(
    title_text='Olympic Medal Distribution by Country Over the Years',
    title_x=0.5,
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='natural earth',
        landcolor='lightgray',
        coastlinecolor='white'
    ),
    updatemenus=[{
        'type': 'buttons',
        'showactive': False,
        'y': 1.1,
        'x': 0.1,
        'xanchor': 'left',
        'yanchor': 'top',
        'buttons': [{
            'label': 'Play',
            'method': 'animate',
            'args': [None, {
                'frame': {'duration': 1000, 'redraw': True},
                'transition': {'duration': 500},
                'fromcurrent': True
            }]
        }]
    }]
)

# timeline slider
fig.update_layout(
    sliders=[{
        'active': 0,
        'yanchor': 'top',
        'xanchor': 'left',
        'currentvalue': {
            'font': {'size': 16},
            'prefix': 'Year: ',
            'visible': True,
            'xanchor': 'right'
        },
        'transition': {'duration': 500},
        'pad': {'b': 10, 't': 50},
        'len': 0.9,
        'x': 0.1,
        'y': 0,
        'steps': [{
            'args': [
                [str(year)],
                {'frame': {'duration': 500, 'redraw': True}, 'mode': 'immediate'}
            ],
            'label': str(year),
            'method': 'animate'
        } for year in years]
    }]
)

fig.update_layout(
    font=dict(size=12),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

fig.show()

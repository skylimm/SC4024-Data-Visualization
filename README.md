# 🏅 Olympic Data Visualization — *How Wealth, Gender, and Time Shape Olympic Success*

## 🎯 Project Overview
This project explores how **wealth, gender, and time** have influenced Olympic success from **1896 to 2014**.  
Using data from *The Guardian* (via Kaggle), the analysis visualizes patterns in medal distribution, global expansion, and gender inclusiveness across more than a century of Olympic history.  

The project transforms raw data into compelling visuals and narratives to reveal:
- How **GDP per capita** and **population size** affect medal performance.  
- The **historical dominance** and later **global diversification** of medal-winning countries.  
- The **evolution of gender participation and equality** over time.  
- How **top nations specialize** in different sports based on tradition and strategy.  


## 📊 Dataset
**Source:** [The Guardian Olympic Games Dataset (Kaggle)](https://www.kaggle.com/datasets/the-guardian/olympic-games)  
**Coverage:** 1896–2014 (Summer and Winter Games)  


## ⚙️ Running the files

```
git clone https://github.com/skylimm/SC4024-Data-Visualization.git
```
```
cd <repo-name>
```
```
pip install -r requirements.txt
```

Each script generates a specific visualization.
Run any file directly with Python, for example:
```
python bubble.py
```

### Visualizations Overview

| Script | Visualization Type | Description |
|--------|--------------------|-------------|
| `racings.py` | 🏁 Racing Bar Chart | Animated chart showing top medal-winning countries from 1896–2014, illustrating shifting dominance over time. |
| `bubble.py` | 💰 Bubble Chart | Visualizes the relationship between GDP per capita, population, and total medals won — highlighting economic influence on Olympic success. |
| `map.py` | 🗺️ Choropleth Map | Displays the global expansion of Olympic medal-winning nations, showing how participation and success have spread worldwide. |
| `stackedbar.py` | 🥇 Stacked Bar Chart | Breaks down total medals by type (Gold, Silver, Bronze) for the top 5 countries, showing overall performance balance. |
| `treemap.py` | 🌳 Treemap | Highlights sport specialization among top 10 countries — the size and color of each block represent medals won per sport. |
| `violin plot.py` | 🎻 Violin Plot | Shows medal distribution by gender, emphasizing changes in female participation and narrowing gender gaps over time. |
| `line.py` | 📈 Line Chart | Depicts long-term trends in total medals awarded, reflecting the growth of the Olympic Games and evolving participation. |

#### 📺 **Please watch the full visualization walkthrough on YouTube** for a detailed explanation of each chart and storytelling sequence:  
👉 https://youtu.be/0dLtS6rzyDk

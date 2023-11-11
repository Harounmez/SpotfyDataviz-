import pandas as pd
import panel as pn
import hvplot.pandas

# Step 1: Read your dataset (replace 'your_dataset.csv' with your dataset file)
df = pd.read_csv("dataset.csv")

# Step 2: Calculate the average speechiness for each genre
avg_speechiness_by_genre = df.groupby('track_genre')['speechiness'].mean().sort_values(ascending=False)

# Step 3: Create a bar plot for each track_genre using hvplot
def bar_plot(data):
    return data.hvplot.bar(y='speechiness', rot=45, xlabel='Genre', ylabel='Average Speechiness', title='Average Speechiness')

# Create a Panel app for each bar plot
panel_app = pn.Tabs(
    *[(genre, bar_plot(df[df['track_genre'] == genre])) for genre in avg_speechiness_by_genre.index],
)

# Serve the Panel app
panel_app.servable()

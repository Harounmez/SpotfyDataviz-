import pandas as pd
import plotly.express as px
import panel as pn
pn.extension('plotly')

from dataloadre import df

class PieChart:
    def __init__(self, data):
        self.data = data
        self.layout = self._create_dashboard()

    def _create_dashboard(self):
        genre_popularity = self.data.groupby('track_genre')['popularity'].mean().reset_index()
        sorted_genre_popularity = genre_popularity.sort_values(by='popularity', ascending=False)
        top_10_genres = sorted_genre_popularity.head(10)

        fig = px.pie(top_10_genres, names='track_genre', values='popularity', hole=0.3, title='Les Genres les plus populaires')
        fig.update_traces(textinfo='percent+label')

        donut_chart = pn.pane.Plotly(fig, sizing_mode="scale_both")  # Use sizing_mode to control layout

        return donut_chart


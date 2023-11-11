import pandas as pd
import matplotlib.pyplot as plt
import panel as pn

pn.extension(raw_css=[open('styles.css').read()])  # Load the CSS file

class TopGenresByArtist:
    def __init__(self, data, num_top_artists=20):
        self.data = data
        self.num_top_artists = num_top_artists
        self.layout = self._create_dashboard()

    def _create_dashboard(self):
        # Step 1: Filter the dataset for the top N artists
        top_artists = self.data['artists'].value_counts().head(self.num_top_artists).index.tolist()

        # Create a dropdown widget for artist selection
        artist_select = pn.widgets.Select(name='Select Artist', options=top_artists, sizing_mode="stretch_width")

        # Initialize the Matplotlib figure and pane
        fig, ax = plt.subplots(figsize=(8, 8))
        chart_pane = pn.pane.Matplotlib(fig, height=600, width=600, sizing_mode="stretch_width")
        chart_pane.css_classes = ['center-chart']  # Apply the CSS class to center the chart

        # Create a function to update the chart based on the selected artist
        def update_chart(event):
            selected_artist = artist_select.value
            filtered_df = self.data[self.data['artists'] == selected_artist]
            genre_counts = filtered_df['track_genre'].value_counts()

            ax.clear()  # Clear the previous plot
            ax.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140)
            ax.set_title(f"Track Genres of {selected_artist}")
            chart_pane.object = fig  # Update the chart pane

        # Bind the function to the 'value' parameter of the artist_select widget
        artist_select.param.watch(update_chart, 'value')

        # Initialize the Panel app
        panel_app = pn.Column("## Track Genres of Top Artists", artist_select, chart_pane, sizing_mode="stretch_width")

        return panel_app


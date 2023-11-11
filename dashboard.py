import panel as pn
from bokeh.models import CustomJS
import pandas as pd

from dataloadre import df
from piechart_g_p import PieChart 
from piechart_g_a import TopGenresByArtist
from piechart_a_p import PieChart1
from heatmap import HeatmapChart
from countplot import CountPlots
from plots import ScatterPlot
pn.extension('plotly')

# Load your data (assuming df is defined)


Pie_chart = PieChart(df)
Pie_chart2 = TopGenresByArtist(df)
Piechart3 = PieChart1(df)
heat_map = HeatmapChart(df)

variables = ["time_signature", "mode", "explicit"]



count_plots = CountPlots(df, variables)

subsample = df.sample(n=500, random_state=42) 
# Select only numerical columns
numerical_columns = subsample.select_dtypes(include='number').columns.tolist()
 
# Create an instance of the ScatterPlot class
scatter_plot = ScatterPlot(subsample, title="Sample Scatter Plot")
# Set options for the Select widgets to include only numerical columns
scatter_plot.x_selector.options = numerical_columns
scatter_plot.y_selector.options = numerical_columns

# Create your main layouts
main_layout1 = pn.Column(
    heat_map.layout,
    scatter_plot.layout,
    sizing_mode="stretch_width",  # Adjust the sizing mode as needed
    align="center",  # Align content in the middle
)
main_layout3 = pn.Column(
    pn.Row(Pie_chart2.layout, align="center"),
    pn.Row(Piechart3.layout, align="center"),
    sizing_mode="stretch_width",
    align="center",  # Align content in the middle

)

main_layout2 = pn.Column(
    pn.Row(Pie_chart.layout, align="center"), 
)

main_layout4 = pn.Column(
    count_plots.layout,
    sizing_mode="stretch_width",  # Adjust the sizing mode as needed
    align="center",
    
)
template = pn.template.FastListTemplate(
    site ="Spotify Dashboard",
    title='<h1 style="text-align:center;">SPOTIFY Dashboard Application for Data Visualization</h1>',  # Center-align the title
    header_color="#1DB954",
    header_background="#000000",  # Set the background color to black
    collapsed_sidebar=False,
    sidebar_width=330,
    corner_radius=5,
    main=[main_layout3, main_layout1, main_layout2, main_layout4], 
    logo="spotifylogo.png"
)

tabs = pn.Tabs(
    ("Explanatory Data Analysis for Relations between Numerical Data", main_layout1),
    ("Pie Charts To visualize Artist Genres", main_layout3),
    ("Pie Charts To visualize Track Genres", main_layout2),
    ("Visualization of Binary Variables", main_layout4),
    tabs_location="above",
    dynamic=True,
    width=2000,
    css_classes=["dashboard", "custom-tabs"]  # Add a custom class for styling
)

# Add custom CSS for the tab titles
pn.config.raw_css.append(
    """
    .custom-tabs .bk-root .bk-tab {
        font-size: 20px;  # Adjust the font size as needed
        font-family: Arial, sans-serif;
        font-weight: bold;
    }
    """
)




tabs

template.main[:] = [tabs]

# Display the template
template.servable()
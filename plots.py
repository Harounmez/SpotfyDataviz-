import pandas as pd
import panel as pn
import hvplot.pandas as hvplot  # Ensure you have hvplot installed (pip install hvplot)
from dataloadre import df
class ScatterPlot:
    def __init__(self, data, title="Scatter Plot"):
        self.data = data
        self.title = title
        self.x_selector = pn.widgets.Select(name='Select X Variable')
        self.y_selector = pn.widgets.Select(name='Select Y Variable')
        self.plot_pane = pn.pane.HoloViews(sizing_mode="scale_both", min_height=500)
        self.layout = self.create_layout()

        # Bind the update function to the Select widgets
        self.x_selector.param.watch(self.update_plot, 'value')
        self.y_selector.param.watch(self.update_plot, 'value')

        # Create an initial scatter plot
        self.update_plot()

    def create_layout(self):
        layout = pn.Column(
            f"## {self.title}",
            self.x_selector,
            self.y_selector,
            pn.Row(self.plot_pane, align="center", sizing_mode="scale_both"),
        )
        return layout

    def create_plot(self, x_variable, y_variable):
        scatter = self.data.hvplot.scatter(x=x_variable, y=y_variable, width=800, height=600)
        return scatter

    def update_plot(self, event=None):
        x_variable = self.x_selector.value
        y_variable = self.y_selector.value

        if x_variable is not None and y_variable is not None:
            scatter_figure = self.create_plot(x_variable, y_variable)
            self.plot_pane.object = scatter_figure


import pandas as pd
import plotly.express as px
import panel as pn
from dataloadre import df

class ScatterPlot:
    def __init__(self, data, title="Scatter Plot"):
        self.data = data
        self.title = title
        self.x_selector = pn.widgets.Select(name='Select X Variable', options=[])
        self.y_selector = pn.widgets.Select(name='Select Y Variable', options=[])
        self.layout = self.create_layout()

        # Bind the update function to the Select widgets
        self.x_selector.param.watch(self.update_plot, 'value')
        self.y_selector.param.watch(self.update_plot, 'value')

        # Set default values for Select widgets
        self.set_default_values()

        # Create an initial scatter plot
        self.update_plot()

    def set_default_values(self):
        # Get the list of numerical variables
        numerical_variables = self.data.select_dtypes(include='number').columns.tolist()

        # Set options for the Select widgets
        self.x_selector.options = numerical_variables
        self.y_selector.options = numerical_variables

        # Set default values or choose some initial options
        self.x_selector.value = numerical_variables[0] if numerical_variables else None
        self.y_selector.value = numerical_variables[1] if len(numerical_variables) > 1 else None

    def create_layout(self):
        layout = pn.Column(
            "## Scatter Plot Example",
            self.x_selector,
            self.y_selector,
        )
        return layout

    def create_plot(self, x_variable, y_variable):
        scatter = px.scatter(
            self.data,
            x=x_variable,
            y=y_variable,
            title=self.title,
        )
        return scatter

    def update_plot(self, event=None):
        x_variable = self.x_selector.value
        y_variable = self.y_selector.value

        # Check if selected columns exist in the DataFrame
        if x_variable not in self.data.columns or y_variable not in self.data.columns:
            print(f"Error: {x_variable} or {y_variable} not found in DataFrame columns.")
            return

        # Check if selected columns have numeric data types
        if not pd.api.types.is_numeric_dtype(self.data[x_variable]) or not pd.api.types.is_numeric_dtype(self.data[y_variable]):
            print(f"Error: {x_variable} and {y_variable} must be numeric columns.")
            return

        scatter_figure = self.create_plot(x_variable, y_variable)
        scatter_pane = pn.pane.Plotly(scatter_figure)
        self.layout[-1] = scatter_pane  # Replace the last element to update the plot

# Sample dataset
data = df  # Use your dataset

# Create an instance of the ScatterPlot class
scatter_plot = ScatterPlot(data, title="Scatter Plot Example")

# Display the Panel app
scatter_plot.layout.servable()

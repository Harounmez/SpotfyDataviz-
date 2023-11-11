import pandas as pd
import panel as pn
import seaborn as sns
import matplotlib.pyplot as plt

class HeatmapChart:
    def __init__(self, data):
        self.data = data  # Fix the variable name
        self.layout = self._create_dashboard()  # Rename to layout

    def _create_dashboard(self):
        # Step 2: Select only the numerical columns
        numerical_columns = self.data.select_dtypes(include=['number'])

        # Step 3: Calculate the correlation matrix
        corr_matrix = numerical_columns.corr()

        # Step 4: Create a heatmap using Seaborn
        fig, ax = plt.subplots(figsize=(8, 8))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)

        # Step 5: Create a Panel app to display the heatmap
        heatmap_pane = pn.pane.Matplotlib(fig, tight=True)
        panel_app = pn.Column("## Correlation Heatmap", heatmap_pane)

        return panel_app

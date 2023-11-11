import seaborn as sns
import matplotlib.pyplot as plt
import panel as pn
import param
from dataloadre import df


class CountPlots(param.Parameterized):
  def __init__(self, dataset, variables=None):
    super().__init__()
    self.dataset = dataset
    self.variables = variables or []
    self.layout=self.show_plots()
  
  def create_count_plots(self):
    fig, axes = plt.subplots(1, len(self.variables), figsize=(8, 4))
    for ax, var in zip(axes, self.variables):
      sns.countplot(data=self.dataset, x=var, ax=ax)
      ax.set_title(var)
    plt.tight_layout()
    return fig

  def show_plots(self):
    return self.create_count_plots()




from bokeh.charts import Bar
from bokeh.embed import components
from bokeh.models import Range1d
from bokeh.charts.attributes import CatAttr
import bokeh.plotting as plt

def make_bar_plot(labels, values):
    data = {'labels': labels, 'values': values}
    bar = Bar(data, values='values', label=CatAttr(columns=['labels'], sort=False), legend=False, agg='mean', bar_width=0.6, plot_width=500, plot_height=350)
    bar.y_range = Range1d(0.0, 1.0)
    script, div = components(bar)
    return script, div

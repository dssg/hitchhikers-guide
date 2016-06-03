# Data visualization with Python

There are many libraries to do dataviz using Python, here you'll find some alternative and their use cases. Take into account that there's no *one fits all* solution, choose a tool depending on what you want to do.

## matplotlib

matplotlib is the core library for creating static plots in Python. You can create pretty much everything using it. Since matplotlib is intended to offer great flexibility, understanding the low-level API takes time some libraries such as Seaborn or sklearn-evaluation are built on top of matplotlib to provide a simpler API for domain-specific plots.

**Use matplotlib if...**

*   You want to create a custom plot
*   Need complete control over the elements to plot

**Resources**

*   [matplotlib on Github](https://github.com/matplotlib/matplotlib)
*   [Gallery](http://matplotlib.org/gallery.html)
*   [Examples](matplotlib.ipynb)

## Pandas

What? Pandas? I thought it was a library for Data Analysis. Well, yes but it also has a nice API to make plots (using matplotlib under the hood) from your DataFrames. If you are already using pandas, consider using its plotting API instead of using matplotlib directly.

**Use pandas for visualization if...**

*   You are already using pandas for analysis (duh!)

**Resources** 

*   [Pandas Visualization documentation](http://pandas.pydata.org/pandas-docs/stable/visualization.html)
*   [Examples](pandas.ipynb)

## Seaborn

Seaborn provides a much simpler API than matplotlib to make statistical plots, it also has much nicer default settings so you get pretty plots without having to manually configure colors, axis, etc. Seaborn provides functions for box plots, distributions, heat maps, cluster maps, time series among others.

**Use Seaborn if...**

-   You are plotting statistical data
-   Want to have nice default settings

**Resources**

-   [Seaborn on Github](https://github.com/mwaskom/seaborn)
-   [Gallery](http://stanford.edu/~mwaskom/software/seaborn/examples/index.html)
-   [Examples](seaborn.ipynb)

## Folium

There are many options to plot maps in Python but we've found that the best option right now is Folium, even though it has a limited set of features, plotting a map requires just a couple of lines.

**Use Folium if...**

-   Need a straightforward way of plotting simple maps (the API is quite limited and not well-documented)

**Resources**

-   [Folium on Github](https://github.com/python-visualization/folium)
-   [Gallery](http://nbviewer.jupyter.org/github/python-visualization/folium/tree/master/examples/)
-   [Examples](http://htmlpreview.github.io/?https://github.com/dssg/hitchhikers-guide/blob/master/tech-tutorials/dataviz/folium.html)

## Bokeh 

If you are building a dashboard which requires interaction with the user, consider using Bokeh.

**Use Bokeh if...**

-   You want to create interactive plots

**Resources**

-   [Bokeh on Github](https://github.com/bokeh/bokeh)
-   [Gallery](http://bokeh.pydata.org/en/latest/docs/gallery.html)
-   [Examples](bokeh.ipynb)



## sklearn-evaluation

If you want an easy way to create standard plots to evaluate Machine Learning models, sklearn-evaluation is a good option. The API is limited to classifiers, but it will save you a lot of time. 

**Use sklearn-evaluation if...**

-   You want to evaluate a Machine Learning model through visualization (e.g. ROC, Precision-Recall)

**Resources**

-   [sklearn-evaluation on Github](https://github.com/edublancas/sklearn-evaluation)
-   [Examples](sklearn-evaluation.ipynb)


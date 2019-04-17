#!/usr/bin/env python
"""Hacky script to generate HTML plots of feature distributions."""

import pandas as pd
import numpy as np
import argparse
import os
from bokeh.plotting import figure, show
from bokeh.palettes import Set1
from bokeh.io import save
from bokeh.layouts import gridplot
from bokeh.resources import CDN
from scipy.stats import ks_2samp


def fetch_and_split_data(infile_name, cutoff):
    """
    Reads data from a CSV file, performs some sanity checks, and then
    returns to dataframes which have been split based on the 'score' column
    at the prefined cutoff ratio. If predictions are rank-tied, the high-risk
    group might be larger than specified by cutoff.

    Args:
        infile_name (str): File name of a CSV file. This function expects
                           the CSV to contain at 'score' column.
        cutoff (float): Ratio of entities that should be considered
                        high-risk. Needs to be in [0,1].
    Returns (pd.DataFrame, pd.DataFrame): The input data, split by score.
    """

    if not infile_name:
        raise ValueError("Input CSV file is required.")

    if cutoff < 0. or cutoff > 1.0:
        raise ValueError("cutoff must be in [0, 1].")

    # fetch the data
    df = pd.read_csv(infile_name)

    # clean up some columns that aren't features or the prediction score
    if 'entity_id' in df.columns:
        del df['entity_id']

    if 'true_label' in df.columns:
        del df['true_label']

    if not 'score' in df.columns:
        raise ValueError('The data must contain a "score" columns.')

    df = df.sort_values(by='score', ascending=False)
    
    ranks = df.score.rank(method='min', ascending=False)
    cutoff_idx = int(pd.np.floor(cutoff*len(df))) 

    del df['score']

    return df[ranks<=cutoff_idx], df[ranks>cutoff_idx]


def sort_features(df1, df2):
    """
    Takes two dataframes, and calculates a KS-Test between each 
    two columns that appear in both dataframes. Returns a list of
    column names, sorted by p-value in ascending order, and a list
    of corresponding p-values.

    Args:
        df1 (pd.DataFrame): Dataframe of feature columns for 'sample 1'
        df2 (pd.DataFrame): Dataframe of feature columns for 'sample 2'
    Returns ([str], [float]): Lists of column names and p-values.
    """

    common_cols = set.intersection(*[set(df.columns) for df in [df1, df2]])

    if len(common_cols) == 0:
        raise ValueError("The dataframes have no columns in common.")

    # calculate a KS-test for each feature column
    d = []
    p_vals = []
    for c in common_cols:
        this_d, this_p = ks_2samp(df1[c], df2[c])
        d.append(this_d)
        p_vals.append(this_p)

    # sort by p-value
    pc = list(zip(p_vals, common_cols))
    pc.sort()
    p_vals, common_cols = zip(*pc)

    # return sorted list of feature names and p-values
    return list(common_cols), list(p_vals)


def plot_feature_histograms(df_list, names=[], nbins=50, colors=[]):
    """
    Takes a list of dataframes with equal columns. For each column, 
    from that list, creates a histogram that contrasts the distribution of 
    that column's values between dataframes.
    Note: The returned plots are returned in the same order as they appear 
    in df_list[0].
    Args:
        df_list: list of dataframes
        names: list of dataframe names
        nbins: the number of bins in the histograms
        colors: list of colors to use; uses a standard palette by default
    Returns:
        List of bokeh.figures
    """

    if names and len(names)!=len(df_list):
        raise ValueError("The number of names and dataframes must match.")

    if colors and len(colors)!=len(df_list):
        raise ValueError("The number of colors and dataframes must match.")

    if not names:
        names = ['dataframe_%.02d'%idx for idx in range(len(df_list))]

    if not colors:
        if len(df_list) > len(Set1[9]):
            raise ValueError("You must specify colors for this many dataframes.")
        colors = Set1[9][:len(df_list)]

    for df in df_list[1:]:
        if not all(df.columns == df_list[0].columns):
            raise ValueError("Not all dataframes have the same columns.")

    # all dataframes have the same columns; make strings
    # note: order is as in df_list[0]
    common_cols = map(str, df_list[0].columns)

    # bokeh is picky with column names
    for df in df_list:
        df.columns = map(str, df.columns)

    # now we can plot each column, grouped by the dataframe name
    res = []
    for col in common_cols:

        # get the bin sizes
        all_values = pd.concat([df[col] for df in df_list], ignore_index=True)
        _, all_edges = np.histogram(all_values, bins=nbins)

        # make a figure
        p = figure(title="Distribution of %s"%col, tools=["save","zoom_in",
            "zoom_out", "box_zoom", "reset", "pan"],
            background_fill_color="#ffffff")

        # add a histogram plot per dataframe
        for idx, df in enumerate(df_list):
            hist, edges = np.histogram(df[col], density=True, bins=all_edges)
            p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
                   fill_color=colors[idx], line_color=colors[idx], 
                   alpha=0.3, legend=names[idx])

        p.legend.location = 'top_right'
        p.xaxis.axis_label = col
        p.yaxis.axis_label = 'density'
        res.append(p)

    return res


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--infile",
                        help=("Path to the CSV file which contains "
                              "the predictions and features."),
                        type=str)

    parser.add_argument("-o", "--outfile",
                        help=("Path to the HTML file which contains "
                              "the histograms. Defaults to "
                              "feature_distributions.html."),
                        type=str, default="feature_distributions.html")

    parser.add_argument("-nf", "--n_features", type=int, default=21,
                        help=("Number of features to plot."))

    parser.add_argument("-c", "--cutoff", type=float, default=0.1,
                        help=("The ratio of predictions that will be considered "
                              "'positive' (high-risk)."))

    parser.add_argument("-nc", "--n_cols", type=int, default=3,
                        help=("Number of plotting columns in the HTML file." 
                              "Defaults to 3."))

    args = parser.parse_args()

    if args.n_features < 1:
        raise ValueError("Cannot plot less than 1 feature.")

    if args.n_cols < 1:
        raise ValueError("Cannot arrange plots in less than 1 columns.")

    df1, df2 = fetch_and_split_data(infile_name=args.infile, cutoff=args.cutoff)

    features, pvals = sort_features(df1, df2)

    # apply the sorting to our dataframes
    df1 = df1[features[:args.n_features]]
    df2 = df2[features[:args.n_features]]

    plots = plot_feature_histograms(
                    df_list=[df1,df2],
                    names=['top_%d_predictions'%len(df1), 
                           'bottom_%d_predictions'%len(df2)],
                    nbins=50,
                    colors=["red", "green"])

    # finally, save the HTML       
    save(gridplot(*plots, ncols=int(args.n_cols), plot_width=600, plot_height=400, 
        toolbar_location='above'), str(args.outfile), resources=CDN, 
        title='feature_densities_%s'%os.path.splitext(str(args.infile))[0])


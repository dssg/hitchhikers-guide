from itertools import product
import multiprocessing as mp
import random
import csv
import timeit
import math

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


def precision_at_abs(labels, predictions_proba):
    cutoff_index = 100

    random.seed(15)
    predictions_proba_sorted, labels_sorted = zip(*sorted(
        zip(predictions_proba, labels),
        key=lambda pair: (pair[0], random.random()), reverse=True)
    )

    test_predictions_binary = [
        1 if x < cutoff_index else 0
        for x in range(len(predictions_proba_sorted))
    ]

    return metrics.precision_score(labels_sorted, test_predictions_binary)

def standard_cv_classification(validation_year, model, fold, queue, indices):
    start_time = timeit.default_timer()
    try:
        complete_data = data[data.SENTENCE_END_YEAR <= validation_year]

        # prep validation data
        validation_df = complete_data.iloc[indices[validation_year]['test'][fold]]
        validation_X = validation_df[X_cols]
        validation_y = validation_df[y_cols]

        # prep training data
        training_df = complete_data.iloc[indices[validation_year]['train'][fold]]
        training_X = training_df[X_cols]
        training_y = training_df[y_cols]

        # fit the model
        clf = clfs[model]
        clf.fit(training_X, training_y)
        validation_precision = precision_at_abs(validation_y, clf.predict(validation_X))

        # return the results
        queue.put([validation_year, model, fold, validation_precision, round(timeit.default_timer() - start_time, 2)])

    except:
        print(validation_year, model, fold, " failed")
        pass

def temporal_cv_classification(validation_year, model, queue):
    start_time = timeit.default_timer()
    try:
        # prep validation data
        validation_df = data[data.SENTENCE_END_YEAR == validation_year]
        validation_X = validation_df[X_cols]
        validation_y = validation_df[y_cols]

        # prep training data
        training_df = data[data.SENTENCE_END_YEAR <= validation_year - 4]
        training_X = training_df[X_cols]
        training_y = training_df[y_cols]

        # fit the model
        clf = clfs[model]
        clf.fit(training_X, training_y)
        validation_precision = precision_at_abs(validation_y, clf.predict(validation_X))

        # return the results
        queue.put([validation_year, model, validation_precision, round(timeit.default_timer() - start_time, 2)])

    except:
        print(validation_year, model, " failed")
        pass

def Writer(dest_filename, queue, stop_token, total_len):
    print(total_len, ' jobs')
    i = 0

    with open(dest_filename, 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        while True:
            line = queue.get()
            if line == stop_token:
                return
            writer.writerow(line)
            i += 1
            if i % 10 == 0:
                csv_file.flush()
                print(round(i/total_len * 100, 1), " %")

if __name__ == "__main__":
    data = pd.read_pickle("recid_data.pickle")

    X_cols = data.columns.difference(['RECITIVATED', 'INMATE_DOC_NUMBER', 'SENTENCE_END', 'SENTENCE_START'])
    y_cols = 'RECITIVATED'

    print(data.dtypes)

    clfs = {
        'rf1': RandomForestClassifier(n_estimators=500, n_jobs=1, max_depth=30, max_features='log2', min_samples_split=10),
        'rf2': RandomForestClassifier(n_estimators=700, n_jobs=1, max_depth=20, max_features='log2', min_samples_split=10),
        'extra1': ExtraTreesClassifier(n_estimators=200, n_jobs=1, criterion='gini', max_depth=50, max_features='log2'),
        'extra2': ExtraTreesClassifier(n_estimators=400, n_jobs=1, criterion='gini', max_depth=30, max_features='log2'),
        'logistic1': LogisticRegression(penalty='l1', C=0.001, solver='saga', max_iter=1000),
        'logistic2': LogisticRegression(penalty='l2', C=0.001, solver='saga', max_iter=1000),
        'decision1': DecisionTreeClassifier(criterion='gini', max_depth=20, max_features='sqrt', min_samples_split=2),
        'decision2': DecisionTreeClassifier(criterion='gini', max_depth=50, max_features='sqrt', min_samples_split=2)
    }

    test_begin_year = 1985
    test_end_year = 2012

    validation_years = range(test_begin_year-4, test_end_year - 4 + 1)
    folds = range(0,5)

    # We will begin by pre-generating all the folds so that they can be easily parallelized
    print("Generating Folds")
    fold_maker = KFold(n_splits=5, shuffle=True, random_state=4312)
    indices = {}

    for year in validation_years:
        print("Validation year: ", year)
        complete_data = data[data.SENTENCE_END_YEAR <= year]

        indices[year] = {'train':{}, 'test':{}}

        fold_num = 0
        for train_indices, test_indices in fold_maker.split(complete_data[X_cols]):
            indices[year]['train'][fold_num] = train_indices
            indices[year]['test'][fold_num] = test_indices

            fold_num += 1

    print("Folds Generated")

    # Standard ----------------------------------------------------------------

    print('Starting Standard CV')
    pool = mp.Pool(processes=64)
    m = mp.Manager()
    queue = m.Queue()

    STOP_TOKEN="STOP"
    total_len = len(validation_years) * len(clfs) * len(folds)
    writer_process = mp.Process(target = Writer, args=("KFold_cv_results.csv", queue, STOP_TOKEN, total_len))
    writer_process.start()

    pool.starmap(standard_cv_classification, product(validation_years, clfs, folds, [queue], [indices]))
    queue.put(STOP_TOKEN)

    pool.close()
    writer_process.join()
    print('Done with Standard CV')

    # Temporal ----------------------------------------------------------------

    print('Starting Temporal CV')
    # Because this process is akin to how the model would be used in practice, we
    # will use it on both the validation years and the final testing years so that
    # we have modeling precisions for those years as well
    temporal_years = range(test_begin_year - 4, test_end_year + 1)

    pool = mp.Pool(processes=64)
    m = mp.Manager()
    queue = m.Queue()

    STOP_TOKEN="STOP"
    total_len = len(temporal_years) * len(clfs)
    writer_process = mp.Process(target = Writer, args=("temporal_cv_results.csv", queue, STOP_TOKEN, total_len))
    writer_process.start()

    pool.starmap(temporal_cv_classification, product(temporal_years, clfs, [queue]))
    queue.put(STOP_TOKEN)

    pool.close()
    writer_process.join()
    print("cv done, congratulations")

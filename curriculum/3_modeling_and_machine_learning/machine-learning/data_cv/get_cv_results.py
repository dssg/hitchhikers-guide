from itertools import product
import multiprocessing as mp
import random
import csv

import numpy as np
import pandas as pd
from sklearn import metrics
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

def standard_cv_classification(test_year, validation_year, model, queue):

    if validation_year < test_year:

        try:
            cv_start = 1950
            cv_end = test_year - 1

            # prep validation data
            df_validation = data[data.SENTENCE_END_YEAR == validation_year]
            X_validation = df_validation[X_cols]
            y_validation = df_validation[y_cols]

            # prep training data
            df_standard_train = data[(data.SENTENCE_END_YEAR != validation_year) &\
                                     (data.SENTENCE_END_YEAR < test_year)]
            X_standard_train = df_standard_train[X_cols]
            y_standard_train = np.ravel(df_standard_train[y_cols])


            # fit the models
            clf = clfs[model]
            clf.fit(X_standard_train, y_standard_train)
            validation_error = precision_at_abs(y_validation, clf.predict(X_validation))

            # return the results
            queue.put([cv_start, cv_end, validation_year, model, validation_error])

        except:
            pass

def Writer(dest_filename, queue, stop_token):
    total_len = 6560
    i = 0

    with open(dest_filename, 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        while True:
            line = queue.get()
            if line == stop_token:
                return
            writer.writerow(line)
            i += 1
            if i % 50 == 0:
                csv_file.flush()
                print(i/total_len, " %")

if __name__ == "__main__":
    data = pd.read_pickle("recid_data.pickle")

    X_cols = data.columns.difference(['RECITIVATED', 'INMATE_DOC_NUMBER', 'SENTENCE_END', 'SENTENCE_START'])
    y_cols = 'RECITIVATED'

    print(data.dtypes)

    clfs = {
        'rf1': RandomForestClassifier(n_estimators=500, n_jobs=-1, max_depth=30, max_features='log2', min_samples_split=10),
        'rf2': RandomForestClassifier(n_estimators=700, n_jobs=-1, max_depth=20, max_features='log2', min_samples_split=10),
        'extra1': ExtraTreesClassifier(n_estimators=200, n_jobs=-1, criterion='gini', max_depth=50, max_features='log2'),
        'extra2': ExtraTreesClassifier(n_estimators=400, n_jobs=-1, criterion='gini', max_depth=30, max_features='log2'),
        'logistic1': LogisticRegression(penalty='l1', C=0.001),
        'logistic2': LogisticRegression(penalty='l2', C=0.001),
        'decision1': DecisionTreeClassifier(criterion='gini', max_depth=20, max_features='sqrt', min_samples_split=2),
        'decision2': DecisionTreeClassifier(criterion='gini', max_depth=50, max_features='sqrt', min_samples_split=2)
    }

    test_begin_year = 1974
    test_end_year = 2013
    test_years = range(test_begin_year, test_end_year+1)

    validation_years = range(1973, test_end_year)

    pool = mp.Pool(processes=128)
    m = mp.Manager()
    queue = m.Queue()

    STOP_TOKEN="STOP"

    writer_process = mp.Process(target = Writer, args=("cv_results.csv", queue, STOP_TOKEN))
    writer_process.start()

    pool.starmap(standard_cv_classification, product(test_years, validation_years, clfs, [queue]))

    queue.put(STOP_TOKEN)

    pool.close()
    writer_process.join()

    print("cv done, congratulations")

# Put any helper preprocessing functions here (scaling, encoding, imputing, etc.)

import pandas as pd


def ensure_columns(X: pd.DataFrame, expected: list):
    for c in expected:
        if c not in X.columns:
            X[c] = 0
    return X[expected]

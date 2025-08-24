# Put any helper preprocessing functions here (scaling, encoding, imputing, etc.)

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("https://raw.githubusercontent.com/Freddy-Apaka/Finance_Prefiction_model/refs/heads/ml-deployment/loan.csv")

def ensure_columns(X: pd.DataFrame, expected: list):
    for c in expected:
        if c not in X.columns:
            X[c] = 0
    return X[expected]

encoder = LabelEncoder()

df["employment_type_encoded"] = encoder.fit_transform(df["employment_type"])
df["income_level_encoded"] = encoder.fit_transform(df["income_level"])

# Separeting the Default_status for Over sampling 
false_values = df[df['default_status']==False]
true_values = df[df['default_status']==True]

# Creating a variable with the same lenght as the over sampled
over_true_values = len(false_values)
# Over sampling the minority sample
over_sample_true_values = true_values.sample(over_true_values, random_state=42,replace=True)

# Joining the two sets in the DataFrame
df2 = pd.concat([over_sample_true_values,false_values], axis=0)

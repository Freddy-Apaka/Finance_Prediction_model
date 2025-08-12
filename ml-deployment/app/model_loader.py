import os
from joblib import load
import pandas as pd
from typing import Any

MODEL_PATH = os.getenv('MODEL_PATH', 'model/model.pkl')

_model = None


def load_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Please save your trained model there.")
        _model = load(MODEL_PATH)
    return _model


def predict(features: dict) -> dict:
    """Given a features dict, run any preprocessing needed and return model prediction.

    NOTE: modify this to match the preprocessing pipeline used at training time.
    """
    model = load_model()

    # convert to DataFrame with single row
    X = pd.DataFrame([features])

    # Example placeholder preprocessing: ensure order of columns expected by model
    # If your model was trained using a pipeline, then model.predict will accept raw X directly.

    # If necessary, add missing columns with default values
    # expected_cols = ['age','income']
    # for c in expected_cols:
    #     if c not in X.columns:
    #         X[c] = 0

    # Make prediction
    preds = model.predict(X)

    # If classifier with predict_proba
    proba = None
    if hasattr(model, 'predict_proba'):
        probs = model.predict_proba(X)
        # construct a mapping from class to probability for the first row
        class_labels = list(model.classes_)
        proba = {str(cl): float(probs[0, i]) for i, cl in enumerate(class_labels)}

    return {"prediction": preds[0].tolist() if hasattr(preds[0], 'tolist') else preds[0], "probability": proba}

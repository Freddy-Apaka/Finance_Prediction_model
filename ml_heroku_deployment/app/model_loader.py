import joblib
import pandas as pd

# load model
model = joblib.load("model/model.pkl")

def predict(features: dict):
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]

    # Map prediction result
    result = "Approved" if prediction == 1 else "Not Approved"
    return {"prediction": result}

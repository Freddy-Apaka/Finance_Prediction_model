from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os

from .schemas import PredictRequest, PredictResponse
from .model_loader import predict, load_model

load_dotenv()

app = FastAPI(title="ML Prediction API")

@app.on_event("startup")
async def startup_event():
    # try to preload model so that container fails early if model missing
    try:
        load_model()
    except Exception as e:
        # log but do not crash app startup here — you can change to raise if you prefer
        print(f"Warning loading model at startup: {e}")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
async def predict_endpoint(req: PredictRequest):
    try:
        result = predict(req.features)
        return PredictResponse(prediction=result['prediction'], probability=result.get('probability'))
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {e}")

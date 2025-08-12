from pydantic import BaseModel
from typing import Dict, Any

class PredictRequest(BaseModel):
    # generic dict of features; you may change to explicit typed fields
    features: Dict[str, Any]

class PredictResponse(BaseModel):
    prediction: Any
    probability: Dict[str, float] | None = None

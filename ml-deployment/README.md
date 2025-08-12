# ML Deployment Repo

This repo shows a minimal, production-friendly way to deploy a scikit-learn-style prediction model as a web service using FastAPI and Docker.

## What's included

- FastAPI app (`app/main.py`) exposing a `/predict` endpoint
- Model loader + preprocessing (`app/model_loader.py`)
- Pydantic schemas for request/response validation (`app/schemas.py`)
- Dockerfile and docker-compose for containerised deployment
- Example client (`example_client.py`) to call the API
- `requirements.txt` for dependencies

## How to use

### 1) Prepare your model

Train your model (e.g. with scikit-learn) then save it with joblib:

```python
from joblib import dump
# model is your trained estimator
dump(model, 'model/model.pkl')

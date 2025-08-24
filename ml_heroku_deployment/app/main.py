from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.model_loader import predict
from app.schemas import LoanFeatures

templates = Jinja2Templates(directory="app/templates")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict-form", response_class=HTMLResponse)
def predict_form(
    request: Request,
    loan_amount: float = Form(...),
    interest_rate: float = Form(...),
    credit_score: int = Form(...),
    employment_type_encoded: int = Form(...),
    income_level_encoded: int = Form(...),
):
    features = {
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "credit_score": credit_score,
        "employment_type_encoded": employment_type_encoded,
        "income_level_encoded": income_level_encoded
    }

    result = predict(features)
    return templates.TemplateResponse("index.html", {"request": request, "result": result["prediction"]})

@app.post("/predict")
def api_predict(features: LoanFeatures):
    return predict(features.dict())

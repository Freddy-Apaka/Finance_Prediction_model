from pydantic import BaseModel

# Define the schema for the prediction request
class LoanFeatures(BaseModel):
    loan_amount: float
    interest_rate: float
    credit_score: int
    employment_type_encoded: int
    income_level_encoded: int

 
# src/api/main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from src.api.auth import authenticate_user, create_access_token, get_current_user
import xgboost as xgb
import pandas as pd

app = FastAPI(title="Credit Risk API", description="AI-powered credit scoring for migration and banking", version="1.0")

# Load trained model
model = xgb.XGBClassifier()
model.load_model("src/models/base_model.json")

# Input schema
class CreditInput(BaseModel):
    unemployment_rate: float
    poverty_rate: float

# Login route to get JWT token
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not authenticate_user(form_data.username, form_data.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = create_access_token(data={"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

# Protected prediction route
@app.post("/predict/")
def predict(data: CreditInput, user: str = Depends(get_current_user)):
    df = pd.DataFrame([{
        "UnemploymentRate": data.unemployment_rate,
        "PovertyRate": data.poverty_rate
    }])
    prediction = model.predict(df)[0]
    risk = "Low Risk" if prediction == 1 else "High Risk"
    return {
        "prediction": int(prediction),
        "risk_level": risk
    }
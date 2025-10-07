# src/api/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import xgboost as xgb
import pandas as pd
import pickle

app = FastAPI(title="Credit Risk API", version="1.0")

# مدل فرضی (در حالت واقعی باید از فایل ذخیره‌شده بارگذاری شود)
model = xgb.XGBClassifier()
model.load_model("src/models/base_model.json")  # اگر با save_model ذخیره شده

class CreditInput(BaseModel):
    unemployment_rate: float
    poverty_rate: float

@app.post("/predict/")
def predict_credit_risk(data: CreditInput):
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
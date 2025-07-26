# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load model
model = joblib.load("models/xgb_sales_model.pkl")

# Init app
app = FastAPI()

# Request schema
class SalesInput(BaseModel):
    lag_1: float
    lag_7: float

# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Demand Forecasting API"}

# Predict route
@app.post("/predict/")
def predict_sales(data: SalesInput):
    try:
        input_dict = data.dict()
        df = pd.DataFrame([input_dict])
        prediction = model.predict(df)
        return {"predicted_sales": float(prediction[0])}  # ✅ Convert to regular float
    except Exception as e:
        print("❌ ERROR:", str(e))
        return {"error": str(e)}



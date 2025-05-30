from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
import uvicorn
import os

# 💾 Load model and scaler
model = joblib.load("./model.pkl")
scaler = joblib.load("./scaler.pkl")

# 🚀 Initialize FastAPI
app = FastAPI(title="Fraud Detection API")

# 🧾 Feature names used by the scaler

feature_names = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
       'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

# 🧾 Define input schema
class Transaction(BaseModel):
    features: list[float]

# 🔍 Prediction route
@app.post("/predict")
def predict(transaction: Transaction):
    try:
        # Convert to DataFrame to include feature names
        input_df = pd.DataFrame([transaction.features], columns=feature_names)
        scaled_input = scaler.transform(input_df)

        # Make prediction
        prediction = model.predict(scaled_input)[0]
        proba = model.predict_proba(scaled_input)[0][1]

        return {
            "prediction": int(prediction),
            "fraud_probability": round(proba, 4),
            "status": "Fraud" if prediction == 1 else "Not Fraud",
        }
    except Exception as e:
        return {"error": str(e)}

# 🧪 Optional: Run with `python main.py`
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
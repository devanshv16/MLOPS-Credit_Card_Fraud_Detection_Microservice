# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn
import os

# 💾 Load model and scaler
model = joblib.load("./model.pkl")
scaler = joblib.load("./scaler.pkl")

# 🚀 Initialize FastAPI
app = FastAPI(title="Fraud Detection API")


# 🧾 Define input schema using Pydantic
class Transaction(BaseModel):
    features: list[float]  # must match the feature count after preprocessing


# 🔍 Prediction route
@app.post("/predict")
def predict(transaction: Transaction):
    try:
        # Convert and scale input
        input_array = np.array([transaction.features])
        scaled_input = scaler.transform(input_array)

        # Make prediction
        prediction = model.predict(scaled_input)[0]
        proba = model.predict_proba(scaled_input)[0][
            1
        ]  # probability of fraud (class 1)

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

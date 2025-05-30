import pandas as pd
from utils import load_data, preprocess_data

# Load and preprocess
df = load_data("./data/creditcard.csv")
X, y, scaler = preprocess_data(df)

# ✅ First sample (likely non-fraud)
sample_input = X[0].tolist()
sample_label = y[0]
print("🟢 Sample input (non-fraud):")
print(sample_input)
print("✅ Actual class:", sample_label)

# 🚨 Sample from fraud class
import numpy as np
fraud_indices = np.where(y == 1)[0]
fraud_sample_input = X[fraud_indices[0]].tolist()
fraud_sample_label = y[fraud_indices[0]]
print("\n🔴 Sample input (fraud):")
print(fraud_sample_input)
print("⚠️ Actual class:", fraud_sample_label)
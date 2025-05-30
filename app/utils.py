# app/utils.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE


def load_data(filepath):
    df = pd.read_csv(filepath)
    return df


def preprocess_data(df):
    X = df.drop("Class", axis=1)
    print(X.columns)
    y = df["Class"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    #print(X_scaled.columns)
    return X_scaled, y, scaler


def train_test_data(X, y):
    return train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)


def resample_data(X_train, y_train):
    smote = SMOTE(random_state=42)
    return smote.fit_resample(X_train, y_train)


def save_model(model, scaler, model_path="model.pkl", scaler_path="scaler.pkl"):
    import joblib

    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

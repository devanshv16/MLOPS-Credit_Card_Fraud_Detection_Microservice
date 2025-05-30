# app/train.py

from utils import load_data, preprocess_data, train_test_data, resample_data, save_model
from model import get_model
from sklearn.metrics import classification_report, precision_recall_fscore_support
import os
import mlflow
import mlflow.sklearn


def train_model(model_name="logistic", data_path="./data/creditcard.csv"):
    print(f"🔄 Loading data from: {data_path}")
    df = load_data(data_path)

    print("🧼 Preprocessing data...")
    X, y, scaler = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_data(X, y)
    X_resampled, y_resampled = resample_data(X_train, y_train)

    print(f"🧠 Training model: {model_name}")
    model = get_model(model_name)
    model.fit(X_resampled, y_resampled)

    print("✅ Evaluating model...")
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)

    print("💾 Saving model and scaler...")
    save_model(model, scaler)

    print("📦 Logging to MLflow...")
    mlflow.set_experiment("Credit Card Fraud Detection")
    with mlflow.start_run():
        mlflow.log_param("model_name", model_name)
        import numpy as np

        input_example = np.array(
            [X_test[0]]
        )  # Already a NumPy array, just slice  # 2D array

        mlflow.sklearn.log_model(
            model,
            "model",
            input_example=input_example,
            registered_model_name="FraudDetector",
        )
        for label in [0, 1]:
            p, r, f, _ = precision_recall_fscore_support(
                y_test, y_pred, average="binary", pos_label=label
            )
            print(
                f"[MLflow] Logging for class {label} — Precision: {p}, Recall: {r}, F1: {f}"
            )
            mlflow.log_metric(f"precision_class_{label}", p)
            mlflow.log_metric(f"recall_class_{label}", r)
            mlflow.log_metric(f"f1_score_class_{label}", f)

        from sklearn.metrics import ConfusionMatrixDisplay
        import matplotlib.pyplot as plt

        # Save confusion matrix
        disp = ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
        plt.title("Confusion Matrix")
        plt.savefig("confusion_matrix.png")
        mlflow.log_artifact("confusion_matrix.png")

        from sklearn.metrics import RocCurveDisplay

        # Save ROC curve
        RocCurveDisplay.from_estimator(model, X_test, y_test)
        plt.title("ROC Curve")
        plt.savefig("roc_curve.png")
        mlflow.log_artifact("roc_curve.png")

        os.remove("confusion_matrix.png")
        os.remove("roc_curve.png")
    print("🚀 Training pipeline complete!")


if __name__ == "__main__":
    train_model()

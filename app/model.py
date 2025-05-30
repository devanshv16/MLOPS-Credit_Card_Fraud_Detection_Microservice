from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


def get_model(model_name="random_forest"):
    if model_name == "logistic":
        return LogisticRegression(class_weight="balanced", random_state=42)
    elif model_name == "random_forest":
        return RandomForestClassifier(
            class_weight="balanced", n_estimators=100, random_state=42
        )
    elif model_name == "xgboost":
        return XGBClassifier(
            scale_pos_weight=100,
            use_label_encoder=False,
            eval_metric="logloss",
            random_state=42,
        )
    else:
        raise ValueError(f"Model '{model_name}' is not supported.")

from typing import Any
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix


def evaluate_model(model:Any, X: pd.DataFrame, y :pd.Series) -> dict[str, Any]:
    predictions = model.predict(X)
    return {
        "accuracy": accuracy_score(y, predictions),
        "recall_malignant": recall_score(y, predictions, pos_label=0, zero_division=0),
        "benign_f1": f1_score(y, predictions, zero_division=0),
        "confusion_matrix": confusion_matrix(y, predictions, labels=[0, 1]),
    }

def evaluate_cv_results(results: dict[str, np.ndarray]) -> tuple[float, float]:
    return float(results["test_recall_malignant"].mean()), float(results["test_recall_malignant"].std())
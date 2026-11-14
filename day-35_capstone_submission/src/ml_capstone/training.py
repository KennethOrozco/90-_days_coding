from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, f1_score, make_scorer, confusion_matrix
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd
from typing import Any
from pathlib import Path
import joblib
import json
from ml_capstone.evaluation import evaluate_model, evaluate_cv_results
from ml_capstone.selection import select_best_model

def main() -> None:
    data = load_breast_cancer(as_frame=True)  # Load and inspect data
    
    X = data.data

    y = data.target

    #Print dataset shape and class distrbution

    print("X shape: ", X.shape)
    print("y shape: ", y.shape)

    class_distribution = y.value_counts()

    print(f"Class Distribution:\n{class_distribution}")


    # Split data into training and testing sets

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )

    # Define candidate pipelines
    lr_model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=2000))
    ])

    rf_model = Pipeline([
        ("classifier", RandomForestClassifier(
            n_estimators=200,
            random_state=42
        ))
    ])

    #Cross Validate candidates
    malignant_recall = make_scorer(
        recall_score,
        pos_label=0
    )

    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    scoring = {
        "accuracy": "accuracy",
        "f1_benign": "f1",
        "recall_malignant": malignant_recall
    }

    lr_results = cross_validate(
        lr_model,
        X_train,
        y_train,
        cv=cv,
        scoring=scoring,
    )

    rf_results = cross_validate(
        rf_model,
        X_train,
        y_train,
        cv=cv,
        scoring=scoring
    )

    # Select winning model off of higher mean malignant recall score. Lower standard deviaton as tie breaker.
    # If still tied choose Logistic Regression

    lr_mean_recall, lr_std_recall = evaluate_cv_results(lr_results)
    rf_mean_recall, rf_std_recall = evaluate_cv_results(rf_results)

    selected_model_name = select_best_model(lr_mean_recall, lr_std_recall, rf_mean_recall, rf_std_recall)

    best_model = lr_model if selected_model_name == "Logistic Regression" else rf_model
    # Fit and evaluate winner

    best_model.fit(X_train, y_train)

    best_model_data = evaluate_model(best_model, X_test, y_test)

    for key, value in best_model_data.items():
        if key == "confusion_matrix":
            print(f"{key}:\n{value}")
        else:
            print(f"{key}: {value}")

    # Save model and metadata

    meta = {
        "selected_model": selected_model_name,
        "selection_metric": "mean_cv_recall_malignant",
        "cv_results": {
            "Logistic Regression": {
                "mean_recall_malignant": lr_mean_recall,
                "std_recall_malignant": lr_std_recall
            },
            "Random Forest": {
                "mean_recall_malignant": rf_mean_recall,
                "std_recall_malignant": rf_std_recall
            }
        },
        "test_metrics": {
            "accuracy": best_model_data["accuracy"],
            "recall_malignant" : best_model_data["recall_malignant"],
            "benign_f1": best_model_data["benign_f1"]
        },
        "dataset": "sklearn_breast_cancer",
        "feature_names": best_model.feature_names_in_.tolist(),
        "random_state": 42
    }
    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    models_dir = PROJECT_ROOT / "models"
    models_dir.mkdir(exist_ok=True)

    joblib.dump(best_model, models_dir / "best_model.joblib")

    with open(models_dir / "metadata.json", "w", encoding="utf-8") as file:
        json.dump(meta, file, indent=4)


if __name__ == "__main__":
    main()
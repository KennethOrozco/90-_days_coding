from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_validate, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from typing import Any

#Get a dictionary of metrics from model
def evaluate_model(model:Any, X: pd.DataFrame, y :pd.Series) -> dict[str, Any]:
    predictions = model.predict(X)
    return {
        "model": model.named_steps["classifier"],
        "accuracy": accuracy_score(y, predictions),
        "precision": precision_score(y, predictions, zero_division=0),
        "recall": recall_score(y, predictions, zero_division=0),
        "f1": f1_score(y, predictions, zero_division=0),
        "matrix": confusion_matrix(y, predictions, labels=[0, 1]),
        "classification_report": classification_report(y, predictions, zero_division=0)
    }
# Make X and y datasets from load_breast_cancer and split in to training and testing data sets
data = load_breast_cancer(as_frame=True)

X = data.data

y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

#Make a pipeline for each classifier
lr_model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=2000))
])

rf_model = Pipeline([
    ("classifier", RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ))
])

#Configure identical cv's

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
#Evaluate both models

scoring = [
    "accuracy",
    "precision",
    "recall",
    "f1"
]

lr_results = cross_validate(
    estimator=lr_model,
    X=X_train,
    y=y_train,
    cv=cv,
    scoring=scoring,
    n_jobs=-1
)

rf_results = cross_validate(
    estimator=rf_model,
    X=X_train,
    y=y_train,
    cv=cv,
    scoring=scoring,
    n_jobs=-1
)

# Convert results to a dataframe with the mean and std for each metric
lr_data = {}
rf_data = {}

for metric in lr_results:
    lr_data[f"{metric}_mean"] = lr_results[metric].mean()
    lr_data[f"{metric}_std"] = lr_results[metric].std()

for metric in rf_results:
    rf_data[f"{metric}_mean"] = rf_results[metric].mean()
    rf_data[f"{metric}_std"] = rf_results[metric].std()

df = pd.DataFrame([lr_data, rf_data], index=["Logistic Regression", "Random Forest"])

print(df)

#Extract f1 scores and calculate the differences

lr_f1_scores = lr_results["test_f1"]
rf_f1_scores = rf_results["test_f1"]

differences = rf_f1_scores - lr_f1_scores

print(lr_f1_scores)
print(rf_f1_scores)
print(differences)
print(differences.mean())
print("Fold count where LR performed better: ", np.sum(differences < 0))
print("Fold count where RF performed better: ", np.sum(differences > 0))
print("# of tied folds: ", np.sum(differences == 0))

lr_f1_mean = lr_f1_scores.mean()
rf_f1_mean = rf_f1_scores.mean()
lr_f1_std = lr_f1_scores.std()
rf_f1_std = rf_f1_scores.std()

#Choose best models off of qualifications
if lr_f1_mean > rf_f1_mean:
    best_model = lr_model
elif rf_f1_mean > lr_f1_mean:
    best_model = rf_model
else:
    if rf_f1_std < lr_f1_std:
        best_model = rf_model
    else:
        best_model = lr_model

#Train and evaluate model
best_model.fit(X_train, y_train)

best_model_data = evaluate_model(best_model, X_test, y_test)

for key, value in best_model_data.items():
    if key == "matrix":
        print(f"{key}:\n{value}")
    else:
        print(f"{key}: {value}")


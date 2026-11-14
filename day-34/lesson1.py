from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, f1_score
from typing import Any
import joblib
from pathlib import Path

#Get a dictionary of metrics from model
def evaluate_model(model:Any, X: pd.DataFrame, y :pd.Series) -> dict[str, float]:
    predictions = model.predict(X)
    return {
        "accuracy": accuracy_score(y, predictions),
        "f1": f1_score(y, predictions, zero_division=0)
    }

data = load_breast_cancer(as_frame=True)
#Seperate features and targets and split them into testing and training sets.
X = data.data

y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

#Train a pipeline

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=2000))
])

model.fit(X_train, y_train)

og_predictions = model.predict(X_test)

#Calculate test accuracy and f1

model_data = evaluate_model(model, X_test, y_test)


#Save and load the model

model_dir = Path("models")
model_dir.mkdir(parents=True, exist_ok=True)

model_path = model_dir / "breast_cancer_pipeline.joblib"

joblib.dump(model, model_path)

loaded_model = joblib.load(model_path)
#Compare the original model with the loaded one
loaded_model_data = evaluate_model(loaded_model, X_test, y_test)

loaded_predictions = loaded_model.predict(X_test)

print("OG Test Accuracy: ", model_data["accuracy"])
print("OG F1 Score: ", model_data["f1"])



print("Loaded Test Accuracy: ", loaded_model_data["accuracy"])
print("Loaded F1 Score: ", loaded_model_data["f1"])

print(np.array_equal(og_predictions, loaded_predictions))

print(type(loaded_model))
print(loaded_model.named_steps.keys())


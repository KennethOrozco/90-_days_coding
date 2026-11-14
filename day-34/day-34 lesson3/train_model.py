from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from sklearn.metrics import accuracy_score, f1_score
import json
import sklearn
import sys

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

#Print accuracy and F1
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, zero_division=0)
print("Accuracy: ", accuracy)
print("F1: ", f1)

#Save  the model
base_dir = Path(__file__).resolve().parent

model_dir = base_dir / "models"
model_dir.mkdir(parents=True, exist_ok=True)
model_path = model_dir / "breast_cancer_pipeline.joblib"
metadata_path = model_dir/ "metadata.json"

joblib.dump(model, model_path)

#Create metadata file with json
metadata = {
    "model_name": "breast_cancer_pipeline.joblib",
    "dataset": "sklearn_breast_cancer",
    "feature_count": int(model.n_features_in_),
    "feature_names": model.feature_names_in_.tolist(),
    "test_accuracy": accuracy,
    "test_f1": f1,
    "random_state": 42,
    "python": sys.version.split()[0],
    "scikit_learn": sklearn.__version__,
    "numpy": np.__version__,
    "pandas": pd.__version__,
    "joblib": joblib.__version__
}

with open(metadata_path, "w", encoding="utf-8") as file:
    json.dump(metadata, file, indent=4)
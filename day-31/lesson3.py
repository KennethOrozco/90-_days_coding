import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import clone
from typing import Any

# use model and x, y to get a dictionary of metrics
def evaluate_model(model:Any, X: pd.DataFrame, y :pd.Series) -> dict[str, float]:
    predictions = model.predict(X)
    return {
        "accuracy": accuracy_score(y, predictions),
        "precision": precision_score(y, predictions, zero_division=0),
        "recall": recall_score(y, predictions, zero_division=0),
        "f1": f1_score(y, predictions, zero_division=0)
    }


rng = np.random.default_rng(42)
n = 600

age = rng.integers(18, 70, size=n).astype(float)
income = rng.normal(65000, 22000, size=n)
income = np.clip(income, 18000, 160000)

membership = rng.choice(
    ["Basic", "Standard", "Premium"],
    size=n,
    p=[0.45, 0.35, 0.20]
)

region = rng.choice(
    ["North", "South", "East", "West"],
    size=n
)

visits = rng.poisson(5, size=n).astype(float)

purchase_score = (
    0.035 * (age - 35)
    + 0.000025 * (income - 65000)
    + 0.30 * visits
    + 0.7 * (membership == "Premium")
    - 1.7
)

purchase_probability = 1 / (1 + np.exp(-purchase_score))
purchased = rng.binomial(1, purchase_probability)

customers = pd.DataFrame({
    "age": age,
    "annual_income": income,
    "membership": membership,
    "region": region,
    "visits": visits,
    "purchased": purchased
})

# Introduce missing values into features only
for column in ["age", "annual_income", "visits"]:
    missing_indices = rng.choice(
        n, size=30, replace=False
    )
    customers.loc[missing_indices, column] = np.nan

for column in ["membership", "region"]:
    missing_indices = rng.choice(
        n, size=20, replace=False
    )
    customers.loc[missing_indices, column] = None

#Replace all None values in categorical features with np.nan    
customers.loc[:,["membership", "region"]] = customers[["membership", "region"]].replace({None:np.nan})
#Seperate X and y

X = customers.drop(columns=["purchased"])

y = customers["purchased"]

#Split data into train, validated, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=42,
    stratify=y
)

X_validation, X_test, y_validation, y_test = train_test_split(
    X_temp,
    y_temp,
    test_size=0.5,
    random_state=42,
    stratify=y_temp
)
#make two seperate pipelines for numerical and categorical features
numerical_features = [
    "age",
    "annual_income",
    "visits"
]

categorical_features = [
    "membership",
    "region"
]

numerical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
])
# use the preprocesser of both pipelines to make a logistic regression model and a random forest ensemble
#train model after creating them
preprocesser = ColumnTransformer([
    ("numerical", numerical_pipeline, numerical_features),
    ("categorical", categorical_pipeline, categorical_features)

])

lr_model = Pipeline([
    ("preprocesser", clone(preprocesser)),
    ("model", LogisticRegression(max_iter=1000))
])
lr_model.fit(X_train, y_train)

rf_model = Pipeline([
    ("preprocesser", clone(preprocesser)),
    ("model", RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    ))
])
rf_model.fit(X_train, y_train)
#Get validation metrics
lr_validation_data = evaluate_model(lr_model, X_validation, y_validation)

rf_validation_data = evaluate_model(rf_model, X_validation, y_validation)
#print report
print("Model: Logistic Regression")
for key, value in lr_validation_data.items():
    print(f"{key}: {value}")

print("Model: Random Forest Classifier")
for key, value in rf_validation_data.items():
    print(f"{key}: {value}")

#compare models for best f1. accuracy tie breaker
if lr_validation_data["f1"] > rf_validation_data["f1"]:
    print("Best is Logistic Regression")
    best_model = lr_model
elif rf_validation_data["f1"] > lr_validation_data["f1"]:
    print("Best is Random Forest Classifier")
    best_model = rf_model
else:
    if rf_validation_data["accuracy"] > lr_validation_data["accuracy"]:
        print("Best is Random Forest Classifier")
        best_model = rf_model
    else:
        print("Best is Logistic Regression")
        best_model = lr_model


#Evaluate best model on test data

best_model_data = evaluate_model(best_model, X_test, y_test)
#print report on best model
print("Best model: ")
for key, value in best_model_data.items():
    print(f"{key}: {value}")








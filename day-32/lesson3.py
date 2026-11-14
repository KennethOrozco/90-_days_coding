import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
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

customers = pd.DataFrame({
    "age": rng.integers(18, 70, size=n),
    "annual_income": rng.normal(60000, 18000, size=n),
    "visits": rng.poisson(8, size=n),
    "membership": rng.choice(
        ["Basic", "Silver", "Gold"],
        size=n
    ),
    "region": rng.choice(
        ["North", "South", "East", "West"],
        size=n
    )
})

purchase_score = (
    0.03 * customers["age"]
    + 0.000025 * customers["annual_income"]
    + 0.25 * customers["visits"]
    + 0.8 * (customers["membership"] == "Gold")
    - 4.5
)

purchase_probability = 1 / (1 + np.exp(-purchase_score))

customers["purchased"] = rng.binomial(
    1,
    purchase_probability
)

# Inject missing values into feature columns.
for column in [
    "age",
    "annual_income",
    "visits",
    "membership",
    "region"
]:
    missing_indices = rng.choice(
        customers.index,
        size=25,
        replace=False
    )

    if column in ["membership", "region"]:
        customers.loc[missing_indices, column] = None
    else:
        customers.loc[missing_indices, column] = np.nan

#Replace None values with np.nan
customers.loc[:,["membership", "region"]] = customers[["membership", "region"]].replace({None:np.nan})

#Seperate X and y
X = customers.drop(columns=["purchased"])

y = customers["purchased"]

#Split data set into train set and test set.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y, 
    test_size=0.2,
    stratify=y,
    random_state=42
)

# Build Preprocessing pipelines
numeric_features = [
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
    ("encoder", OneHotEncoder(
        handle_unknown="ignore",
        sparse_output=False
    ))
])

#Cobine with ColumnTransformer
preprocesser = ColumnTransformer([
    ("num", numerical_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])

#Build the full model pipeline
model = Pipeline([
    ("preprocessor", preprocesser),
    ("classifier", RandomForestClassifier(
        random_state=42
    ))
])

#Configure hyperparameter tuning
param_grid = {
    "classifier__n_estimators": [50, 100],
    "classifier__max_depth": [3, 5, None],
    "classifier__min_samples_split": [2, 5]
}

#Create a StratifiedKFold
cv = StratifiedKFold(
    n_splits=5,
    shuffle=True, 
    random_state=42
)

#create a gridsearch
search = GridSearchCV(
    model,
    param_grid=param_grid,
    cv=cv,
    scoring="f1",
    n_jobs=-1,
    refit=True
)

search.fit(X_train, y_train)

best_model = search.best_estimator_
print(search.best_params_)
print(search.best_score_)


df = pd.DataFrame(search.cv_results_)

results = df[["params", "mean_test_score", "std_test_score", "rank_test_score"]]

sorted_results = results.sort_values(by="rank_test_score")

print(sorted_results.to_string(index=False))

best_model_data = evaluate_model(best_model, X_test, y_test)

for key, value in best_model_data.items():
    print(f"{key}: {value}")
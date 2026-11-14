from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


data = load_breast_cancer(as_frame=True)

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

#Build Random Forest pipeline
pipeline = Pipeline([
    ("classifier", RandomForestClassifier(random_state=42))
])

#Defien parameter grid
param_grid = {
    "classifier__n_estimators": [50, 100],
    "classifier__max_depth": [3, 5, None],
    "classifier__min_samples_split": [2, 5]
}
# Configure Grid Search
cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    scoring="accuracy",
    cv=cv,
    n_jobs=-1,
    refit=True
)

#Train Grid search model
search.fit(X_train, y_train)

#Inspect the best configuration
best_model = search.best_estimator_
print(search.best_params_)
print(search.best_score_)
print(type(best_model))

df = pd.DataFrame(search.cv_results_)

results = df[["params", "mean_test_score", "std_test_score", "rank_test_score"]]

sorted_results = results.sort_values(by="rank_test_score")

print(sorted_results.to_string(index=False))



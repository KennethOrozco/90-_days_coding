from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
import pandas as pd
from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

def evaluate_model(model: any , X_train: np.ndarray , X_test: np.ndarray, y_train: np.ndarray, y_test: np.ndarray ) -> dict:
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)
    train_accuracy = accuracy_score(y_train, train_predictions)
    test_accuracy = accuracy_score(y_test, test_predictions)
    precision = precision_score(y_test, test_predictions, zero_division=0)
    recall = recall_score(y_test, test_predictions)
    f1 = f1_score(y_test, test_predictions)
    matrix = confusion_matrix(y_test, test_predictions)
    actual_depth = model.get_depth()
    number_of_leaves = model.get_n_leaves()
    return {
        "train_accuracy": train_accuracy,
        "test_accuracy": test_accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "matrix": matrix,
        "actual_depth": actual_depth,
        "number_of_leaves": number_of_leaves
        }


X, y = make_classification(
    n_samples=1000,
    n_features=12,
    n_informative=6,
    n_redundant=3,
    flip_y=0.05,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

baseline_model_dict = evaluate_model(model, X_train, X_test, y_train, y_test)
print(baseline_model_dict)

param_grid = {
    "max_depth": [2, 3, 4, 5, 7, 10, None],
    "min_samples_leaf": [1, 3, 5, 10],
    "min_samples_split": [2, 5, 10]
}

search = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    cv=5,
    param_grid=param_grid,
    scoring="f1",
    n_jobs=-1,
)

search.fit(X_train, y_train)

print(search.best_params_)
print(search.best_score_)

tuned_model = search.best_estimator_

tuned_model_dict = evaluate_model(tuned_model, X_train, X_test, y_train, y_test)

print(tuned_model_dict)

df = pd.DataFrame(search.cv_results_)

results = df[["params", "mean_test_score", "std_test_score", "rank_test_score"]]
sorted_results = results.sort_values(by="mean_test_score", ascending=False)

print(sorted_results.head())

feature_names_list = [f"feature_{i}" for i in range(X.shape[1])]

print(export_text(tuned_model, feature_names=feature_names_list))


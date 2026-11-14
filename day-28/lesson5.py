from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split , GridSearchCV
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import pprint
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

X, y = make_classification(
    n_samples=600,
    n_features=12,
    n_informative=6,
    n_redundant=3,
    flip_y=0.06,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

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


param_grid = {
    "max_depth": [2, 3, 4, 5, 7, None],
    "min_samples_leaf": [1, 3, 5, 10]
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

best_model = search.best_estimator_

best_train_predictions = best_model.predict(X_train)
best_test_predictions = best_model.predict(X_test)
best_train_accuracy = accuracy_score(y_train, best_train_predictions)
best_test_accuracy = accuracy_score(y_test, best_test_predictions)
best_precision = precision_score(y_test, best_test_predictions, zero_division=0)
best_recall = recall_score(y_test, best_test_predictions)
best_f1 = f1_score(y_test, best_test_predictions)
best_matrix = confusion_matrix(y_test, best_test_predictions, labels=[0, 1])
best_actual_depth = best_model.get_depth()
best_number_of_leaves = best_model.get_n_leaves()
print(f"Matrix: \n{best_matrix}")
print(f"Actual depth: {best_actual_depth}")
print(f"Number of leaves: {best_number_of_leaves}")

metrics = ["train accuracy", "test Accuracy", "precision", "recall", "F1"]
baseline = [train_accuracy, test_accuracy, precision, recall, f1]
tuned = [best_train_accuracy, best_test_accuracy, best_precision, best_recall, best_f1]

for metric, metric_baseline, metric_tuned in zip(metrics, baseline, tuned):
    print(f"Baseline model's {metric}: {metric_baseline:.3f}")
    print(f"Tuned model's {metric}: {metric_tuned:.3f}")

results = pd.DataFrame(search.cv_results_)
better = results[["params", "mean_test_score", "std_test_score", "rank_test_score"]]
better_sorted = better.sort_values(by="mean_test_score", ascending=False)

params = results["params"]
f1_mean = results["mean_test_score"]
f1_std = results["std_test_score"]
ranks = results["rank_test_score"]

data = {}

for index, (param, mean, std, rank) in enumerate(zip(params, f1_mean, f1_std, ranks)):
    letter = chr(65 + index)
    data[f"model_{letter}"] = {
        "max_depth": param["max_depth"],
        "min_samples_leaf": param["min_samples_leaf"],
        "mean_test_score": mean,
        "std_test_score": std,
        "rank_test_score": rank
    }

df = pd.DataFrame(data)

sorted_data = dict(sorted(data.items(), key=lambda model:model[1]["mean_test_score"], reverse=True))

first_five_dict = dict(list(sorted_data.items())[:5])
pprint.pprint(first_five_dict)

print(better_sorted.head())












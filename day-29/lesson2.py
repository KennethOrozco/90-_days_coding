from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score
import numpy as np
from typing import Any

#Make a dictionary that stores training and test accuracy of model
def evaluate_model(model: Any, X_train: np.ndarray, X_test: np.ndarray, y_train: np.ndarray, y_test:np.ndarray)-> dict:
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)
    train_accuracy = accuracy_score(y_train, train_predictions)
    test_accuracy = accuracy_score(y_test, test_predictions)
    precision = precision_score(y_test, test_predictions, zero_division=0)
    recall = recall_score(y_test, test_predictions)
    return {
        "train_accuracy": train_accuracy,
        "test_accuracy": test_accuracy,
        "gap": train_accuracy - test_accuracy,
        "precision": precision,
        "recall": recall,
        "predictions": test_predictions
        }
#Makes a classification report
def model_report(data: dict[str, Any]) -> None:
    for index, prediction in enumerate(data["predictions"], start= 1):
        classification = "Malignant" if prediction == 0 else "Benign"
        print(f"Test observation #{index}: Predicted class: {classification}")

data = load_breast_cancer()

X = data.data
y = data.target

feature_names = data.feature_names

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
#train decision tree
decision_model = DecisionTreeClassifier(max_depth=5, random_state=42)
decision_model.fit(X_train, y_train)
# get train and test predictions for decision tree
decision_train_predictions = decision_model.predict(X_train)
decision_test_predictions = decision_model.predict(X_test)

#train random forest
rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
rf_model.fit(X_train, y_train)

decision_data = evaluate_model(decision_model, X_train, X_test, y_train, y_test)

rf_data = evaluate_model(rf_model, X_train, X_test, y_train, y_test)

#make a report of the models data
model_report(decision_data)
model_report(rf_data)

print(classification_report(y_test, decision_data["predictions"]))
print(classification_report(y_test, rf_data["predictions"]))

print("Training accuracy for Decision Tree model: ", decision_data["train_accuracy"])
print("Training accuracy for RF ensemble: ", rf_data["train_accuracy"])
print("Test accuracy for Decision Tree model: ", decision_data["test_accuracy"])
print("Test accuracy for RF ensemble: ", rf_data["test_accuracy"])
#print # of trained trees
print(len(rf_model.estimators_))
#prints classes of the forest
print(rf_model.classes_)

# print first five labels from the prediction
rf_predictions = rf_model.predict(X_test)
print(rf_predictions[:5])

#print first five probabilities from the prediction
rf_proba = rf_model.predict_proba(X_test)
print(rf_proba[:5])

#find the 5 most important features and their importance values.
features = {}
for index, (importance, name) in enumerate(zip(rf_model.feature_importances_, feature_names)):
    features[name] = importance

sorted_features = dict(sorted(features.items(), key=lambda name:name[1], reverse=True))

for index, (name, importance) in enumerate(sorted_features.items()):
    if index > 4:
        break
    print(f"{name}: {importance}")





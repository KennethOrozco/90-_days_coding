from sklearn.tree import (DecisionTreeClassifier, export_text)
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

customers = [
    [22, 2500],
    [35, 3000],
    [27, 5000],
    [42, 6500],
    [19, 1800],
    [29, 4200],
    [31, 2000],
    [45, 5500],
    [24, 3200],
    [38, 4700],
    [26, 3900],
    [33, 2800],
    [41, 6000],
    [21, 2100],
    [36, 3500],
    [28, 4800],
]

purchased = [
    0, 1, 1, 1,
    0, 1, 1, 1,
    0, 1, 0, 1,
    1, 0, 1, 1,
]

X = customers

y = purchased

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

training_accuracy = accuracy_score(y_train, train_predictions)
testing_accuracy = accuracy_score(y_test, test_predictions)
precision = precision_score(y_test, test_predictions, zero_division=0)
recall = recall_score(y_test, test_predictions, zero_division=0)
f1 = f1_score(y_test, test_predictions, zero_division=0)
matrix = confusion_matrix(y_test, test_predictions, labels=[0, 1])
print(f"Training Accuracy: {training_accuracy}")
print(f"Testing Accuracy: {testing_accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1: {f1}")
print(f"Matrix:\n{matrix}")

print(model.get_depth())
print(model.get_n_leaves())
print(export_text(model, feature_names=["age", "income"]))

new_customers = [
    [25, 4500],
    [40, 2500],
    [32, 5000],
    [23, 2000],
]

new_predictions = model.predict(new_customers)
new_probabilities = model.predict_proba(new_customers)
print(new_predictions)
print(new_probabilities)

for index, (prediction, probability, customer) in enumerate(zip(new_predictions, new_probabilities, new_customers), start=1):
    print(f"Customer #{index} ")
    print(f"Age: {customer[0]}")
    print(f"Income: {customer[1]}")
    print(f"Predicted Class: {prediction}")
    print(f"Probabiltiy: {probability[1]:.3f}")
    

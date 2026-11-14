import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

study_hours = np.array([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    2, 3, 5, 7, 9, 4, 6, 8, 10, 1
])

attendance = np.array([
    50, 55, 60, 65, 70, 75, 80, 85, 90, 95,
    60, 65, 72, 82, 92, 68, 78, 88, 98, 45
])

passed = np.array([
    0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
    0, 0, 1, 1, 1, 0, 1, 1, 1, 0
])

X = np.column_stack((study_hours, attendance))

y = passed

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_train, y_train)
logistic_train_prediction = logistic_model.predict(X_train)
logistic_test_prediction = logistic_model.predict(X_test)
logistic_train_accuracy = accuracy_score(y_train, logistic_train_prediction)
logistic_test_accuracy = accuracy_score(y_test, logistic_test_prediction)
logistic_generalization_gap = logistic_train_accuracy - logistic_test_accuracy
print("Logistic Regression's Training Accuracy: ", logistic_train_accuracy)
print("Logistic Regression's Testing Accuracy: ", logistic_test_accuracy)
print("Logistic Regression's Generalization Gap: ", logistic_generalization_gap)

decision_model = DecisionTreeClassifier(random_state=42)
decision_model.fit(X_train, y_train)
decision_train_prediction = decision_model.predict(X_train)
decision_test_prediction = decision_model.predict(X_test)
decision_train_accuracy = accuracy_score(y_train, decision_train_prediction)
decision_test_accuracy = accuracy_score(y_test, decision_test_prediction)
decision_generalization_gap = decision_train_accuracy - decision_test_accuracy
print("Decision Tree's Training Accuracy: ", decision_train_accuracy)
print("Decision Tree's Testing Accuracy: ", decision_test_accuracy)
print("Decision Tree's Generalization Gap: ", decision_generalization_gap)

new_students = [[3, 60],
                [5, 72],
                [8, 90]]

new_students_logistic_p = logistic_model.predict(new_students)
new_students_decision_p = decision_model.predict(new_students)

for index, label in enumerate(new_students_logistic_p):
    letter = chr(65 + index)
    print(f"Student {letter}'s Logistic Regression's Predicted Class: {label}")

for index, label in enumerate(new_students_decision_p):
    letter = chr(65 + index)
    print(f"Student {letter}'s Decision Tree's Predicted Class: {label}")


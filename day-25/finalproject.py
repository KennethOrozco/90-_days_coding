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

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

train_prediction = model.predict(X_train)
test_prediction = model.predict(X_test)

train_accuracy = accuracy_score(y_train, train_prediction)
test_accuracy = accuracy_score(y_test, test_prediction)


print("Training Accuracy: ", train_accuracy)
print("Testing Accuracy: ", test_accuracy)
print("Learned Coefficients: ",model.coef_)
print("Learned Intercept: ", model.intercept_)

new_students = [
    [2, 55],
    [4, 68],
    [5, 72],
    [7, 85],
    [9, 95]
]

new_students_prediction = model.predict(new_students)
new_students_proba = model.predict_proba(new_students)

for index, (prediction, probability) in enumerate(zip(new_students_prediction, new_students_proba)):
    letter = chr(65 + index)
    print(f"Student {letter}")
    print(f"Predicted Class: {prediction}")
    print(f"Predicted Probability: {probability[1]}")

thresholds = [0.3, 0.5, 0.7]

data = {}

for threshold in thresholds:
    predictions = [1 if probability[1] >= threshold else 0 for probability in new_students_proba]
    data[threshold] = predictions
    print(f"Count of students who passed at a threshold of {threshold}: {sum(predictions)}")

at_three = data[0.3]
at_seven = data[0.7]

for index, (three, seven) in enumerate(zip(at_three, at_seven)):
    letter = chr(65 + index)
    if three != seven:
        print(f" Student {letter}'s Classification label has been changed!")

decision_model = DecisionTreeClassifier(random_state=42)
decision_model.fit(X_train, y_train)
decision_train_prediction = decision_model.predict(X_train)
decision_test_prediction = decision_model.predict(X_test)
decision_train_accuracy = accuracy_score(y_train, decision_train_prediction)
decision_test_accuracy = accuracy_score(y_test, decision_test_prediction)

print(f"Logistic Regression's Training Accuracy: {train_accuracy} -- Decision Tree's Training Accuracy: {decision_train_accuracy}")
print(f"Logistic Regression's Testing Accuracy: {test_accuracy} -- Decision Tree's Testing Accuracy: {decision_test_accuracy}")





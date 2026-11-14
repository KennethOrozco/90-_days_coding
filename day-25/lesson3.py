from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

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
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)
train_probabilities = model.predict_proba(X_train)
test_probabilities = model.predict_proba(X_test)

for train in train_probabilities:
    print(f"Training Probability: {train}")

for test in test_probabilities:
    print(f"Testing Probability: {test}")

train_accuracy = accuracy_score(y_train, train_predictions)
test_accuracy = accuracy_score(y_test, test_predictions)

print("Training Accuracy: ", train_accuracy)
print("Testing Accuracy", test_accuracy)

print(model.coef_)
print(model.intercept_)

new_students = [ [3, 60],
              [7, 85],
              [5,72]]

new_student_proba = model.predict_proba(new_students)
new_student_class = model.predict(new_students)


for index, probability in enumerate(new_student_proba):
    letter = chr(65 + index)
    print(f"Student {letter} -- Predicted Class: {new_student_class[index]} --Class Probability: {probability[1]:.2f}")

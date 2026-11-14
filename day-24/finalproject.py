import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                        2, 3, 5, 7, 9, 4, 6, 8, 10, 1])

attendance = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95,
                       60, 65, 72, 82, 92, 68, 78, 88, 98, 45])

assignments = np.array([1, 2, 2, 3, 4, 5, 6, 7, 8, 9,
                        2, 3, 4, 6, 8, 3, 5, 7, 9, 1])

passed = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
                   0, 0, 1, 1, 1, 0, 1, 1, 1, 0])

X = np.column_stack((study_hours, attendance, assignments))

y = passed

print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

train_prediction = model.predict(X_train)
test_prediction = model.predict(X_test)

train_accuracy = accuracy_score(y_train, train_prediction)
test_accuracy = accuracy_score(y_test, test_prediction)
generalization_gap = train_accuracy - test_accuracy

print("Training Accuracy: ", train_accuracy)
print("Testing Accuracy: ", test_accuracy)
print("Generalization Gap: ", generalization_gap)

for student, (actual, predicted) in enumerate(zip(y_test, test_prediction)):
    letter = chr(65 + student)
    actual_class = "Passed" if actual else "Failed"
    predicted_class = "Passed" if predicted else "Failed"
    print(f"Student{letter} -- Actual Class: {actual_class} -- Predicted Class: {predicted_class}")

new_students = [[3, 60, 2],
                [7, 85, 7],
                [5, 72, 4]]

new_students_prediction = model.predict(new_students)
probabilities = model.predict_proba(new_students)

for index, (prediction, probability) in enumerate(zip(new_students_prediction, probabilities)):
    letter = chr(65 + index)
    passed = "Passed" if prediction else "Failed"
    print(f"Student {letter} -- Predicted Class: {passed} -- Probability: {probability}")
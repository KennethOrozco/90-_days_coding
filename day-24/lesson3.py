from sklearn.tree import DecisionTreeClassifier
import numpy as np

study_hours = np.array([1, 3, 5, 7, 9])

attendance = np.array([50, 65, 75, 85, 95])

passed = np.array([0, 0, 1, 1, 1])


X= np.column_stack((study_hours, attendance))

y = passed

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

prediction = model.predict(X)

print(prediction)

student_a_b = [[4, 70], [8, 90]]

new_prediction = model.predict(student_a_b)

student_a = "passed" if new_prediction[0] else "failed"
student_b = "passed" if new_prediction[1] else "failed"

print(f"Student A: {student_a}")
print(f"Student B: {student_b}")

probabilities = model.predict_proba(student_a_b)
print(probabilities)
print(model.classes_)

for student, (result, probability) in enumerate(zip(new_prediction, probabilities)):
    passed = "Passed" if result else "Failed"
    letter = chr(65 + student)
    print(f"Student {letter}-- Class: {passed} -- Probability: {probability}")

print(probabilities.sum(axis=1))



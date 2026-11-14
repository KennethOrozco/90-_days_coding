import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10])

attendance = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 65, 75, 85, 90, 98])

passed = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1])

X = np.column_stack((study_hours, attendance))

y = passed

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)
train_accuracy = accuracy_score(y_train, train_predict)
test_accuracy = accuracy_score(y_test, test_predict)
gap = train_accuracy - test_accuracy
print("Training accuracy: ", train_accuracy)
print("Testing accuracy: " , test_accuracy)
print("Gap: ", gap)

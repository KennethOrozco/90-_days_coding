import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "exam_score": [43, 50, 54, 62, 66, 73, 77, 84, 89, 95, 98, 100]
}

df = pd.DataFrame(data)

X = df[["study_hours"]]
y = df["exam_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

train_prediction = model.predict(X_train)
test_prediction = model.predict(X_test)

train_mae = mean_absolute_error(y_train, train_prediction)
test_mae = mean_absolute_error(y_test, test_prediction)

gap = test_mae - train_mae

print("Training MAE: ", train_mae)
print("Testing MAE: ", test_mae)
print("Generalization Gap: ", gap)

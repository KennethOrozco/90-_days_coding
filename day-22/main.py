from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# data = {
#     "study_hours": [1, 2, 3, 4, 5, 6],
#     "attendance": [60, 65, 70, 80, 85, 95],
#     "exam_score": [50, 55, 65, 70, 80, 90]
# }

# df = pd.DataFrame(data)

# x = df[["study_hours", "attendance"]]

# y = df["exam_score"]

# shape_x = x.shape

# print(x)
# print(y)
# print(x.shape)
# print(y.shape)
# print(f"Number of Samples: {shape_x[0]} -- Number of Features: {shape_x[1]}")

# print("Predictions: ", prediction)
# print("Actual scores: ", y_test.to_numpy())
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "attendance": [55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
    "exam_score": [42, 48, 53, 60, 65, 72, 78, 85, 90, 96]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance"]]
y = df["exam_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
mae = mean_absolute_error(y_test, prediction)
mse = mean_squared_error(y_test, prediction)
r2 = r2_score(y_test, prediction)
print("MAE Score: ", mae)
print("MSE Score: ", mse)
print("R2 Score: ", r2)

for p , y in zip(prediction, y_test.to_numpy()):
    print(f"Predicted Score: {p} -- Actual Score: {y}")



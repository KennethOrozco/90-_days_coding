import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "attendance": [60, 75, 65, 80, 70, 85, 78, 95, 88, 92, 82, 98],
    "exam_score": [45, 55, 52, 65, 62, 72, 70, 85, 80, 88, 84, 95]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance"]]

y = df["exam_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print("MAE Score: ", mae)
print("MSE Score: ", mse)
print("R2 Score: ", r2)

for x, y in zip(predictions, y_test.to_numpy()):
    print(f"Predicted Score: {x} -- Actual Score: {y}")

user_hours = float(input("Study Hours: "))
user_attendance = float(input("Attendance Percentage: "))

user_df = pd.DataFrame([[user_hours, user_attendance]], columns=["study_hours", "attendance"])

a = model.predict(user_df)

print("Predicted Score for User: ", a[0])



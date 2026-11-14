import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import PolynomialFeatures


X = np.arange(1, 21).reshape(-1, 1)

y = np.array([
    5, 8, 13, 19, 27,
    37, 48, 62, 77, 95,
    114, 135, 158, 183, 210,
    239, 270, 303, 338, 375
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

degrees = [1, 2, 3, 5, 10]

data = []

for degree in degrees:
    poly= PolynomialFeatures(degree=degree, include_bias=False)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    model = LinearRegression()
    model.fit(X_train_poly, y_train)
    
    train_prediction = model.predict(X_train_poly)
    test_prediction = model.predict(X_test_poly)
    train_mae = mean_absolute_error(y_train, train_prediction)
    test_mae = mean_absolute_error(y_test, test_prediction)
    gap = test_mae - train_mae
    machine = {
        "degree": degree,
        "Training MAE Score" : train_mae,
        "Testing MAE Score": test_mae,
        "Generalization Gap": gap
    }
    data.append(machine)

for result in data:
    print(f"Degree: {result["degree"]}")
    print(f"Training Mae Score: {result["Training MAE Score"]}")
    print(f"Testing MAE Score: {result["Testing MAE Score"]}")
    print(f"Generalization Gap: {result["Generalization Gap"]}")

best_model = min(data, key=lambda result:result["Testing MAE Score"])

print("Best Model Degree: ", best_model["degree"])
print("Best Model Testing MAE Score: ", best_model["Testing MAE Score"])


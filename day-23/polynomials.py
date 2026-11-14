import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([3, 6, 11, 18, 27, 38])

poly = PolynomialFeatures(degree=2, include_bias=False)

X_poly = poly.fit_transform(X)

print(X_poly)
print(X_poly.shape)

model = LinearRegression()

model.fit(X_poly, y)

predictions = model.predict(X_poly)

for prediction, actual in zip(predictions, y):
    print(f"Predicted Score: {prediction} -- Actual Score: {actual}")

mae = mean_absolute_error(y, predictions)
print("MAE Score: ", mae)
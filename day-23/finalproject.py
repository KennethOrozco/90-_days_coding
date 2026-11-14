import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

X = np.linspace(-5, 5, 60).reshape(-1, 1)
y = 3 * X.flatten() ** 2 + 2 * X.flatten() + 5
y = y + rng.normal(0, 5, size=len(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

data = []

degrees = [1, 2, 3, 5, 10]

for degree in degrees:
    model = make_pipeline(
        PolynomialFeatures(degree=degree, include_bias=False),
        LinearRegression()
    )
    model.fit(X_train, y_train)
    train_prediction = model.predict(X_train)
    test_prediction = model.predict(X_test)
    train_mae = mean_absolute_error(y_train, train_prediction)
    test_mae = mean_absolute_error(y_test, test_prediction)
    gap = test_mae - train_mae
    result = {
        "degree": degree,
        "train": train_mae,
        "test": test_mae,
        "gap": gap
    }
    data.append(result)
for result in data:
    print(f"Degree: {result["degree"]}")
    print(f"Training MAE: {result["train"]}")
    print(f"Testing MAE: {result["test"]}")
    print(f"Generalization Gap: {result["gap"]}")
cross_data = []

for degree in degrees:
    model = make_pipeline(
        PolynomialFeatures(degree=degree, include_bias=False),
        LinearRegression()
    )
    scores = cross_val_score(
        model,
        X_train,
        y_train,
        cv=5,
        scoring="neg_mean_absolute_error"
    )
    mae_scores = -scores
    average_mae = mae_scores.mean()
    result = {
        "degree": degree,
        "average mae": average_mae
    }
    cross_data.append(result)

for result in cross_data:
    print(f"Degree: {result["degree"]}")
    print(f"Average Validated MAE: {result["average mae"]}")

best_model = min(cross_data, key=lambda result: result["average mae"])

print(best_model["degree"])

train = [result["train"] for result in data]
test = [result["test"] for result in data]
cross_average = [result["average mae"] for result in cross_data]

plt.plot(degrees, train, color="red", label="Training MAE")
plt.plot(degrees, test, color="blue", label="Testing MAE")
plt.plot(degrees, cross_average, color="orange", label="Cross_Validation MAE")
plt.title("MAE Chart")
plt.xlabel("Polynomial Degree")
plt.ylabel("Mean Absolute Error (MAE)")
plt.legend()
plt.show()





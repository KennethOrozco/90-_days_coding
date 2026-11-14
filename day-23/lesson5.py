from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

X = np.arange(1, 21).reshape(-1, 1)

y = np.array([
    5, 8, 13, 19, 27,
    37, 48, 62, 77, 95,
    114, 135, 158, 183, 210,
    239, 270, 303, 338, 375
])

degrees = [1, 2, 3, 5]

data = []

for degree in degrees:
    model = make_pipeline(
        PolynomialFeatures(degree=degree, include_bias=False),
        LinearRegression()
    )
    scores = cross_val_score(
        model,
        X,
        y,
        cv=5,
        scoring="neg_mean_absolute_error"
    )
    mae_scores = -scores
    average_mae = mae_scores.mean()
    models = {
        "degree": degree,
        "average mae": average_mae
    }
    data.append(models)

for result in data:
    print(f"Degree: {result["degree"]}")
    print(f"Average Validation Mae: {result["average mae"]}")

lowest = min(data, key=lambda result: result["average mae"])
print(f"Degree with lowest average validation MAE: {lowest["degree"]} -- Lowest average validation MAE: {lowest["average mae"]}")
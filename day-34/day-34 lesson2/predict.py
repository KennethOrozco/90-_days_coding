import joblib
from pathlib import Path
import numbers
import numpy as np
import pandas as pd
from typing import Any

def validate_features(features: list[float | int] | tuple[float | int, ...], expected_count: int) -> None:
    if len(features) != expected_count:
        raise ValueError(
            f"Expected {expected_count} features, "
            f"recieved {len(features)}"
        )
    for value in features:
        if not isinstance(value, numbers.Real):
            raise TypeError("All features must be real numbers")
        elif isinstance(value, (bool, np.bool_)):
            raise TypeError("Bolean values are not valid features")
        elif not np.isfinite(value):
            raise ValueError("Features must be finite")

def make_prediction(model:Any, features: list[int] | tuple[int]) -> int:
    validate_features(features, model.n_features_in_)
    feature_names = model.feature_names_in_
    input_df = pd.DataFrame([features], columns=feature_names)
    return int(model.predict(input_df)[0])
    
 #Load model   

base_dir = Path(__file__).resolve().parent
model_dir = base_dir / "models"
model_path = model_dir / "breast_cancer_pipeline.joblib"
model = joblib.load(model_path)

#Get a valid observation
test_features = [19.55, 28.77, 133.6, 1207.0, 0.0926, 0.2063, 0.1784,
                 0.1144, 0.1893, 0.06232, 0.8426, 1.199, 7.158, 106.4,
                 0.006356, 0.04765, 0.03863, 0.01519, 0.01936, 0.005252,
                 25.05, 36.27, 178.6, 1926.0, 0.1281, 0.5329, 0.4251, 0.1941, 0.2818, 0.1005]



# Wrong number of features
too_few = test_features[:-1]
too_many = test_features + [5.0]

# Wrong data types
contains_string = test_features.copy()
contains_string[0] = "invalid"

contains_boolean = test_features.copy()
contains_boolean[0] = True

#N Non-finite values 
contains_nan = test_features.copy()
contains_nan[0] = float("nan")

contains_infinity = test_features.copy()
contains_infinity[0] = float("inf")

tests = [too_few, too_many, contains_string, contains_boolean, contains_nan, contains_infinity]

for test in tests:
    try:
        result = make_prediction(model, test)
        print("Prediction:", result)
    except (ValueError, TypeError) as error:
        print("Invalid input:", error)


model_predictions = make_prediction(model, test_features)
print(model_predictions)
    
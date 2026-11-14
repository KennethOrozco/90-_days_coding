from pathlib import Path
import joblib
import json
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
import pytest
import numbers
from ml_capstone.prediction import validate_features, make_prediction

MODELS_DIR = Path(__file__).resolve().parents[2] / "models"

@pytest.fixture
def features():
    data = load_breast_cancer(as_frame=True)
    return data.data.iloc[0].tolist()

@pytest.fixture(scope="module")
def loaded_model():
    model_path = MODELS_DIR / "best_model.joblib"
    return joblib.load(model_path)

@pytest.fixture(scope="module")
def metadata():
    meta_path = MODELS_DIR / "metadata.json"
    with open(meta_path, "r", encoding="utf-8") as file:
        return json.load(file)

    
def test_mode_file_exits():
    assert (MODELS_DIR / "best_model.joblib").is_file()

def test_meta_exist():
    assert (MODELS_DIR / "metadata.json").is_file()

def test_model_loads(loaded_model):
    assert hasattr(loaded_model, "predict")

def test_metadata_required_keys(metadata):
    required = {
        "selected_model",
        "cv_results",
        "test_metrics",
        "feature_names",
        "random_state"
    }

    assert required.issubset(metadata)

def test_feature_names_match(metadata, loaded_model):
    assert metadata["feature_names"] == loaded_model.feature_names_in_.tolist()

@pytest.mark.parametrize("modifier, expected_error, error_msg", [
    pytest.param(
        lambda f: f[:-1],
        ValueError,
        "Expected 30 features, recieved 29",
        id="too_few_features",
    ),
    pytest.param(
        lambda f: f + [5.0],
        ValueError,
        "Expected 30 features, recieved 31",
        id="too_many_features",
    ),
    pytest.param(
        lambda f: ["invalid"] + f[1:],
        TypeError,
        "All features must be real numbers",
        id="contains_string",
    ),
    pytest.param(
        lambda f: [True] + f[1:],
        TypeError,
        "Bolean values are not valid features",
        id="contains_python_bool",
    ),
    pytest.param(
        lambda f: [np.bool_(True)] + f[1:],
        TypeError,
        "Bolean values are not valid features",
        id="contains_numpy_bool",
    ),
    pytest.param(
        lambda f: [float("nan")] + f[1:],
        ValueError,
        "Features must be finite",
        id="contains_nan",
    ),
    pytest.param(
        lambda f: [float("inf")] + f[1:],
        ValueError,
        "Features must be finite",
        id="contains_infinity",
    ),
])

def test_validate_features_raises(features, modifier, expected_error, error_msg):
    bad_features = modifier(features)

    with pytest.raises(expected_error, match=error_msg):
        validate_features(bad_features, 30)



def test_make_prediction(loaded_model, features):
    assert make_prediction(loaded_model, features) in (0, 1)













































# def validate_features(features: list[float | int] | tuple[float | int, ...], expected_count: int) -> None:
#     if len(features) != expected_count:
#         raise ValueError(
#             f"Expected {expected_count} features, "
#             f"recieved {len(features)}"
#         )
#     for value in features:
#         if not isinstance(value, numbers.Real):
#             raise TypeError("All features must be real numbers")
#         elif isinstance(value, (bool, np.bool_)):
#             raise TypeError("Bolean values are not valid features")
#         elif not np.isfinite(value):
#             raise ValueError("Features must be finite")

# def make_prediction(model:Any, features: list[int] | tuple[int]) -> int:
#     validate_features(features, model.n_features_in_)
#     feature_names = model.feature_names_in_
#     input_df = pd.DataFrame([features], columns=feature_names)
#     return int(model.predict(input_df)[0])

# #Get test features

# data = load_breast_cancer(as_frame=True)

# test_features = data.data.iloc[0].tolist()

# # Load model and metadata
# project_root = Path(__file__).resolve().parent.parent

# models_dir = project_root / "models"

# with open(models_dir/ "metadata.json", "r", encoding="utf-8") as file:
#     metadata = json.load(file)

# model = joblib.load(models_dir / "best_model.joblib")

# print(metadata["selected_model"])
# print(metadata["cv_results"])
# print(metadata["test_metrics"])
# print(metadata["feature_names"])
# print(metadata["random_state"])

# print(metadata["feature_names"] == model.feature_names_in_.tolist())

# valid_prediction = make_prediction(model, test_features)


# print(valid_prediction)

# # Wrong number of features
# too_few = test_features[:-1]
# too_many = test_features + [5.0]

# # Wrong data types
# contains_string = test_features.copy()
# contains_string[0] = "invalid"

# contains_boolean = test_features.copy()
# contains_boolean[0] = True

# #N Non-finite values 
# contains_nan = test_features.copy()
# contains_nan[0] = float("nan")

# contains_infinity = test_features.copy()
# contains_infinity[0] = float("inf")

# # Use function for tests
# tests = [too_few, too_many, contains_string, contains_boolean, contains_nan, contains_infinity]

# for test in tests:
#     try:
#         result = make_prediction(model, test)
#         print("Prediction:", result)
#     except (ValueError, TypeError) as error:
#         print("Invalid input:", error)


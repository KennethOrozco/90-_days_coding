from typing import Any
import numpy as np
import pandas as pd
import numbers


def validate_features(features: list[float | int] | tuple[float | int, ...], expected_count: int) -> None:
    if len(features) != expected_count:
        raise ValueError(
            f"Expected {expected_count} features, "
            f"recieved {len(features)}"
        )
    for value in features:
        if isinstance(value, (bool, np.bool_)):
            raise TypeError("Bolean values are not valid features")
        elif not isinstance(value, numbers.Real):
            raise TypeError("All features must be real numbers")
        elif not np.isfinite(value):
            raise ValueError("Features must be finite")

def make_prediction(model:Any, features: list[int] | tuple[int]) -> int:
    validate_features(features, model.n_features_in_)
    feature_names = model.feature_names_in_
    input_df = pd.DataFrame([features], columns=feature_names)
    return int(model.predict(input_df)[0])
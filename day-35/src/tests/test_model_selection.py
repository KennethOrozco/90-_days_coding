from ml_capstone.selection import select_best_model
import pytest

@pytest.mark.parametrize(
        "lr_mean, lr_std, rf_mean, rf_std, expected",
        [
            (100.0, .9, 92.3, 0.8, "Logistic Regression"),
            (80.0, .7, 95.5, .9, "Random Forest"),
            (80.0, .2, 80.0, .6, "Logistic Regression"),
            (80.0, .9, 80.0, .5, "Random Forest"),
            (80.0, .2, 80.0, .2, "Logistic Regression")
        ]
)
def test_select_best_model(lr_mean, lr_std, rf_mean, rf_std, expected):
    assert select_best_model(lr_mean, lr_std, rf_mean, rf_std) == expected
    
    
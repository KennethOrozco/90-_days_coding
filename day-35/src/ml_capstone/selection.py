def select_best_model(
    lr_mean: float,
    lr_std: float,
    rf_mean: float,
    rf_std: float
) -> str:
    if lr_mean > rf_mean:
        return "Logistic Regression"
    elif rf_mean > lr_mean:
        return "Random Forest"
    else:
        if rf_std < lr_std:
            return "Random Forest"
        else:
            return "Logistic Regression"
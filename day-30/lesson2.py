import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
from sklearn.model_selection import train_test_split

def transform_features(df: pd.DataFrame) -> pd.DataFrame:
    results = df.copy()
    scaler = StandardScaler()
    scaled = scaler.fit_transform(results[["annual_income"]])
    results["income_standardized"]  = scaled.ravel()
    minmax = MinMaxScaler()
    minmax_scaled = minmax.fit_transform(results[["age"]])
    results["age_normalized"] = minmax_scaled.ravel()
    results["log_total_spent"] = np.log1p(results["total_spent"])
    return results

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "age": [22, 35, 48, 60, 29, 41, 54, 33],
    "annual_income": [30000, 65000, 110000, 180000, 42000, 85000, 140000, 55000],
    "total_spent": [150, 400, 1200, 5000, 250, 750, 3000, 350],
    "total_orders": [3, 8, 15, 25, 5, 12, 20, 7]
})

df_v2 = transform_features(customers)

print(df_v2)

X = customers[["age", "annual_income", "total_spent", "total_orders"]]

X_train, X_test = train_test_split(
    X,
    test_size=0.25,
    random_state=42
)

scaler = StandardScaler()

scaled = scaler.fit_transform(X_train)
test_scaled_values = scaler.transform(X_test)
print(scaled.shape)
print(scaled.shape)
print(scaled.mean(axis=0))
print(test_scaled_values.mean(axis=0))
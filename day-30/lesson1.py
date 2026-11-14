import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    results = df.copy()
    results["average_order_value"] = (results["total_spent"] / results["total_orders"].replace(0, float("nan")))
    results["orders_per_month"] = (results["total_orders"] / results["months_as_customer"].replace(0, float("nan")))
    results["is_frequent_customer"] = (results["total_orders"] >= 5)
    results["is_inactive"] = (results["days_since_last_order"] > 60)
    return results

                              
customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104, 105, 106],
    "total_spent": [300, 150, 0, 600, 250, 90],
    "total_orders": [5, 3, 0, 12, 2, 1],
    "days_since_last_order": [10, 45, 120, 3, 60, 90],
    "months_as_customer": [12, 6, 2, 24, 10, 3]
})

updated_df = engineer_features(customers)

print(updated_df)

max_average_order_idx = updated_df["average_order_value"].idxmax()

row_data = updated_df.loc[max_average_order_idx]

print(f"Highest average order value:\n {row_data}")

print("Frequent customers count: ", updated_df["is_frequent_customer"].sum())

print(f"Inactive customers: \n {updated_df.loc[updated_df["is_inactive"], "customer_id"]}")

print("Average order per month for all customers: ", updated_df["orders_per_month"].mean())
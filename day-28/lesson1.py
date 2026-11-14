def predict_purchase(age:int, income: float) -> int:
    if age >= 30:
        return 1
    elif income >= 4000:
        return 1
    return 0

def predict_purchase_v2(age: int, income: float) -> int:
    if age >= 30 and income >= 3000:
        return 1
    elif age < 30 and income >= 4500:
        return 1
    return 0

customers = [
    {"age": 22, "income": 2500},
    {"age": 35, "income": 3000},
    {"age": 27, "income": 5000},
    {"age": 42, "income": 6500},
    {"age": 19, "income": 1800},
    {"age": 29, "income": 4200},
    {"age": 31, "income": 2000},
]

predictions = []

for customer in customers:
    purchase = predict_purchase(customer["age"], customer["income"])
    predictions.append(purchase)

for index, prediction in enumerate(predictions, start=1):
    purchased = "Purchased" if prediction == 1 else "Did not Purchase"
    print(f"Customer No.{index}: {purchased}")

purchase_count = sum(predictions)
print(purchase_count)
no_purchase_count = predictions.count(0)
print(no_purchase_count)
percentage_purchase = (purchase_count / len(predictions)) * 100
print(f"{percentage_purchase:.3f}%")

predictions_v2 = []

for customer in customers:
    purchase = predict_purchase_v2(customer["age"], customer["income"])
    predictions_v2.append(purchase)

for index, (prediction_v1, prediction_v2) in enumerate(zip(predictions, predictions_v2), start=1):
    if prediction_v1 != prediction_v2:
        print(f"Customer No.{index} predictions are different.")

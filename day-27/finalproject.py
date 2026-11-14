from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

def evaluate_thresholds(actual: list[int], probabilities: list[float], thresholds: list[float]) -> dict[float, dict]:
    if not all([actual, probabilities, thresholds]):
        return {}
    data = {}
    for threshold in thresholds:
        predictions = [1 if probability >= threshold else 0 for probability in probabilities]
        accuracy = accuracy_score(actual, predictions)
        precision = precision_score(actual, predictions, zero_division=0)
        recall = recall_score(actual, predictions, zero_division=0)
        f1 = f1_score(actual, predictions, zero_division=0)
        matrix = confusion_matrix(actual, predictions, labels=[0, 1])
        tn, fp, fn, tp = matrix.ravel()
        cost = false_positive_cost * fp + false_negative_cost * fn
        data[threshold] = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "matrix": matrix,
            "TN": tn,
            "FP": fp,
            "FN": fn,
            "TP": tp,
            "cost": cost,
            "predictions": predictions
        }
    return data

def best_f1_threshold(results: dict[float, dict]) -> tuple[list[float], float]| None:
    if not results:
        return None
    max_val = max(results[threshold]["f1"] for threshold in results)
    thresholds = [threshold for threshold in results if results[threshold]["f1"] == max_val]
    return thresholds, max_val

def best_pecision_with_recall(results: dict[float, dict], minimum_recall: float) -> list[float] | None:
    if not results:
        return None
    threshold_min_recall = [threshold for threshold in results if results[threshold]["recall"] >= minimum_recall]
    if not threshold_min_recall:
        return None
    max_val = max(results[threshold]["precision"] for threshold in threshold_min_recall)
    qualified = [threshold for threshold in threshold_min_recall if results[threshold]["precision"] == max_val]
    if not qualified:
        print("No threshold satisfied the requirements!")
        return None
    return qualified

def lowest_cost_threshold(results: dict[dict], false_positive_cost: int, false_negative_cost: int) ->  tuple[list[float], float] | None:
    if not results:
        return None
    costs = {}
    for threshold in results:
        cost = false_positive_cost * results[threshold]["FP"] + false_negative_cost * results[threshold]["FN"]
        costs[threshold] = cost
    lowest_cost = min(costs[cost] for cost in costs)
    return [threshold for threshold in costs if costs[threshold] == lowest_cost], lowest_cost
    

actual = [
    0, 0, 1, 0, 1, 0, 0, 1, 0, 1,
    0, 0, 1, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 0, 1, 0, 1, 0, 0, 1, 0
]

probabilities = [
    0.10, 0.25, 0.65, 0.40, 0.80,
    0.15, 0.55, 0.90, 0.30, 0.70,
    0.20, 0.45, 0.85, 0.35, 0.60,
    0.75, 0.50, 0.10, 0.95, 0.25,
    0.55, 0.40, 0.15, 0.80, 0.30,
    0.65, 0.20, 0.45, 0.90, 0.05
]

thresholds = [0.20, 0.35, 0.50, 0.65, 0.80]

minimum_recall = 0.80
false_positive_cost = 25
false_negative_cost = 400

results = evaluate_thresholds(actual, probabilities, thresholds)

highest_f1_threshold, highest_f1_score = best_f1_threshold(results)

qualified_recall = best_pecision_with_recall(results, minimum_recall)

low_cost_threshold, lowest_cost = lowest_cost_threshold(results, false_positive_cost, false_negative_cost)

for threshold in results:
    print(f"Threshold: {threshold}")
    print(f"Accuracy: {results[threshold]["accuracy"]}")
    print(f"Precision: {results[threshold]["precision"]}")
    print(f"Recall: {results[threshold]["recall"]}")
    print(f"F1: {results[threshold]["f1"]}")
    print(f"Matrix:\n{results[threshold]["matrix"]}")
    print(f"Cost: {results[threshold]["cost"]}")

print("Best F1 threshold: ", highest_f1_threshold)
print("Best precison threshold subject to minimum recall: ", qualified_recall)
print("Lowest-cost threshold: ", low_cost_threshold)





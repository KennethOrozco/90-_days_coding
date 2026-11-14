from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

actual = [
    0, 0, 0, 1, 0,
    1, 0, 0, 1, 0,
    1, 0, 0, 0, 1,
    0, 1, 0, 0, 1
]

probabilities = [
    0.10, 0.35, 0.20, 0.45, 0.60,
    0.85, 0.15, 0.40, 0.75, 0.25,
    0.90, 0.55, 0.30, 0.05, 0.65,
    0.50, 0.95, 0.70, 0.20, 0.80
]

thresholds = [0.30, 0.50, 0.70, 0.90]

data = {}

for threshold in thresholds:
    predictions = [1 if probability >= threshold else 0 for probability in probabilities]
    accuracy = accuracy_score(actual, predictions)
    precision = precision_score(actual, predictions, zero_division=0)
    recall = recall_score(actual, predictions, zero_division=0)
    f1 = f1_score(actual, predictions, zero_division=0)
    matrix = confusion_matrix(actual, predictions, labels=[0, 1])
    tn, fp, fn, tp = matrix.ravel()
    data[threshold] = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "matrix": matrix,
        "TN": tn,
        "FP": fp,
        "FN": fn,
        "TP": tp
    }

eighty_recall = [threshold for threshold in data if data[threshold]["recall"] >= .80]
print(eighty_recall)
best_qualified = []
if not eighty_recall:
    eighty_recall = 0
else:
    highest_precision = max(data[threshold]["precision"] for threshold in eighty_recall)
    best_qualified = [threshold for threshold in eighty_recall if data[threshold]["precision"] == highest_precision]

if best_qualified:
    print(best_qualified)
else:
    print("No threshold met the qualifications")

threshold_cost = {}
for threshold in data:
    cost = 20 * data[threshold]["FP"] + 500 * data[threshold]["FN"]
    threshold_cost[threshold] = cost

lowest = min(value for value in threshold_cost.values())

lowest_error_cost = [threshold for threshold in threshold_cost if threshold_cost[threshold] == lowest]

print(lowest_error_cost)

highest_f1 =  max(data[threshold]["f1"] for threshold in data)

threshold_high_f1 = [threshold for threshold in data if data[threshold]["f1"] == highest_f1]

print("highest f1: ", threshold_high_f1)
print("best precision with qualified recall: ", best_qualified)
print("lowest error cost: ", lowest_error_cost)









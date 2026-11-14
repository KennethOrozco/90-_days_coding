from sklearn.metrics import (
    precision_recall_curve,
    precision_score,
    recall_score
)


actual = [
    0, 0, 1, 0, 1,
    1, 0, 1, 0, 1,
    0, 0, 1, 0, 1
]

probabilities = [
    0.10, 0.25, 0.40, 0.35, 0.55,
    0.70, 0.60, 0.85, 0.20, 0.95,
    0.15, 0.30, 0.75, 0.45, 0.90
]

precision_values, recall_values, thresholds = precision_recall_curve(actual, probabilities)
print(precision_values)
print(recall_values)
print(thresholds)

print(len(precision_values))
print(len(recall_values))
print(len(thresholds))

scores = {}



for precision, recall, threshold in zip(precision_values, recall_values, thresholds):
    print(f"Threshold: {threshold}")
    print(f"Precision Score: {precision:.3f}")
    print(f"Recall Score: {recall}")
    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = 2 * precision * recall / (precision + recall)
    scores[threshold] = {"precision": precision, "recall": recall, "f1": f1}

max_val = max(scores[threshold]["f1"] for threshold in scores)

highest_f1 = [threshold for threshold in scores if scores[threshold]["f1"] == max_val]

print(highest_f1)

lowest_threshold = min(thresholds)

mid = len(thresholds) // 2
middle_threshold = thresholds[mid]

highest_threshold = max(thresholds)

test_thresholds = [lowest_threshold, middle_threshold, highest_threshold]

manual_data = {}

for threshold in test_thresholds:
    predictions = [1 if probability >= threshold else 0 for probability in probabilities]
    precision = precision_score(actual, predictions, zero_division=0)
    recall = recall_score(actual, predictions, zero_division=0)
    manual_data[threshold] = {
        "precision": precision,
        "recall": recall
    }


for threshold in test_thresholds:
    if abs(scores[threshold]["precision"]  - manual_data[threshold]["precision"]) < 1e-9:
        print("Precision score is the same!")
    if abs(scores[threshold]["recall"]  - manual_data[threshold]["recall"]) < 1e-9:
        print("Recall score is the same!")





    

